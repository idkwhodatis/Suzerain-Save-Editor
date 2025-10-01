import json
import os
from pathlib import Path

def atomicWrite(file,data):
    if type(file)==str:
        file=Path(file)
    temp=file.with_suffix(".tmp")
    with temp.open("w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp,file)