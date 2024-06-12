
from PyQt5 import QtWidgets
from generated.MapModal import Ui_Dialog
from tracker.util.game_entry import GameEntryManager
from .dialog_manager import DialogManager
from generated.enums.realms import Realm
from generated.enums.maps import Map


class NoMapSelected(Exception): pass

class MapModalWrapper(Ui_Dialog):
    def show(self):
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        Dialog.show()

    

    def get_map_radio(self):
        if self.azarov27srestingplacebutton.isChecked():
            return Map.Azarov27sRestingPlace
        elif self.badhampreschoolbutton.isChecked():
            return Map.BadhamPreschool
        elif self.bloodlodgebutton.isChecked():
            return Map.BloodLodge
        elif self.coaltowerbutton.isChecked():
            return Map.CoalTower
        elif self.deaddawgsaloonbutton.isChecked():
            return Map.DeadDawgSaloon
        elif self.disturbedwardbutton.isChecked():
            return Map.DisturbedWard
        elif self.eyrieofcrowsbutton.isChecked():
            return Map.EyrieofCrows
        elif self.familyresidencebutton.isChecked():
            return Map.FamilyResidence
        elif self.fathercampbell27schapelbutton.isChecked():
            return Map.FatherCampbell27sChapel
        elif self.forgottenruinsbutton.isChecked():
            return Map.ForgottenRuins
        elif self.fracturedcowshedbutton.isChecked():
            return Map.FracturedCowshed
        elif self.gardenofjoybutton.isChecked():
            return Map.GardenofJoy
        elif self.gasheavenbutton.isChecked():
            return Map.GasHeaven
        elif self.greenvillesquarebutton.isChecked():
            return Map.GreenvilleSquare
        elif self.grimpantrybutton.isChecked():
            return Map.GrimPantry
        elif self.groaningstorehousebutton.isChecked():
            return Map.GroaningStorehouse
        elif self.ironworksofmiserybutton.isChecked():
            return Map.IronworksofMisery
        elif self.lampkinlanebutton.isChecked():
            return Map.LampkinLane
        elif self.midwichelementaryschoolbutton.isChecked():
            return Map.MidwichElementarySchool
        elif self.mother27sdwellingbutton.isChecked():
            return Map.Mother27sDwelling
        elif self.mountormondresortbutton.isChecked():
            return Map.MountOrmondResort
        elif self.nostromowreckagebutton.isChecked():
            return Map.NostromoWreckage
        elif self.raccooncitypolicestationbutton.isChecked():
            return Map.RaccoonCityPoliceStation
        elif self.raccooncitypolicestationeastwingbutton.isChecked():
            return Map.RaccoonCityPoliceStationEastWing
        elif self.raccooncitypolicestationwestwingbutton.isChecked():
            return Map.RaccoonCityPoliceStationWestWing
        elif self.rancidabattoirbutton.isChecked():
            return Map.RancidAbattoir
        elif self.rottenfieldsbutton.isChecked():
            return Map.RottenFields
        elif self.sanctumofwrathbutton.isChecked():
            return Map.SanctumofWrath
        elif self.shelterwoodsbutton.isChecked():
            return Map.ShelterWoods
        elif self.suffocationpitbutton.isChecked():
            return Map.SuffocationPit
        elif self.thegamebutton.isChecked():
            return Map.TheGame
        elif self.thepalerosebutton.isChecked():
            return Map.ThePaleRose
        elif self.theshatteredsquarebutton.isChecked():
            return Map.TheShatteredSquare
        elif self.thetempleofpurgationbutton.isChecked():
            return Map.TheTempleofPurgation
        elif self.thethompsonhousebutton.isChecked():
            return Map.TheThompsonHouse
        elif self.theundergroundcomplexbutton.isChecked():
            return Map.TheUndergroundComplex
        elif self.tobalandingbutton.isChecked():
            return Map.TobaLanding
        elif self.tormentcreekbutton.isChecked():
            return Map.TormentCreek
        elif self.treatmenttheatrebutton.isChecked():
            return Map.TreatmentTheatre
        elif self.wreckers27yardbutton.isChecked():
            return Map.Wreckers27Yard
        elif self.wretchedshopbutton.isChecked():
            return Map.WretchedShop
        else:
            raise NoMapSelected

    def populate_realms(self):
        self.realms.addItems([m.name for m in Realm if m.value != 0])

    

    def setupUi(self, window):
        func = window.accept
        def callback(*params):
            self.save_callback()
            func(*params)
        window.accept = callback
        super().setupUi(window)
        self.populate_realms()

       