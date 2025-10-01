import platform
from pathlib import Path
import pathlib

def getDir():
    system=platform.system()
    home=Path.home()

    if system=="Windows":
        path=home/"AppData"/"LocalLow"/"Torpor Games"/"Suzerain"
        return str(path) if path.is_dir() else ""
    elif system=="Darwin":
        path=home/"Library"/"Application Support"/"Torpor Games"/"Suzerain"
        return str(path) if path.is_dir() else ""
    elif system=="Linux":
        path=home/".steam"/"steam"/"steamapps"/"compatdata"/"1207650"/"pfx"/"drive_c"/"users"/"steamuser"/"AppData"/"LocalLow"/"Torpor Games"/"Suzerain"
        return str(path) if path.is_dir() else ""
    else:
        return ""

def getFiles(dir):
    prefixes=("Active","Auto","Turn","Final")
    prefix_priority={p:i for i,p in enumerate(prefixes)}

    results=[]
    for path in pathlib.Path(dir).rglob("*.json"):
        for prefix in prefixes:
            if path.name.startswith(prefix):
                results.append((path.name,str(path),path.stat().st_mtime,prefix_priority[prefix]))
                break

    results.sort(key=lambda x:(-x[2],x[3]))

    return {name:full_path for name,full_path,_,_ in results}