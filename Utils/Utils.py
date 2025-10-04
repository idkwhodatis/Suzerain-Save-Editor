import functools
import json
import os
import sys
from pathlib import Path
import shutil
import time


def debounce(wait):
    def decorator(fn):
        last_call=[0]
        @functools.wraps(fn)
        def wrapped(*args,**kwargs):
            now=time.time()
            if now-last_call[0]>=wait:
                last_call[0]=now
                return fn(*args,**kwargs)
        return wrapped
    return decorator

@debounce(0.3)
def atomicWrite(file,data):
    if type(file)==str:
        file=Path(file)
    temp=file.with_name(file.name+".tmp")
    with temp.open("w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp,file)

@debounce(0.3)
def atomicBackup(file):
    if type(file)==str:
        file=Path(file)
    shutil.copy2(file,file.with_name(file.name+".bkup"))

@debounce(0.3)
def atomicRestore(file):
    if type(file)==str:
        file=Path(file)
    temp=file.with_name(file.name+".tmp")
    shutil.copy2(file,temp)
    with open(temp,"rb") as f:
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp,file)

@debounce(0.3)
def atomicDelete(file):
    if type(file)==str:
        file=Path(file)
    file.unlink(missing_ok=True)

def assets(*parts):
    if getattr(sys,"frozen",False):
        base=Path(sys.argv[0]).resolve().parent
    else:
        base=Path(__file__).resolve().parents[1]
    return str(base.joinpath(*parts))