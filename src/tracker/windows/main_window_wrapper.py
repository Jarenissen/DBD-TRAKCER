from generated.MainWindow import Ui_MainWindow
from tracker.windows.survivor_modal_wrapper import SurvivorModalWrapper
from tracker.windows.map_modal_wrapper import MapModalWrapper
from tracker.windows.killer_modal_wrapper import KillerModalWrapper
from tracker.util.game_entry import GameEntryManager, IncompleteEntry
from tracker.data.victory import Victory
from tracker.util.database import Database
from PyQt5 import QtCore, QtGui
from .dialog_manager import DialogManager
from tracker.data.pips import Pips
from enum import Enum
from generated.enums.maps import Map
from generated.enums.killers import Killer  
from generated.enums.survivors import Survivor
from tracker.util.pathing import asset_path

class NoVictorySelected(Exception): pass

class MainWindowWrapper(Ui_MainWindow):
    def update_selections(self):
        self.selectedMapLabel.setText(f"{GameEntryManager._entry.mapvariation.name}")
        self.selectedKillerLabel.setText(f"{GameEntryManager._entry.killer.name}")
        self.selectedSurviorLabel.setText(f"{GameEntryManager._entry.survivor.name}")
        def scale(pixmap):
            if not pixmap.isNull():
                return pixmap.scaled(self.selectedMapImgLabel.size(), QtCore.Qt.IgnoreAspectRatio)
            else:
                return pixmap
        self.selectedMapImgLabel.setPixmap(scale(QtGui.QPixmap(GameEntryManager._entry.mapvariation.get_img_path())))
        self.selectedKillerImgLabel.setPixmap(scale(QtGui.QPixmap(GameEntryManager._entry.killer.get_img_path())))
        self.selectedSurvivorImgLabel.setPixmap(scale(QtGui.QPixmap(GameEntryManager._entry.survivor.get_img_path())))

    def update_list_contents(self):
        self.gameHistoryList.clear()
        self.gameHistoryList.addItems(map(lambda x: " - ".join([y.name if isinstance(y, Enum) else y for y in x]), Database().get_all()))

    def get_victory_radio(self):
        if self.killerWonRadio.isChecked():
            return Victory.KillerWon
        elif self.hatchEscapeRadio.isChecked():
            return Victory.HatchEscape
        elif self.gateEscapeRadio.isChecked():
            return Victory.GateEscape
        else:
            return None
        
    def get_pip_radio(self):
        if self.pip0.isChecked():
            return Pips.pip0
        elif self.pip1.isChecked():
            return Pips.Pip1
        elif self.pip2.isChecked():
            return Pips.Pip2
        else:
            return None
        
   

    
    def save_callback(self):
        GameEntryManager.set_victory(self.get_victory_radio())
        GameEntryManager.set_pips(self.get_pip_radio())
        try:
            GameEntryManager.save()
            self.errorLabel.setStyleSheet("color: green")
            self.errorLabel.setText("Saved")
            self.update_list_contents()
        except IncompleteEntry:
            self.errorLabel.setStyleSheet("color: red")
            self.errorLabel.setText("Data Missing...")
    
    def clear_callback(self):
        self.errorLabel.setText("")
        self.victoryTypeButtonGroup.setExclusive(False)
        self.killerWonRadio.setChecked(False)
        self.hatchEscapeRadio.setChecked(False)
        self.gateEscapeRadio.setChecked(False)
        self.victoryTypeButtonGroup.setExclusive(True)
        GameEntryManager.clear()

    def setupUi(self, main_window):
        super().setupUi(main_window)
        self.update_selections()
        self.update_list_contents()
        self.MapFilter.addItem("All")
        self.KillerFilter.addItem("All")
        self.SurvivorFilter.addItem("All")
        self.MapFilter.addItems([x.name for x in Map if x.value != 0])
        self.KillerFilter.addItems([x.name for x in Killer if x.value != 0])
        self.SurvivorFilter.addItems([x.name for x in Survivor if x.value != 0])
        GameEntryManager.set_callback(self.update_selections)
        self.logoLabel.setPixmap(QtGui.QPixmap(asset_path("Logo.png")).scaled(self.logoLabel.size(), QtCore.Qt.IgnoreAspectRatio))
        # not random
        self.saveButton.clicked.connect(self.save_callback)
        self.clearButton.clicked.connect(self.clear_callback)
        self.saveButton.clicked.connect(self.clear_callback)
        self.selectSurvivorButton.clicked.connect(lambda _: DialogManager.open(SurvivorModalWrapper()))
        self.selectMapButton.clicked.connect(lambda _: DialogManager.open(MapModalWrapper()))
        self.selectKillerButton.clicked.connect(lambda _: DialogManager.open(KillerModalWrapper()))

        
        