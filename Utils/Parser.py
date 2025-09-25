import json
import re

from Utils.Store import store
from Models.Metadata import Metadata
from Models.Sordland import Sordland
from Models.Rizia import Rizia

def parse(file):
    with open(file,"r",encoding="utf-8") as f:
        data=json.load(f)
    metadata=Metadata(data["campaignName"],data["currentStoryPack"],data["turnNo"])

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
    store["variables"]=variables

    sordland=Sordland(**{field:variables[key] for field,key in FIELD_MAP_SORDLAND.items()})
    rizia=Rizia(**{field:variables[key] for field,key in FIELD_MAP_RIZIA.items()})

    return (metadata,sordland,rizia)

FIELD_MAP_SORDLAND={
    "governmentBudget":"BaseGame.GovernmentBudget",
    "personalWealth":"BaseGame.PersonalWealth",
    "economy":"BaseGame.Economy",
    "publicOpinion":"BaseGame.Public_Opinion",
    "bludishOpinion":"BaseGame.Bludish_Opinion"
}

FIELD_MAP_RIZIA={
    "resourcesBudget":"RiziaDLC.Resources_Budget",
    "resourcesAuthority":"RiziaDLC.Resources_Authority",
    "resourcesEnergy":"RiziaDLC.Resources_Energy"
}

def apply():
    s="Variable={"

    for k,v in store["variables"].items():
        s+="[\\\""+k+"\\\"]="
        match v:
            case bool():
                s+=str(v).lower()
            case int() | float():
                s+=str(v)
            case _:
                s+="\\\""+v+"\\\""
        s+=", "

    if s.endswith(", "):
        s=s[:-2]
    s+="}; "

    return s