FIELD_MAP_SORDLAND={
    "governmentBudget":"BaseGame.GovernmentBudget",
    "personalWealth":"BaseGame.PersonalWealth",
    "economy":"BaseGame.Economy",
    "publicOpinion":"BaseGame.Public_Opinion",
    "bludishOpinion":"BaseGame.Bludish_Opinion",
    "countryUnrest":"BaseGame.Country_Unrest",
    "lucianOpinion":"BaseGame.Relations_Lucian_Opinion",
    "monicaOpinion":"BaseGame.Relations_Monica_Opinion",
    "francOpinion":"BaseGame.Relations_Franc_Opinion",
    "deanaLoved":"BaseGame.Relations_Deana_Loved",
    "deanaOpinion":"BaseGame.Relations_Deana_Opinion",
    "ewaldDiscontent":"BaseGame.Relations_Ewald_Discontent",
    "ewaldNeutral":"BaseGame.Relations_Ewald_Neutral",
    "ewaldFriendly":"BaseGame.Relations_Ewald_Friendly"
}

GROUP_SORDLAND={
    "Money":[
        "governmentBudget",
        "personalWealth",
    ],
    "Economy":[
        "economy"
    ],
    "Opinion":[
        "publicOpinion",
        "bludishOpinion",
        "countryUnrest",
        "lucianOpinion",
        "monicaOpinion",
        "francOpinion",
        "deanaLoved",
        "deanaOpinion",
        "ewaldOpinion"
    ]
}


FIELD_MAP_RIZIA={
    "resourcesBudget":"RiziaDLC.Resources_Budget",
    "resourcesAuthority":"RiziaDLC.Resources_Authority",
    "resourcesEnergy":"RiziaDLC.Resources_Energy"
}

GROUP_RIZIA={
    "Money":[
        "resourcesBudget",
        "resourcesAuthority",
        "resourcesEnergy"
    ]
}

STORY_PACK={
    "sordland":{
        "field_map":FIELD_MAP_SORDLAND,
        "group":GROUP_SORDLAND
    },
    "rizia":{
        "field_map":FIELD_MAP_RIZIA,
        "group":GROUP_RIZIA
    }
}

ABOUT={
    "Author":"idkwhodatis",
    "License":"MIT"
}