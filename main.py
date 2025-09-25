import dearpygui.dearpygui as dpg

from Utils.Store import store
from Utils.Parser import parse,apply

# print(parse("./sample.json"))
parse("./sample.json")
print(store["variables"]["BaseGameSupport.CollectionItem_WineBottle_Date"])
apply()

dpg.create_context()
dpg.create_viewport(title='Suzerain Save Editor',width=1200,height=800)

with dpg.window(tag="Main Window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Main Window",True)
dpg.start_dearpygui()
dpg.destroy_context()