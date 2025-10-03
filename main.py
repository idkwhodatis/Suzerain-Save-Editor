import dearpygui.dearpygui as dpg

from Utils.Init import init
from Windows.SelectWindow import selectWindow
from Windows.EditWindow import saveCallback
from Utils.Store import store
from Utils.Theme import theme,fonts
from Utils.i18n import i18n,I18N
from Utils.Consts import ABOUT


def updateLocale(sender,app_data,user_data):
    store.locale=user_data[0]
    dpg.bind_font(user_data[1])
    for item in dpg.get_all_items():
        i18nKey=dpg.get_item_user_data(item)
        if i18nKey in I18N[store.locale]:
            if dpg.get_item_type(item)=="mvAppItemType::mvText":
                dpg.set_value(item,i18n(i18nKey))
            else:
                dpg.configure_item(item,label=i18n(i18nKey))
        tag=dpg.get_item_alias(item)
        if tag not in I18N["locales"].values() and not tag.startswith("icon"):
            dpg.bind_item_font(item,user_data[1])

def popupCallback():
    dpg.configure_item("popupAbout",show=True)

width,height,footerOffset=700,800,140

init()
dpg.create_context()

theme()

dpg.create_viewport(title='Suzerain Save Editor',width=width,height=height)
dpg.set_viewport_vsync(True)

with dpg.viewport_menu_bar():
    with dpg.menu(label=i18n("File"),user_data="File"):
        dpg.add_menu_item(tag="Open Folder",label=i18n("Open Folder"),user_data="Open Folder",callback=lambda:dpg.show_item("dirDialog"))
        dpg.add_menu_item(tag="save",label=i18n("Save"),user_data="Save",enabled=False,callback=saveCallback)
    with dpg.menu(label=i18n("Settings"),user_data="Settings"):
        dpg.add_checkbox(label=i18n("Auto Backup"),user_data="Auto Backup",default_value=store.autoBackup,callback=lambda sender,app_data,user_data:setattr(store,"autoBackup",app_data))
        with dpg.menu(label=i18n("Language"),user_data="Language"):
            for i in I18N["locales"]:
                locale=I18N["locales"][i]
                font=fonts["font"+locale.upper()]
                lang=dpg.add_menu_item(tag=locale,label=i,callback=updateLocale,user_data=(locale,font))
                dpg.bind_item_font(lang,font)
    dpg.add_menu_item(label=i18n("About"),user_data="About",callback=popupCallback)

with dpg.window(show=False):
    dpg.add_button(tag="dummyAbout",show=False)
    with dpg.popup("dummyAbout",modal=True,tag="popupAbout"):
            for k,v in ABOUT.items():
                with dpg.group(horizontal=True):
                    dpg.add_text(i18n(k),user_data=k,tag=k)
                    dpg.add_text(v)
            dpg.add_button(label=i18n("Close"),user_data="Close",callback=lambda:dpg.configure_item("popupAbout",show=False))

selectWindow(width,height)

dpg.setup_dearpygui()

# dpg.show_item_registry()
# dpg.show_style_editor()

dpg.show_viewport()
dpg.set_primary_window("Select",True)
dpg.start_dearpygui()

dpg.destroy_context()
