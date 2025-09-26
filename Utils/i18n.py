from Utils.Store import store

def i18n(key):
    return I18N[store.locale][key]


I18N={
    "locales":{
        "English":"en",
        "简体中文":"zh"
    },
    "en":{
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
        "Money":"财政",
        "Economy":"经济",
        "Opinion":"民意/好感",

        "governmentBudget":"政府预算",
        "personalWealth":"私人财富",
        "economy":"经济",
        "publicOpinion":"民意",
        "bludishOpinion":"布尔德民意",
        "countryUnrest":"国家动乱",
        "lucianOpinion":"卢锡安好感",
        "monicaOpinion":"莫妮卡好感",
        "francOpinion":"弗兰克好感",
        "deanaLoved":"迪安娜喜爱",
        "deanaOpinion":"迪安娜好感",
        "ewaldOpinion":"埃瓦尔德好感",


        "resourcesBudget":"政府预算",
        "resourcesAuthority":"政府权威",
        "resourcesEnergy":"政府能源"
    }
}