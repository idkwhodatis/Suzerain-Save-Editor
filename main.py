from enum import Enum

import dearpygui.dearpygui as dpg

from Utils.Store import store
from Utils.Consts import STORY_PACK
from Utils.Parser import parse,apply
from Utils.i18n import i18n

print(parse("./sample.json")[1].ewaldOpinion)
# apply("./sample.json")


def input_callback(sender,app_data,user_data):
    setattr(getattr(store,user_data),sender,app_data)

def tab_callback(sender,app_data,user_data):
    store.tab=dpg.get_item_label(app_data).lower()
    for sp in STORY_PACK:
        dpg.configure_item("fields"+sp,show=(store.tab==sp))

def resize_callback(sender,app_data):
    print(dpg.get_viewport_height())
    dpg.configure_item("body",height=dpg.get_viewport_height()-105)

width,height=700,800

dpg.create_context()
dpg.create_viewport(title='Suzerain Save Editor',width=width,height=height)

with dpg.item_handler_registry(tag="resize handler") as handler:
    dpg.add_item_resize_handler(callback=resize_callback)

with dpg.window(tag="Edit",no_scrollbar=True,no_scroll_with_mouse=True):
    # with dpg.tab_bar():
    #     dpg.add_tab_button(label="Back")
    #     for sp in STORY_PACK:
    #         with dpg.tab(label=sp,tag=sp):
    #             for k,v in STORY_PACK[sp]["group"].items():
    #                 with dpg.collapsing_header(label=k,default_open=True):
    #                     for i in v:
    #                         kwargs=dict(tag=i,user_data=sp,callback=input_callback)
    #                         curr=getattr(getattr(store,sp),i)
    #                         if type(curr)==int:
    #                             with dpg.group(horizontal=True):
    #                                 dpg.add_text(i18n(i))
    #                                 dpg.add_input_int(label="",default_value=curr,width=250,step=5,**kwargs)
    #                         elif type(curr)==str:
    #                             with dpg.group(horizontal=True):
    #                                 dpg.add_text(i18n(i))
    #                                 dpg.add_input_text(label="",default_value=curr,**kwargs)
    #                         elif type(curr)==bool:
    #                             with dpg.group(horizontal=True):
    #                                 dpg.add_text(i18n(i))
    #                                 dpg.add_checkbox(label="",default_value=curr,**kwargs)
    #                         elif isinstance(curr,Enum):
    #                             with dpg.group(horizontal=True):
    #                                 dpg.add_text(i18n(i))
    #                                 dpg.add_combo(items=[e.value for e in type(curr)],default_value=curr.value,width=250,**kwargs)
    #             for i in range(20):
    #                 with dpg.group(horizontal=True):
    #                     dpg.add_text("")
    #                     dpg.add_input_text(label="")
    # # dpg.add_button(label="Save",callback=lambda:apply("./sample.json"))
    # dpg.add_button(label="Save",callback=lambda:dump_scrollables())
    
    with dpg.group(tag="header",horizontal=True):
        dpg.add_button(label="Back")
        dpg.add_spacer(width=1)
        with dpg.tab_bar(tag="tab",callback=tab_callback):
            for sp in STORY_PACK:
                with dpg.tab(label=sp.capitalize(),tag=sp):
                    pass

    with dpg.child_window(tag="body",autosize_x=True,horizontal_scrollbar=False,border=False,height=height-105):
        for sp in STORY_PACK:
            with dpg.group(tag="fields"+sp,show=True if sp=="sordland" else False):
                for k,v in STORY_PACK[sp]["group"].items():
                    with dpg.collapsing_header(label=k,default_open=True):
                        for i in v:
                            kwargs=dict(tag=i,user_data=sp,callback=input_callback)
                            curr=getattr(getattr(store,sp),i)
                            if type(curr)==int:
                                with dpg.group(horizontal=True):
                                    dpg.add_text(i18n(i))
                                    dpg.add_input_int(label="",default_value=curr,width=250,step=5,**kwargs)
                            elif type(curr)==str:
                                with dpg.group(horizontal=True):
                                    dpg.add_text(i18n(i))
                                    dpg.add_input_text(label="",default_value=curr,**kwargs)
                            elif type(curr)==bool:
                                with dpg.group(horizontal=True):
                                    dpg.add_text(i18n(i))
                                    dpg.add_checkbox(label="",default_value=curr,**kwargs)
                            elif isinstance(curr,Enum):
                                with dpg.group(horizontal=True):
                                    dpg.add_text(i18n(i))
                                    dpg.add_combo(items=[e.value for e in type(curr)],default_value=curr.value,width=250,**kwargs)
                for i in range(20):
                    dpg.add_input_text(label="")

    dpg.add_separator()
    with dpg.group(tag="footer",horizontal=True):
        dpg.add_button(label="Save",callback=lambda:print(dpg.get_value("tab"),dpg.get_item_label(dpg.get_value("tab"))))
        dpg.add_spacer(width=1)
        dpg.add_button(label="Cancel",callback=lambda:(print(dpg.get_viewport_height(),print(dpg.get_item_rect_size("Edit")))))

dpg.bind_item_handler_registry("body","resize handler")

# dpg.bind_theme(theme)
dpg.setup_dearpygui()

# dpg.show_item_registry()

dpg.show_viewport()
dpg.set_primary_window("Edit",True)
dpg.start_dearpygui()

dpg.destroy_context()
