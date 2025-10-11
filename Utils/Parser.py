import json
import re

from Utils.Store import store
from Utils.Consts import STORY_PACK,FIELD_MAP_SORDLAND,FIELD_MAP_RIZIA
from Utils.Utils import atomicWrite,debounce
from Models.Metadata import Metadata
from Models.Sordland import Sordland
from Models.Rizia import Rizia


@debounce(0.3)
def parse(file):
    with open(file,"r",encoding="utf-8") as f:
        data=json.load(f)
    metadata=Metadata(data["campaignName"],data["currentStoryPack"],data["turnNo"],data["version"])
    store.metadata=metadata

    variables={}
    for k,v in re.findall(r'\["([^"]+)"\]=("(?:(?:\\.|[^"\\])*)"|[^,}]+)',data["variables"]):
        v=v.strip()
        if v=="true":
            v=True
        elif v=="false":
            v=False
        elif re.fullmatch(r"[+-]?\d+",v):
            v=int(v)
        elif re.fullmatch(r"[+-]?\d+\.\d+",v):
            v=float(v)
        else:
            v=v.replace("\"","")
        variables[k]=v
    store.variables=variables.copy()

    sordland=Sordland(**{field:variables[key] for field,key in FIELD_MAP_SORDLAND.items()})
    rizia=Rizia(**{field:variables[key] for field,key in FIELD_MAP_RIZIA.items()})
    store.sordland=sordland
    store.rizia=rizia

    return (metadata,sordland,rizia)

@debounce(0.3)
def apply(file):
    for storyPack in STORY_PACK:
        for field,key in STORY_PACK[storyPack]["field_map"].items():
            store.variables[key]=getattr(getattr(store,storyPack),field)

    s="Variable={"

    for k,v in store.variables.items():
        s+="[\""+k+"\"]="
        match v:
            case bool():
                s+=str(v).lower()
            case int() | float():
                s+=str(v)
            case _:
                s+="\""+v+"\""
        s+=", "

    if s.endswith(", "):
        s=s[:-2]
    s+="}; "

    with open(file,"r",encoding="utf-8") as f:
        data=json.load(f)
    data["variables"]=s
    atomicWrite(file,data)

    return s

@debounce(0.3)
def maxMoney(file):
    parse(file)
    store.sordland.governmentBudget=store.variables.get("BaseGame.Sordland_HUDStat_GovernmentBudget_Max",99)
    store.sordland.personalWealth=store.variables.get("BaseGame.Sordland_HUDStat_PersonalWealth_Max",99)
    store.rizia.resourcesBudget=store.variables.get("RiziaDLC.Rizia_HUDStat_Budget_Max",99)
    store.rizia.resourcesAuthority=store.variables.get("RiziaDLC.Rizia_HUDStat_Authority_Max",99)
    store.rizia.resourcesEnergy=store.variables.get("RiziaDLC.Rizia_HUDStat_Energy_Max",99)
    apply(file)
    store.clear()