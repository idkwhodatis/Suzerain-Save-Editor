from enum import Enum
from pathlib import Path

import dearpygui.dearpygui as dpg

from Utils.Store import store
from Utils.Consts import STORY_PACK
from Utils.Theme import fonts
from Utils.Parser import parse
from Utils.FileHandler import save
from Utils.i18n import i18n


footerOffset=175

def inputCallback(sender,app_data,user_data):
    setattr(getattr(store,user_data),sender,app_data)

def tabCallback(sender,app_data,user_data):
    store.tab=dpg.get_item_alias(app_data)
    for sp in STORY_PACK:
        dpg.configure_item("fields"+sp,show=(store.tab==sp))

def resizeCallback(sender,app_data):
    dpg.configure_item("body",height=dpg.get_viewport_height()-footerOffset)

def backCallback(sender,app_data,user_data):
    dpg.configure_item("Select",show=True)
    dpg.set_primary_window("Select",True)
    dpg.delete_item("Edit")
    dpg.configure_item("save",enabled=False)

def editWindow(width,height):
    parse(str(Path(store.saveDir)/store.currFile))

    with dpg.window(tag="Edit",no_scrollbar=True,no_scroll_with_mouse=True):
        dpg.add_text(tag="currFile",default_value=store.currFile)
        dpg.add_separator()

        with dpg.menu_bar(show=False):
            pass

        with dpg.group(tag="header",horizontal=True):
            back=dpg.add_button(tag="iconBack",label=chr(0xE5C4),user_data="Back",callback=backCallback)
            dpg.bind_item_font(back,fonts["fontICON"])
            dpg.add_spacer(width=1)
            with dpg.tab_bar(tag="tab",callback=tabCallback):
                for sp in STORY_PACK:
                    with dpg.tab(label=sp.capitalize(),tag=sp):
                        pass

        with dpg.child_window(tag="body",autosize_x=True,horizontal_scrollbar=False,border=False,height=height-footerOffset):
            for sp in STORY_PACK:
                with dpg.group(tag="fields"+sp,show=True if sp=="sordland" else False):
                    for k,v in STORY_PACK[sp]["group"].items():
                        with dpg.collapsing_header(label=i18n(k),user_data=k,default_open=True):
                            for i in v:
                                kwargs=dict(tag=i,user_data=sp,callback=inputCallback)
                                curr=getattr(getattr(store,sp),i)
                                if type(curr)==int:
                                    with dpg.group(horizontal=True):
                                        dpg.add_text(i18n(i),user_data=i)
                                        dpg.add_input_int(label="",default_value=curr,step=5,width=150,**kwargs)
                                elif type(curr)==str:
                                    with dpg.group(horizontal=True):
                                        dpg.add_text(i18n(i),user_data=i)
                                        dpg.add_input_text(label="",default_value=curr,**kwargs)
                                elif type(curr)==bool:
                                    with dpg.group(horizontal=True):
                                        dpg.add_text(i18n(i),user_data=i)
                                        dpg.add_checkbox(label="",default_value=curr,**kwargs)
                                elif isinstance(curr,Enum):
                                    with dpg.group(horizontal=True):
                                        dpg.add_text(i18n(i),user_data=i)
                                        dpg.add_combo(items=[e.value for e in type(curr)],default_value=curr.value,**kwargs)

        dpg.add_separator()
        with dpg.group(tag="footer",horizontal=True):
            dpg.add_button(label=i18n("Save"),user_data="Save",callback=save)
            dpg.add_spacer(width=1)
            dpg.add_button(label=i18n("Close"),user_data="Close",callback=backCallback)

    if not dpg.does_item_exist("resizeHandler"):
        with dpg.item_handler_registry(tag="resizeHandler") as handler:
            dpg.add_item_resize_handler(callback=resizeCallback)

    dpg.bind_item_handler_registry("Edit","resizeHandler")