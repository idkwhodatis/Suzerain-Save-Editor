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
    reformAllianceNFP:bool
    reformAlliancePFJP:bool
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

    highwayProject:bool
    railwayProject:bool
    industrialExpansionAgricultural:bool
    industrialExpansionAutomotive:bool
    industrialExpansionElectronics:bool
    industrialExpansionMilitary:bool
    industrialZone:bool
    airportProject:bool
    agriculturalZone:bool
    portProject:bool
    
    _agnoliaTradeDeal:bool
    _agnoliaTrade:bool
    _agnoliaAlliance:bool
    _policyAgnoliaAlliance:bool
    _wehlenTradeDeal:bool
    _wehlenTrade:bool
    _wehlenDefendBorder:bool
    _wehlenJointOperation:bool
    wehlenJoinedWar:bool
    lespiaTradeDeal:bool
    _lespiaAlliance:bool
    _policyLespiaAlliance:bool
    valgslandTradeDeal:bool
    _valgslandAlliance:bool
    _policyValgslandAlliance:bool
    _ATO:bool
    _ATOArea:bool
    _CSP:bool
    _CSPArea:bool

    _courtBacklog:bool
    _efficientJusticeSystem:bool
    _limitedWomenRights:bool
    _averageWomenRights:bool
    _excellentWomenRights:bool
    _corruption:bool
    _corruptionTackled:bool
    _organisedCrime:bool
    _organisedCrimeContained:bool

    _modernisedArmy:bool
    _modernisationArmy:bool
    _expandedArmy:bool
    _expansionArmy:bool
    _modernisedNavy:bool
    _modernisationNavy:bool
    _expandedNavy:bool
    _expansionNavy:bool
    _modernisedAirForce:bool
    _modernisationAirForce:bool
    _expandedAirForce:bool
    _expansionAirForce:bool

    FPnTMentionedKA74:bool
    FPnTMentionedNukes:bool
    televisionInterviewInternationalFavor:int
    FPnTRumburgIsolated:bool
    SnOPhase1Success:bool
    SnOPhase2Success:bool
    rumburgWarPerformance:int
    _vesordRumburgNavyInferior:bool
    _vesordRumburgNavySuperior:bool
    _SnORumburgWarLost:bool
    _SnORumburgWarWin:bool


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
    def agnoliaTradeDeal(self):
        return self._agnoliaTradeDeal and self._agnoliaTrade
    @agnoliaTradeDeal.setter
    def agnoliaTradeDeal(self,val):
        self._agnoliaTradeDeal=self._agnoliaTrade=val

    @property
    def agnoliaAlliance(self):
        return self._agnoliaAlliance and self._policyAgnoliaAlliance
    @agnoliaAlliance.setter
    def agnoliaAlliance(self,val):
        self._agnoliaAlliance=self._policyAgnoliaAlliance=val

    @property
    def wehlenTradeDeal(self):
        return self._wehlenTradeDeal and self._wehlenTrade
    @wehlenTradeDeal.setter
    def wehlenTradeDeal(self,val):
        self._wehlenTradeDeal=self._wehlenTrade=val

    @property
    def wehlenAlliance(self):
        return self._wehlenAlliance and self._policywehlenAlliance
    @wehlenAlliance.setter
    def wehlenAlliance(self,val):
        self._wehlenAlliance=self._policywehlenAlliance=val

    @property
    def lespiaAlliance(self):
        return self._lespiaAlliance and self._policyLespiaAlliance
    @lespiaAlliance.setter
    def lespiaAlliance(self,val):
        self._lespiaAlliance=self._policyLespiaAlliance=val

    @property
    def valgslandAlliance(self):
        return self._valgslandAlliance and self._policyValgslandAlliance
    @valgslandAlliance.setter
    def valgslandAlliance(self,val):
        self._valgslandAlliance=self._policyValgslandAlliance=val

    @property
    def ATO(self):
        return self._ATO and self._ATOArea
    @ATO.setter
    def ATO(self,val):
        self._ATO=self._ATOArea=val

    @property
    def CSP(self):
        return self._CSP and self._CSPArea
    @CSP.setter
    def CSP(self,val):
        self._CSP=self._CSPArea=val

    @property
    def modernisedArmy(self):
        return self._modernisedArmy and self._modernisationArmy
    @modernisedArmy.setter
    def modernisedArmy(self,val):
        self._modernisedArmy=self._modernisationArmy=val

    @property
    def expandedArmy(self):
        return self._expandedArmy and self._expansionArmy
    @expandedArmy.setter
    def expandedArmy(self,val):
        self._expandedArmy=self._expansionArmy=val

    @property
    def modernisedNavy(self):
        return self._modernisedNavy and self._modernisationNavy
    @modernisedNavy.setter
    def modernisedNavy(self,val):
        self._modernisedNavy=self._modernisationNavy=val

    @property
    def expandedNavy(self):
        return self._expandedNavy and self._expansionNavy
    @expandedNavy.setter
    def expandedNavy(self,val):
        self._expandedNavy=self._expansionNavy=val

    @property
    def modernisedAirForce(self):
        return self._modernisedAirForce and self._modernisationAirForce
    @modernisedAirForce.setter
    def modernisedAirForce(self,val):
        self._modernisedAirForce=self._modernisationAirForce=val

    @property
    def expandedAirForce(self):
        return self._expandedAirForce and self._expansionAirForce
    @expandedAirForce.setter
    def expandedAirForce(self,val):
        self._expandedAirForce=self._expansionAirForce=val

    @property
    def rumburgWarWin(self):
        return self._SnORumburgWarWin and not self._SnORumburgWarLost
    @rumburgWarWin.setter
    def rumburgWarWin(self,val):
        self._SnORumburgWarWin=val
        self._SnORumburgWarLost=not val


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

    @property
    def operationBearTrap(self):
        if self._wehlenDefendBorder:
            return OperationBearTrap.MID
        elif self._wehlenJointOperation:
            return OperationBearTrap.HIGH
        else:
            return OperationBearTrap.NONE
    @operationBearTrap.setter
    def operationBearTrap(self,val):
        self._wehlenDefendBorder=self._wehlenJointOperation=False
        if type(val)==str:
            val=OperationBearTrap(val)
        match val:
            case OperationBearTrap.MID:
                self._wehlenDefendBorder=True
            case OperationBearTrap.HIGH:
                self._wehlenJointOperation=True

    @property
    def courtStatus(self):
        if self._courtBacklog:
            return CourtStatus.BAD
        elif self._efficientJusticeSystem:
            return CourtStatus.GOOD
    @courtStatus.setter
    def courtStatus(self,val):
        self._courtBacklog=self._efficientJusticeSystem=False
        if type(val)==str:
            val=CourtStatus(val)
        match val:
            case CourtStatus.BAD:
                self._courtBacklog=True
            case CourtStatus.GOOD:
                self._efficientJusticeSystem=True

    @property
    def womenRights(self):
        if self._limitedWomenRights:
            return WomenRights.BAD
        elif self._averageWomenRights:
            return WomenRights.MID
        elif self._excellentWomenRights:
            return WomenRights.GOOD
    @womenRights.setter
    def womenRights(self,val):
        self._limitedWomenRights=self._averageWomenRights=self._excellentWomenRights=False
        if type(val)==str:
            val=WomenRights(val)
        match val:
            case WomenRights.BAD:
                self._limitedWomenRights=True
            case WomenRights.MID:
                self._averageWomenRights=True
            case WomenRights.GOOD:
                self._excellentWomenRights=True

    @property
    def corruption(self):
        if self._corruption:
            return Corruption.BAD
        elif self._corruptionTackled:
            return Corruption.GOOD
    @corruption.setter
    def corruption(self,val):
        self._corruption=self._corruptionTackled=False
        if type(val)==str:
            val=Corruption(val)
        match val:
            case Corruption.BAD:
                self._corruption=True
            case Corruption.GOOD:
                self._corruptionTackled=True

    @property
    def crime(self):
        if self._organisedCrime:
            return Crime.BAD
        elif self._organisedCrimeContained:
            return Crime.GOOD
    @crime.setter
    def crime(self,val):
        self._organisedCrime=self._organisedCrimeContained=False
        if type(val)==str:
            val=Crime(val)
        match val:
            case Crime.BAD:
                self._organisedCrime=True
            case Crime.GOOD:
                self._organisedCrimeContained=True

    @property
    def vesordRumbergNavy(self):
        if self._vesordRumburgNavyInferior:
            return VesordRumbergNavy.BAD
        elif self._vesordRumburgNavySuperior:
            return VesordRumbergNavy.GOOD
    @vesordRumbergNavy.setter
    def vesordRumbergNavy(self,val):
        self._vesordRumburgNavyInferior=self._vesordRumburgNavySuperior=False
        if type(val)==str:
            val=VesordRumbergNavy(val)
        match val:
            case VesordRumbergNavy.BAD:
                self._vesordRumburgNavyInferior=True
            case VesordRumbergNavy.GOOD:
                self._vesordRumburgNavySuperior=True

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

class OperationBearTrap(Enum):
    MID="Defend Border"
    HIGH="Joint Operation"
    NONE="None"

class CourtStatus(Enum):
    BAD="Court Backlog"
    GOOD="Efficient Justice System"

class WomenRights(Enum):
    BAD="Limited Women Rights"
    MID="Average Women Rights"
    GOOD="Excellent Women Rights"

class Corruption(Enum):
    BAD="Corruption"
    GOOD="Corruption Tackled"

class Crime(Enum):
    BAD="Organised Crime"
    GOOD="Organised Crime Contained"

class VesordRumbergNavy(Enum):
    BAD="Inferior"
    GOOD="Superior"