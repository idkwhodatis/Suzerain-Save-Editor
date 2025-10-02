import dearpygui.dearpygui as dpg

from Utils.Theme import fonts
from Utils.Store import store
from Utils.FileHandler import getFiles
from Utils.i18n import i18n


headerOffset=140
tabs=("Save Files","Backup Files")

def buildTables():
    dpg.add_table_column(init_width_or_weight=5,parent="tableSaveFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableSaveFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableSaveFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableSaveFiles")
    for i in store.saveFiles:
        print(i)
        with dpg.table_row(parent="tableSaveFiles"):
            dpg.add_text(i)
            dpg.add_button(label=i18n("Backup"),user_data="Backup")
            dpg.add_button(label=i18n("Max Money"),user_data="Max Money")
            dpg.add_selectable(span_columns=True,callback=editCallback)

    dpg.add_table_column(init_width_or_weight=10,parent="tableBackupFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableBackupFiles")
    dpg.add_table_column(init_width_or_weight=0,parent="tableBackupFiles")
    for i in store.backupFiles:
        with dpg.table_row(parent="tableBackupFiles"):
            dpg.add_text(i)
            dpg.add_button(label=i18n("Restore"),user_data="Restore")

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
    print(app_data,user_data)

def tabCallback(sender,app_data,user_data):
    store.tabSelect=dpg.get_item_alias(app_data)
    for tab in tabs:
        dpg.configure_item("table"+tab.replace(" ",""),show=(store.tabSelect==tab))

def selectWindow(width,height):
    dpg.add_file_dialog(tag="dirDialog",label=i18n("SaveDir"),default_path=store.saveDir,directory_selector=True,show=False,width=width-100,height=height-400,callback=dirDialogCallback,user_data="SaveDir")

    with dpg.window(tag="Select",no_scrollbar=True,no_scroll_with_mouse=True):
        with dpg.menu_bar(show=False):
            pass

        with dpg.group():
            with dpg.tab_bar(tag="tabFile",callback=tabCallback):
                for tab in tabs:
                    with dpg.tab(label=i18n(tab),tag=tab,user_data=tab):
                        pass
            with dpg.group(horizontal=True):
                dir=dpg.add_button(tag="icon",label=chr(0xF07C),callback=lambda:dpg.show_item("dirDialog"))
                dpg.bind_item_font(dir,fonts["fontICON"])
                dpg.add_text(tag="saveDir",default_value=store.saveDir)
        dpg.add_separator()

        with dpg.child_window(tag="table",autosize_x=True,horizontal_scrollbar=False,border=False,height=height-headerOffset):
            with dpg.table(tag="tableSaveFiles",header_row=False,borders_innerH=True):
                pass

            with dpg.table(tag="tableBackupFiles",header_row=False,borders_innerH=True,show=False):
                pass
            buildTables()