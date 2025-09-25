from dataclasses import dataclass


@dataclass
class Sordland:
    governmentBudget:int
    personalWealth:int
    economy:int
    publicOpinion:int
    bludishOpinion:int

GROUP_SORDLAND={
    "Money":[
        "governmentBudget",
        "personalWealth",
    ],
    "Economy":[
        "economy"
    ],
    "Oponion":[
        "publicOpinion",
        "bludishOpinion"
    ]
}