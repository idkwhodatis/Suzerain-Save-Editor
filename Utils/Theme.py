import dearpygui.dearpygui as dpg

from Utils.Store import store


fonts={}

def theme():
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
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg,bgColor,category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive,upperBgColor,category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg,(0,0,0),category=dpg.mvThemeCat_Core)
    dpg.bind_theme(theme)

    with dpg.font_registry():
        with dpg.font("./Fonts/FontAwesome-Regular.otf",18) as fontICON:
            dpg.add_font_chars([0xF07C])
        fontEN=dpg.add_font("./Fonts/NotoSans-Regular.ttf",18)
        with dpg.font("./Fonts/NotoSansSC-Regular.ttf",18) as fontZH:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)

        fonts["fontICON"]=fontICON
        fonts["fontEN"]=fontEN
        fonts["fontZH"]=fontZH

        dpg.bind_font(fonts["font"+store.locale.upper()])