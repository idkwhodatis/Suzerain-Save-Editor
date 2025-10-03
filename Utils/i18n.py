from Utils.Store import store


def i18n(key):
    return I18N.get(store.locale,{}).get(key,"")


I18N={
    "locales":{
        "English":"en",
        "简体中文":"zh"
    },
    "en":{
        "File":"File",
        "Settings":"Settings",
        "About":"About",
        "Open Folder":"Open Folder",
        "Save":"Save",
        "Auto Backup":"Auto Backup",
        "Language":"Language",
        "Author":"Author: ",
        "License":"License: ",

        "Confirm":"Confirm",
        "SaveDir":"Choose Save File Directory",
        "Save Files":"Save Files",
        "Backup Files":"Backup Files",
        "Backup":"Backup",
        "Max Money":"Max Money",
        "Restore":"Restore",
        "Delete":"Delete",
        "Close":"Close",

        "Backed Up":"Backed Up",
        "Restored":"Restored",
        "Deleted":"Deleted",
        "Max Moneyed":"Money Maximized",

        "Money":"Money",
        "Economy":"Economy",
        "Opinion":"Opinion",
    
        "governmentBudget":"Government Budget",
        "personalWealth":"Personal Wealth",
        "economy":"Economy",
        "publicOpinion":"Public Opinion",
        "bludishOpinion":"Bludish Opinion",
        "countryUnrest":"Country Unrest",
        "lucianOpinion":"Lucian Opinion",
        "monicaOpinion":"Monica Opinion",
        "francOpinion":"Franc Opinion",
        "deanaLoved":"Deana Loved",
        "deanaOpinion":"Deana Opinion",
        "ewaldOpinion":"Ewald Opinion",

        "resourcesBudget":"Government Budget",
        "resourcesAuthority":"Government Authority",
        "resourcesEnergy":"Government Energy"
    },
    "zh":{
        "File":"文件",
        "Settings":"设置",
        "About":"关于",
        "Open Folder":"打开文件夹",
        "Save":"保存",
        "Auto Backup":"自动备份",
        "Language":"语言",
        "Author":"作者: ",
        "License":"开源证书: ",

        "Confirm":"确认",
        "SaveDir":"选择存档目录",
        "Save Files":"存档文件",
        "Backup Files":"备份文件",
        "Backup":"备份",
        "Max Money":"最大金钱",
        "Restore":"恢复",
        "Delete":"删除",
        "Close":"关闭",

        "Backed Up":"已备份",
        "Restored":"已恢复",
        "Deleted":"已删除",
        "Max Moneyed":"已最大金钱",

        "Money":"财政",
        "Economy":"经济",
        "Opinion":"民意/好感",

        "governmentBudget":"政府预算",
        "personalWealth":"私人财富",
        "economy":"经济",
        "publicOpinion":"民意",
        "bludishOpinion":"Bludish民意",
        "countryUnrest":"国家动乱",
        "lucianOpinion":"Lucian好感",
        "monicaOpinion":"Monica好感",
        "francOpinion":"Franc好感",
        "deanaLoved":"Deana喜爱",
        "deanaOpinion":"Deana好感",
        "ewaldOpinion":"Ewald好感",


        "resourcesBudget":"政府预算",
        "resourcesAuthority":"政府权威",
        "resourcesEnergy":"政府能源"
    }
}