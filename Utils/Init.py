import dearpygui.dearpygui as dpg

from Utils.Store import store,PersisStore
from Utils.FileHandler import getDir,getFiles


def init():
    PersisStore.get(store)
    if not store.saveDir:
        getDir()
    getFiles(store.saveDir)