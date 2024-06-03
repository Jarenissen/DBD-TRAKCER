
from PyQt5 import QtWidgets
from generated.KillerModal import Ui_Dialog
from tracker.util.game_entry import GameEntryManager
from tracker.data.killers import Killer

class NoKillerSelected(Exception): pass

class KillerModalWrapper(Ui_Dialog):
    def show(self):
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        Dialog.show()

    def get_killer_radio(self):
        if self.michaelbutton.isChecked():
            return Killer.MichaelMyers
        elif self.thetrapperbutton.isChecked():
            return  Killer.TheTrapper
        elif self.twinsbutton.isChecked():
            return  Killer.TheTwins
        elif self.wraithbutton.isChecked():
            return  Killer.TheWraith
        elif self.hillbillybutton.isChecked():
            return  Killer.Hillbilly
        elif self.nursebutton.isChecked():
            return  Killer.TheNurse
        elif self.michaelbutton.isChecked():
            return  Killer.TheShape
        elif self.hagbutton.isChecked():
            return  Killer.TheHag
        elif self.doctorbutton.isChecked():
            return  Killer.TheDoctor
        elif self.huntressbutton.isChecked():
            return  Killer.Huntress
        elif self.cannibalbutton.isChecked():
            return  Killer.Cannibal
        elif self.nightmarebutton.isChecked():
            return  Killer.TheNightmare
        elif self.pigbutton.isChecked():
            return  Killer.ThePig
        elif self.clownbutton.isChecked():
            return  Killer.Clown
        elif self.spiritbutton.isChecked():
            return  Killer.Spirit
        elif self.legionbutton.isChecked():
            return  Killer.Legion
        elif self.plaguebutton.isChecked():
            return  Killer.ThePlague
        elif self.ghostbutton.isChecked():
            return  Killer.GhostFace
        elif self.demogorgonbutton.isChecked():
            return  Killer.Demogorgon
        elif self.onibutton.isChecked():
            return  Killer.TheOni
        elif self.deathslingerbutton.isChecked():
            return  Killer.DeathSlinger
        elif self.executionerbutton.isChecked():
            return  Killer.Executioner
        elif self.blightbutton.isChecked():
            return  Killer.TheBlight
        elif self.tricksterbutton.isChecked():
            return  Killer.Trickster
        elif self.nemesisbutton.isChecked():
            return  Killer.Nemesis
        elif self.cenobitebutton.isChecked():
            return  Killer.Cenobite
        elif self.artistbutton.isChecked():
            return  Killer.Artist
        elif self.onryobutton.isChecked():
            return  Killer.TheOnryo
        elif self.dredgebutton.isChecked():
            return  Killer.TheDredge
        elif self.mastermindbutton.isChecked():
            return  Killer.TheMastermind
        elif self.knightbutton.isChecked():
            return  Killer.TheKnight
        elif self.merchantbutton.isChecked():
            return  Killer.SkullMerchant
        elif self.singularitybutton.isChecked():
            return  Killer.TheSingularity
        elif self.xenomorphbutton.isChecked():
            return  Killer.TheXenomorph
        elif self.goodbutton.isChecked():
            return  Killer.TheGoodguy
        elif self.unknownbutton.isChecked():
            return  Killer.TheUnknown
        elif self.vecnabutton.isChecked():
            return  Killer.TheLich
        
        else:
        
            raise NoKillerSelected

    def save_callback(self):
        var = self.get_killer_radio()
        GameEntryManager.set_killer(var)

    def setupUi(self, window):
        func = window.accept
        def callback(*params):
            self.save_callback()
            func(*params)
        window.accept = callback
        super().setupUi(window)