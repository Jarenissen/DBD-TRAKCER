
from PyQt5 import QtWidgets
from generated.SurvivorModal import Ui_Dialog
from tracker.util.game_entry import GameEntryManager
from tracker.data.survivors import Survivor

class NoSurvivorSelected(Exception): pass

class SurvivorModalWrapper(Ui_Dialog):
    def show(self):
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        Dialog.show()

    def get_survivor_radio(self):
        if self.dwightRadio.isChecked():
            return Survivor.DwightFairfield
        elif self.megRadio.isChecked():
            return Survivor.MegThomas
        elif self.acebutton.isChecked():
            return Survivor.Ace
        elif self.adabutton.isChecked():
            return Survivor.Ada
        elif self.adambutton.isChecked():
            return Survivor.Adam
        elif self.alanbutton.isChecked():
            return Survivor.Alan
        elif self.ashbutton.isChecked():
            return Survivor.Ash
        elif self.billbutton.isChecked():
            return Survivor.Bill
        elif self.cherylbutton.isChecked():
            return Survivor.Cheryl
        elif self.claudettebutton.isChecked():
            return Survivor.Claudette
        elif self.davidbutton.isChecked():
            return Survivor.David
        elif self.davidtappbutton.isChecked():
            return Survivor.DavidTapp
        elif self.ellenbutton.isChecked():
            return Survivor.Ellen
        elif self.elodiebutton.isChecked():
            return Survivor.Elodie
        elif self.felixbutton.isChecked():
            return Survivor.Felix
        elif self.fengbutton.isChecked():
            return Survivor.Feng
        elif self.gabrielbutton.isChecked():
            return Survivor.Gabriel
        elif self.haddiebutton.isChecked():
            return Survivor.Haddie
        elif self.jakebutton.isChecked():
            return Survivor.Jake
        elif self.janebutton.isChecked():
            return Survivor.Jane
        elif self.jeffbutton.isChecked():
            return Survivor.Jeff
        elif self.jillbutton.isChecked():
            return Survivor.Jill
        elif self.jonahbutton.isChecked():
            return Survivor.Jonah
        elif self.katebutton.isChecked():
            return Survivor.Kate
        elif self.lauriebutton.isChecked():
            return Survivor.laurie
        elif self.leonbutton.isChecked():
            return Survivor.Leon
        elif self.mikaelabutton.isChecked():
            return Survivor.Mikaela
        elif self.nancybutton.isChecked():
            return Survivor.Nancy
        elif self.neabutton.isChecked():
            return Survivor.Nea
        elif self.nicolasbutton.isChecked():
            return Survivor.Nicolas
        elif self.quentinbutton.isChecked():
            return Survivor.Quentin
        elif self.rebeccabutton.isChecked():
            return Survivor.Rebecca
        elif self.renatobutton.isChecked():
            return Survivor.Renato
        elif self.sablebutton.isChecked():
            return Survivor.Sable
        elif self.stevebutton.isChecked():
            return Survivor.Steve
        elif self.thalitabutton.isChecked():
            return Survivor.Thalita
        elif self.aestributton.isChecked():
            return Survivor.Troupe
        elif self.baermarbutton.isChecked():
            return Survivor.Troupe
        elif self.vittoriobutton.isChecked():
            return Survivor.Vittorio
        elif self.yoichibutton.isChecked():
            return Survivor.Yoichi
        elif self.yuibutton.isChecked():
            return Survivor.Yui
        elif self.yunbutton.isChecked():
            return Survivor.Yun
        elif self.zarinabutton.isChecked():
            return Survivor.Zarina
        





        else:
            raise NoSurvivorSelected

    def save_callback(self):
        var = self.get_survivor_radio()
        GameEntryManager.set_survivor(var)

    def setupUi(self, window):
        func = window.accept
        def callback(*params):
            self.save_callback()
            func(*params)
        window.accept = callback
        super().setupUi(window)