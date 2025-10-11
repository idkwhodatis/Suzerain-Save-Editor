from dataclasses import dataclass
from enum import Enum


@dataclass
class Sordland:
    governmentBudget:int
    personalWealth:int

    _blackTuesday:bool
    _marketsCrash:bool

    economy:int
    tradeAmount:int
    economicReliance:int
    _superpowerTradeWar:bool
    _globalTradeWar:bool
    economyAgnland:int
    economyBergia:int
    economyGruni:int
    economyLorren:int
    investmentAgnland:bool
    investmentBergia:bool
    investmentGruni:bool
    investmentLorren:bool
    _agnlandMajorFishExport:bool
    _agnlandEconomicStabilisation:bool
    _agnlandLackInvestment:bool
    _bergiaMajorAgriculturalZone:bool
    _bergiaEconomicStabilisation:bool
    _bergiaEconomicDownturn:bool
    _gruniLightTowerRegion:bool
    _gruniLaggingBehind:bool
    _gruniMaintainingGrowth:bool
    _lorrenProductionAndTradeCenter:bool
    _lorrenEconomicStabilisation:bool
    _lorrenRustBelt:bool
    _highEmployment:bool
    _unemploymentCrisis:bool
    _increasedTrade:bool
    _decreasedTrade:bool
    _taxEfficientEconomy:bool
    _taxAvoidance:bool
    _taxEvasion:bool
    _improvedTransportation:bool
    _weakTransportation:bool
    _tourismBooming:bool
    _tourismAverage:bool
    _tourismDeclining:bool

    publicOpinion:int
    bludishOpinion:int
    countryUnrest:int
    lucianOpinion:int
    monicaOpinion:int
    francOpinion:int
    _deanaLoved:bool
    _deanaOpinion:bool
    _ewaldDiscontent:bool
    _ewaldNeutral:bool
    _ewaldFriendly:bool

    reformAssemblyVote:int
    reformAlbinConvinced:bool
    reformGloriaConvinced:bool
    reformCourtVote:int
    reformIsabelConvinced:bool
    reformHeronConvinced:bool
    _partyElectionWon:bool
    _partyElectionLost:bool
    _partyElectionNewParty:bool

    USPAgainstProposal:bool
    USPObstructionist:bool
    NFPDestroyed:bool
    PFJP_Destroyed:bool
    oldGuardContent:bool
    oldGuardDestroyed:bool
    oligarchsAlly:bool
    oligarchsContent:bool
    oligarchsDestroyed:bool
    oligarchsEnemy:bool
    oligarchsKorontiLeader:bool
    reformistsContent:bool

    amnestyForPoliticalPrisoners:bool
    deSollinisation:bool
    fairTradeCommission:bool
    genderEqualityInEducation:bool
    privatePrisons:bool
    ruralEducationInstitutes:bool
    capitalPunishment:bool
    gunRights:bool
    purgeGeneralStaff:bool
    relocationToRural:bool
    removeBankIndependence:bool
    removeReligiousSymbols:bool
    freeMedicine:bool
    lowerRetirementAge:bool
    _sordishRadioTVCouncil:bool
    _sordishRadioTVCouncilControlled:bool
    _sordishRadioTVCouncilIndependent:bool

    @property
    def blackTuesday(self):
        return self._blackTuesday or self._marketsCrash
    @blackTuesday.setter
    def blackTuesday(self,val):
        self._blackTuesday=self._marketsCrash=val

    @property
    def superpowerTradeWar(self):
        return self._superpowerTradeWar or self._globalTradeWar
    @superpowerTradeWar.setter
    def superpowerTradeWar(self,val):
        self._superpowerTradeWar=self._globalTradeWar=val

    @property
    def deanaLoved(self):
        return self._deanaLoved and self._deanaOpinion
    @deanaLoved.setter
    def deanaLoved(self,val):
        self._deanaLoved=self._deanaOpinion=val

    @property
    def employment(self):
        if self._highEmployment:
            return Employment.GOOD
        elif self._unemploymentCrisis:
            return Employment.BAD
    @employment.setter
    def employment(self,val):
        self._highEmployment=self._unemploymentCrisis=False
        if type(val)==str:
            val=Employment(val)
        match val:
            case Employment.GOOD:
                self._highEmployment=True
            case Employment.BAD:
                self._unemploymentCrisis=True

    @property
    def trade(self):
        if self._increasedTrade:
            return Trade.GOOD
        elif self._decreasedTrade:
            return Trade.BAD
    @trade.setter
    def trade(self,val):
        self._increasedTrade=self._decreasedTrade=False
        if type(val)==str:
            val=Trade(val)
        match val:
            case Trade.GOOD:
                self._increasedTrade=True
            case Trade.BAD:
                self._decreasedTrade=True

    @property
    def tax(self):
        if self._taxEfficientEconomy:
            return Tax.GOOD
        elif self._taxAvoidance:
            return Tax.MID
        elif self._taxEvasion:
            return Tax.BAD
    @tax.setter
    def tax(self,val):
        self._taxEfficientEconomy=self._taxAvoidance=self._taxEvasion=False
        if type(val)==str:
            val=Tax(val)
        match val:
            case Tax.GOOD:
                self._taxEfficientEconomy=True
            case Tax.MID:
                self._taxAvoidance=True
            case Tax.BAD:
                self._taxEvasion=True

    @property
    def transportation(self):
        if self._improvedTransportation:
            return Transportation.GOOD
        elif self._weakTransportation:
            return Transportation.BAD
    @transportation.setter
    def transportation(self,val):
        self._improvedTransportation=self._weakTransportation=False
        if type(val)==str:
            val=Transportation(val)
        match val:
            case Transportation.GOOD:
                self._improvedTransportation=True
            case Transportation.BAD:
                self._weakTransportation=True

    @property
    def tourism(self):
        if self._tourismBooming:
            return Tourism.GOOD
        elif self._tourismAverage:
            return Tourism.MID
        elif self._tourismDeclining:
            return Tourism.BAD
    @tourism.setter
    def tourism(self,val):
        self._tourismBooming=self._tourismAverage=self._tourismDeclining=False
        if type(val)==str:
            val=Tourism(val)
        match val:
            case Tourism.GOOD:
                self._tourismBooming=True
            case Tourism.MID:
                self._tourismAverage=True
            case Tourism.BAD:
                self._tourismDeclining=True

    @property
    def situationAgnland(self):
        if self._agnlandMajorFishExport:
            return SituationAgnland.GOOD
        elif self._agnlandEconomicStabilisation:
            return SituationAgnland.MID
        elif self._agnlandLackInvestment:
            return SituationAgnland.BAD
    @situationAgnland.setter
    def situationAgnland(self,val):
        self._agnlandMajorFishExport=self._agnlandEconomicStabilisation=self._agnlandLackInvestment=False
        if type(val)==str:
            val=SituationAgnland(val)
        match val:
            case SituationAgnland.GOOD:
                self._agnlandMajorFishExport=True
            case SituationAgnland.MID:
                self._agnlandEconomicStabilisation=True
            case SituationAgnland.BAD:
                self._agnlandLackInvestment=True

    @property
    def situationBergia(self):
        if self._bergiaMajorAgriculturalZone:
            return SituationBergia.GOOD
        elif self._bergiaEconomicStabilisation:
            return SituationBergia.MID
        elif self._bergiaEconomicDownturn:
            return SituationBergia.BAD
    @situationBergia.setter
    def situationBergia(self,val):
        self._bergiaMajorAgriculturalZone=self._bergiaEconomicStabilisation=self._bergiaEconomicDownturn=False
        if type(val)==str:
            val=SituationBergia(val)
        match val:
            case SituationBergia.GOOD:
                self._bergiaMajorAgriculturalZone=True
            case SituationBergia.MID:
                self._bergiaEconomicStabilisation=True
            case SituationBergia.BAD:
                self._bergiaEconomicDownturn=True

    @property
    def situationGruni(self):
        if self._gruniLightTowerRegion:
            return SituationGruni.GOOD
        elif self._gruniMaintainingGrowth:
            return SituationGruni.MID
        elif self._gruniLaggingBehind:
            return SituationGruni.BAD
    @situationGruni.setter
    def situationGruni(self,val):
        self._gruniLightTowerRegion=self._gruniMaintainingGrowth=self._gruniLaggingBehind=False
        if type(val)==str:
            val=SituationGruni(val)
        match val:
            case SituationGruni.GOOD:
                self._gruniLightTowerRegion=True
            case SituationGruni.MID:
                self._gruniMaintainingGrowth=True
            case SituationGruni.BAD:
                self._gruniLaggingBehind=True

    @property
    def situationLorren(self):
        if self._lorrenProductionAndTradeCenter:
            return SituationLorren.GOOD
        elif self._lorrenEconomicStabilisation:
            return SituationLorren.MID
        elif self._lorrenRustBelt:
            return SituationLorren.BAD
    @situationLorren.setter
    def situationLorren(self,val):
        self._lorrenProductionAndTradeCenter=self._lorrenEconomicStabilisation=self._lorrenRustBelt=False
        if type(val)==str:
            val=SituationLorren(val)
        match val:
            case SituationLorren.GOOD:
                self._lorrenProductionAndTradeCenter=True
            case SituationLorren.MID:
                self._lorrenEconomicStabilisation=True
            case SituationLorren.BAD:
                self._lorrenRustBelt=True

    @property
    def ewaldOpinion(self):
        if self._ewaldDiscontent:
            return EwaldOpinion.DISCONTENT
        elif self._ewaldNeutral:
            return EwaldOpinion.NEUTRAL
        elif self._ewaldFriendly:
            return EwaldOpinion.FRIENDLY
        else:
            return EwaldOpinion.NONE
    @ewaldOpinion.setter
    def ewaldOpinion(self,val):
        self._ewaldDiscontent=self._ewaldNeutral=self._ewaldFriendly=False
        if type(val)==str:
            val=EwaldOpinion(val)
        match val:
            case EwaldOpinion.DISCONTENT:
                self._ewaldDiscontent=True
            case EwaldOpinion.NEUTRAL:
                self._ewaldNeutral=True
            case EwaldOpinion.FRIENDLY:
                self._ewaldFriendly=True

    @property
    def partyElectionResult(self):
        if self._partyElectionWon:
            return PartyElectionResult.WON
        elif self._partyElectionLost:
            return PartyElectionResult.LOST
        elif self._partyElectionNewParty:
            return PartyElectionResult.NEWPARTY
        else:
            return PartyElectionResult.NONE
    @partyElectionResult.setter
    def partyElectionResult(self,val):
        self._partyElectionWon=self._partyElectionLost=self._partyElectionNewParty=False
        if type(val)==str:
            val=PartyElectionResult(val)
        match val:
            case PartyElectionResult.WON:
                self._partyElectionWon=True
            case PartyElectionResult.LOST:
                self._partyElectionLost=True
            case PartyElectionResult.NEWPARTY:
                self._partyElectionNewParty=True

    @property
    def sordishRadioTVCouncilStatus(self):
        if not self._sordishRadioTVCouncil:
            return SordishRadioTVCouncilStatus.NONE
        if self._sordishRadioTVCouncilControlled:
            return SordishRadioTVCouncilStatus.CONTROLLED
        elif self._sordishRadioTVCouncilIndependent:
            return SordishRadioTVCouncilStatus.INDEPENDENT
        else:
            return SordishRadioTVCouncilStatus.NONE
    @sordishRadioTVCouncilStatus.setter
    def sordishRadioTVCouncilStatus(self,val):
        self._sordishRadioTVCouncil=self._sordishRadioTVCouncilControlled=self._sordishRadioTVCouncilIndependent=False
        if type(val)==str:
            val=SordishRadioTVCouncilStatus(val)
        match val:
            case SordishRadioTVCouncilStatus.CONTROLLED:
                self._sordishRadioTVCouncil=self._sordishRadioTVCouncilControlled=True
            case SordishRadioTVCouncilStatus.INDEPENDENT:
                self._sordishRadioTVCouncil=self._sordishRadioTVCouncilIndependent=True


class Employment(Enum):
    GOOD="High Employment"
    BAD="Unemployment Crisis"

class Trade(Enum):
    GOOD="Increased Trade"
    BAD="Decreased Trade"

class Tax(Enum):
    GOOD="Tax Efficient"
    MID="Tax Avoidance"
    BAD="Tax Evasion"

class Transportation(Enum):
    GOOD="Weak Transportation"
    BAD="Improved Transportation"

class Tourism(Enum):
    GOOD="Tourism Declining"
    MID="Tourism Average"
    BAD="Tourism Booming"

class SituationAgnland(Enum):
    GOOD="Major Fish Export"
    MID="Economic Stabilisation"
    BAD="Lack Investment"

class SituationBergia(Enum):
    GOOD="Major Agricultural Zone"
    MID="Economic Stabilisation"
    BAD="Economic Downturn"

class SituationGruni(Enum):
    GOOD="Light Tower Region"
    MID="Maintaining Growth"
    BAD="Lagging Behind"

class SituationLorren(Enum):
    GOOD="Production and Trade Center"
    MID="Economic Stabilisation"
    BAD="Rust Belt"

class EwaldOpinion(Enum):
    DISCONTENT="Discontent"
    NEUTRAL="Neutral"
    FRIENDLY="Friendly"
    NONE="None"

class PartyElectionResult(Enum):
    WON="Won"
    LOST="Lost"
    NEWPARTY="New Party"
    NONE="None"

class SordishRadioTVCouncilStatus(Enum):
    CONTROLLED="Controlled"
    INDEPENDENT="Independent"
    NONE="None"