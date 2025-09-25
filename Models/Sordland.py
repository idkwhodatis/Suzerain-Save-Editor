from dataclasses import dataclass
from enum import Enum


@dataclass
class Sordland:
    governmentBudget:int
    personalWealth:int
    economy:int
    publicOpinion:int
    bludishOpinion:int
    countryUnrest:int
    lucianOpinion:int
    monicaOpinion:int
    francOpinion:int
    deanaLoved:bool
    deanaOpinion:int
    ewaldDiscontent:bool
    ewaldNeutral:bool
    ewaldFriendly:bool

    @property
    def ewaldOpinion(self):
        if self.ewaldDiscontent:
            return EwaldOpinion.DISCONTENT
        elif self.ewaldNeutral:
            return EwaldOpinion.NEUTRAL
        elif self.ewaldFriendly:
            return EwaldOpinion.FRIENDLY
    @ewaldOpinion.setter
    def ewaldOpinion(self,opinion):
        self.ewaldDiscontent=self.ewaldNeutral=self.ewaldFriendly=False
        match opinion:
            case EwaldOpinion.DISCONTENT:
                self.ewaldDiscontent=True
            case EwaldOpinion.NEUTRAL:
                self.ewaldNeutral=True
            case EwaldOpinion.FRIENDLY:
                self.ewaldFriendly=True

class EwaldOpinion(Enum):
    DISCONTENT="discontent"
    NEUTRAL="neutral"
    FRIENDLY="friendly"
