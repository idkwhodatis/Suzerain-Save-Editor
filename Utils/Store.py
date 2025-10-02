import json
from pathlib import Path

from platformdirs import user_data_dir

from Utils.Utils import atomicWrite


class PersisStore():
    persistFields=["locale","autoBackup","saveDir"]

    @staticmethod
    def exists():
        configDir=Path(user_data_dir("SuzerainSaveEditor","idkwhodatis"))
        configDir.mkdir(parents=True,exist_ok=True)
        return configDir/"settings.json"

    @staticmethod
    def get(store):
        configFile=PersisStore.exists()
        if configFile.exists():
            with configFile.open("r", encoding="utf-8") as f:
                data=json.load(f)
                store._noPersist=True
                for i in data:
                    setattr(store,i,data[i])
                store._noPersist=False

    @staticmethod
    def set(store):
        data={}
        for i in PersisStore.persistFields:
            data[i]=getattr(store,i)
        atomicWrite(PersisStore.exists(),data)

class Store:
    def __init__(self):
        self._noPersist=True

        self.locale="en"
        self.autoBackup=False
        self.saveDir=""

        self.tab="sordland"
        self.tabSelect="Save Files"

        self.saveFiles=[]
        self.backupFiles=[]

        self.currFile=""
        self.variables={}
        self.metadata=None
        self.sordland=None
        self.rizia=None

        self._noPersist=False

    def __setattr__(self,name,value):
        super().__setattr__(name,value)
        if not self._noPersist and name in PersisStore.persistFields:
            PersisStore.set(self)

    def clear(self):
        self.currFile=""
        self.variables.clear()
        self.metadata=None
        self.sordland=None
        self.rizia=None

store=Store()