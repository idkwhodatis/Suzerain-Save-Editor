import dearpygui.dearpygui as dpg

from Utils.Init import init
from Windows.SelectWindow import selectWindow
from Windows.EditWindow import editWindow
from Utils.Store import store
from Utils.Parser import parse,apply
from Utils.i18n import i18n,I18N

print(parse("./sample.json")[1].ewaldOpinion)
apply("./sample.json")

def updateLocale(sender,app_data,user_data):
    store.locale=user_data[0]
    for item in dpg.get_all_items():
        i18nKey=dpg.get_item_user_data(item)
        if i18nKey in I18N[store.locale]:
            if dpg.get_item_type(item)=="mvAppItemType::mvText":
                dpg.set_value(item,i18n(i18nKey))
            else:
                dpg.configure_item(item,label=i18n(i18nKey))
        if dpg.get_item_alias(item) not in I18N["locales"].values():
            dpg.bind_item_font(item,user_data[1])


width,height=700,800

init()
dpg.create_context()

with dpg.font_registry():
    fontEN=dpg.add_font("./Fonts/NotoSans-Regular.ttf",18)
    with dpg.font("./Fonts/NotoSansSC-Regular.ttf",18) as fontZH:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
    dpg.bind_font(globals()["font"+store.locale.upper()])

hoverColor=tuple(60 for _ in range(3))
activeColor=tuple(70 for _ in range(3))
upperActiveColor=tuple(75 for _ in range(3))
bgColor=tuple(37 for _ in range(3))
upperBgColor=tuple(51 for _ in range(3))

with dpg.theme() as theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,1,category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_FrameBg,upperBgColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered,hoverColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive,activeColor,category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_Button,upperBgColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,hoverColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,activeColor,category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_Header,upperBgColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered,hoverColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive,activeColor,category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_Tab,(55,55,55),category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered,upperActiveColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive,upperActiveColor,category=dpg.mvThemeCat_Core)
        
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark,(255,255,255),category=dpg.mvThemeCat_Core)
        
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg,bgColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab,activeColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered,upperActiveColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive,upperActiveColor,category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_WindowBg,bgColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg,bgColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg,bgColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg,bgColor,category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg,(0,0,0),category=dpg.mvThemeCat_Core)
dpg.bind_theme(theme)

dpg.create_viewport(title='Suzerain Save Editor',width=width,height=height)
dpg.set_viewport_vsync(True)

with dpg.viewport_menu_bar():
    with dpg.menu(label=i18n("File"),user_data="File"):
        dpg.add_menu_item(label=i18n("Open"),user_data="Open")
        dpg.add_menu_item(label=i18n("Open Folder"),user_data="Open Folder")
        dpg.add_menu_item(tag="save",label=i18n("Save"),user_data="Save",enabled=False)
    with dpg.menu(label=i18n("Settings"),user_data="Settings"):
        dpg.add_checkbox(label=i18n("Auto Backup"),user_data="Auto Backup",callback=lambda sender,app_data,user_data:setattr(store,"autoBackup",app_data))
        with dpg.menu(label=i18n("Language"),user_data="Language"):
            for i in I18N["locales"]:
                locale=I18N["locales"][i]
                font=globals()["font"+locale.upper()]
                lang=dpg.add_menu_item(tag=locale,label=i,callback=updateLocale,user_data=(locale,font))
                dpg.bind_item_font(lang,font)
    dpg.add_menu_item(label=i18n("About"),user_data="About")

# editWindow(width,height)
selectWindow(width,height)

dpg.setup_dearpygui()

# dpg.show_item_registry()
# dpg.show_style_editor()

dpg.show_viewport()
# dpg.set_primary_window("Edit",True)
dpg.set_primary_window("Select",True)
dpg.start_dearpygui()

dpg.destroy_context()
