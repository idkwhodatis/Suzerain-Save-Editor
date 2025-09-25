import json
import re

from Utils.Store import store
from Utils.Consts import FIELD_MAP_SORDLAND,FIELD_MAP_RIZIA
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
    store["variables"]=variables.copy()

    sordland=Sordland(**{field:variables[key] for field,key in FIELD_MAP_SORDLAND.items()})
    rizia=Rizia(**{field:variables[key] for field,key in FIELD_MAP_RIZIA.items()})

    return (metadata,sordland,rizia)

def apply(file):
    s="Variable={"

    for k,v in store["variables"].items():
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
    with open(file,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

    return s