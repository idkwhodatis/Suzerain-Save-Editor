from enum import Enum

import dearpygui.dearpygui as dpg

from Utils.Store import store
from Utils.Consts import GROUP_SORDLAND,GROUP_RIZIA
from Utils.Parser import parse,apply
from Utils.i18n import i18n

print(parse("./sample.json")[1].ewaldOpinion)
# apply("./sample.json")

dpg.create_context()
dpg.create_viewport(title='Suzerain Save Editor',width=700,height=800)

with dpg.window(tag="Edit"):
    with dpg.tab_bar():
        with dpg.tab(label="Sordland"):
            for k,v in GROUP_SORDLAND.items():
                with dpg.collapsing_header(label=k,default_open=True):
                    for i in v:
                        curr=getattr(store.sordland,i)
                        if type(curr)==int:
                            with dpg.group(horizontal=True):
                                dpg.add_text(i18n(i))
                                dpg.add_input_int(tag=i,label="",default_value=curr,width=250,step=5)
                        elif type(curr)==str:
                            with dpg.group(horizontal=True):
                                dpg.add_text(i18n(i))
                                dpg.add_input_text(tag=i,label="",default_value=curr)
                        elif type(curr)==bool:
                            with dpg.group(horizontal=True):
                                dpg.add_text(i18n(i))
                                dpg.add_checkbox(tag=i,label="",default_value=curr)
                        elif isinstance(curr,Enum):
                            with dpg.group(horizontal=True):
                                dpg.add_text(i18n(i))
                                dpg.add_combo(tag=i,items=[e.value for e in type(curr)],default_value=curr.value,width=250)
        with dpg.tab(label="Rizia"):
            for k,v in GROUP_RIZIA.items():
                with dpg.collapsing_header(label=k,default_open=True):
                    for i in v:
                        curr=getattr(store.rizia,i)
                        if type(curr)==int:
                            with dpg.group(horizontal=True):
                                dpg.add_text(i18n(i))
                                dpg.add_input_int(tag=i,label="",default_value=curr,width=250,step=5)
                        elif type(curr)==str:
                            with dpg.group(horizontal=True):
                                dpg.add_text(i18n(i))
                                dpg.add_input_text(tag=i,label="",default_value=curr)
                        elif type(curr)==bool:
                            with dpg.group(horizontal=True):
                                dpg.add_text(i18n(i))
                                dpg.add_checkbox(tag=i,label="",default_value=curr)
                        elif isinstance(curr,Enum):
                            with dpg.group(horizontal=True):
                                dpg.add_text(i18n(i))
                                dpg.add_combo(tag=i,items=[e.value for e in type(curr)],default_value=curr.value,width=250)
    dpg.add_button(label="Save",callback=lambda:print())
    
# dpg.bind_theme(theme)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Edit",True)
dpg.start_dearpygui()
dpg.destroy_context()