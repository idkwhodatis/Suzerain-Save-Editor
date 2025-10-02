from pathlib import Path
import dearpygui.dearpygui as dpg

from Windows.EditWindow import editWindow
from Utils.Theme import fonts
from Utils.Store import store
from Utils.FileHandler import getFiles
from Utils.Utils import atomicBackup,atomicRestore,atomicDelete
from Utils.Parser import maxMoney
from Utils.i18n import i18n


headerOffset=140
tabs=("Save Files","Backup Files")

def dirDialogCallback(sender,app_data,user_data):
    store.saveDir=app_data["file_path_name"]
    dpg.set_value("saveDir",store.saveDir)
    dpg.configure_item("dirDialog",default_path=store.saveDir)
    getFiles(store.saveDir)

    dpg.delete_item("tableSaveFiles",children_only=True)
    dpg.delete_item("tableBackupFiles",children_only=True)
    buildTables()

def editCallback(sender,app_data,user_data):
    dpg.set_value(sender,value=False)
    store.currFile=user_data
    editWindow(700,800)
    dpg.configure_item("Select",show=False)
    dpg.set_primary_window("Edit",True)
    dpg.configure_item("save",enabled=True)

def tabCallback(sender,app_data,user_data):
    store.tabSelect=dpg.get_item_alias(app_data)
    for tab in tabs:
        dpg.configure_item("table"+tab.replace(" ",""),show=(store.tabSelect==tab))

def popupCallback(file,label):
    dpg.configure_item("popup",show=True)
    dpg.set_value("popupFile",value=file)
    dpg.set_value("popupLabel",value=i18n(label))
    getFiles(store.saveDir)
    dpg.delete_item("tableSaveFiles",children_only=True)
    dpg.delete_item("tableBackupFiles",children_only=True)
    buildTables()

def backupCallback(sender,app_data,user_data):
    atomicBackup(Path(store.saveDir)/sender[:-1])
    popupCallback(sender[:-1],"Backed Up")

def restoreCallback(sender,app_data,user_data):
    atomicRestore(Path(store.saveDir)/sender[:-1])
    popupCallback(sender[:-1],"Restored")

def deleteCallback(sender,app_data,user_data):
    atomicDelete(Path(store.saveDir)/sender[:-1])
    popupCallback(sender[:-1],"Deleted")

def maxMoneyCallback(sender,app_data,user_data):
    maxMoney(str(Path(store.saveDir)/sender[:-1]))
    popupCallback(sender[:-1],"Max Moneyed")

def buildTables():
    dpg.add_table_column(init_width_or_weight=5,parent="tableSaveFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableSaveFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableSaveFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableSaveFiles")
    for i in store.saveFiles:
        with dpg.table_row(parent="tableSaveFiles"):
            dpg.add_text(i)
            dpg.add_button(tag=i+"B",label=i18n("Backup"),user_data="Backup",callback=backupCallback)
            dpg.add_button(tag=i+"M",label=i18n("Max Money"),user_data="Max Money",callback=maxMoneyCallback)
            dpg.add_selectable(span_columns=True,callback=editCallback,user_data=i)

    dpg.add_table_column(init_width_or_weight=5,parent="tableBackupFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableBackupFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableBackupFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableBackupFiles")
    for i in store.backupFiles:
        with dpg.table_row(parent="tableBackupFiles"):
            dpg.add_text(i)
            dpg.add_button(tag=i+"R",label=i18n("Restore"),user_data="Restore",callback=restoreCallback)
            dpg.add_button(tag=i+"D",label=i18n("Delete"),user_data="Delete",callback=deleteCallback)

def selectWindow(width,height):
    dpg.add_file_dialog(tag="dirDialog",label=i18n("SaveDir"),default_path=store.saveDir,directory_selector=True,show=False,width=width-100,height=height-400,callback=dirDialogCallback,user_data="SaveDir")

    with dpg.window(tag="Select",no_scrollbar=True,no_scroll_with_mouse=True):
        dpg.add_button(tag="dummy",show=False)
        with dpg.popup("dummy",modal=True,tag="popup"):
            dpg.add_text("",tag="popupFile")
            dpg.add_text("",tag="popupLabel")
            dpg.add_button(label=i18n("Close"),user_data="Close",callback=lambda:dpg.configure_item("popup",show=False))

        with dpg.menu_bar(show=False):
            pass

        with dpg.group():
            with dpg.tab_bar(tag="tabFile",callback=tabCallback):
                for tab in tabs:
                    with dpg.tab(label=i18n(tab),tag=tab,user_data=tab):
                        pass
            with dpg.group(horizontal=True):
                dir=dpg.add_button(tag="iconDir",label=chr(0xE2C8),callback=lambda:dpg.show_item("dirDialog"))
                dpg.bind_item_font(dir,fonts["fontICON"])
                dpg.add_text(tag="saveDir",default_value=store.saveDir)
        dpg.add_separator()

        with dpg.child_window(tag="table",autosize_x=True,horizontal_scrollbar=False,border=False,height=height-headerOffset):
            with dpg.table(tag="tableSaveFiles",header_row=False,borders_innerH=True):
                pass
            with dpg.table(tag="tableBackupFiles",header_row=False,borders_innerH=True,show=False):
                pass
            buildTables()
