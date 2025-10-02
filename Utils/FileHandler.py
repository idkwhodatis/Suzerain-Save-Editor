import platform
from pathlib import Path

from Utils.Store import store


def getDir():
    system=platform.system()
    home=Path.home()

    path=None
    if system=="Windows":
        path=home/"AppData"/"LocalLow"/"Torpor Games"/"Suzerain"
    elif system=="Darwin":
        path=home/"Library"/"Application Support"/"Torpor Games"/"Suzerain"
    elif system=="Linux":
        path=home/".steam"/"steam"/"steamapps"/"compatdata"/"1207650"/"pfx"/"drive_c"/"users"/"steamuser"/"AppData"/"LocalLow"/"Torpor Games"/"Suzerain"
    store.saveDir=str(path) if path.is_dir() else ""

def getFiles(dir):
    prefixes=("Active","Auto","Turn","Final")
    prefixPriority={p:i for i,p in enumerate(prefixes)}

    results=[]
    for path in Path(dir).rglob("*.json"):
        for prefix in prefixes:
            if path.name.startswith(prefix):
                results.append((path.name,str(path),path.stat().st_mtime,prefixPriority[prefix]))
                break
    results.sort(key=lambda x:(-x[2],x[3]))
    store.saveFiles={name:path for name,path,_,_ in results}

    backups={}
    for path in Path(dir).rglob("*.bkup"):
        for prefix in prefixes:
            if path.name.startswith(prefix):
                backups[path.name]=str(path)
                break
    store.backupFiles=backups