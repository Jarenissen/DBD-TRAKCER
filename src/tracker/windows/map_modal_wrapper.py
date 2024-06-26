from PyQt5 import QtGui, QtWidgets
from generated.MapModal import Ui_Dialog
from tracker.util.game_entry import GameEntryManager
from .dialog_manager import DialogManager
from generated.enums.realms import Realm
from generated.enums.maps import Map
from tracker.util.realm_map import maps_from_realm
from generated import MapModal






class NoMapSelected(Exception): pass

class MapModalWrapper(Ui_Dialog):
    def show(self):
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        
        
    def populate_realms(self):
        self.realms.addItems([m.name for m in Realm])
        
        self.realms.setStyleSheet("QComboBox{ color: rgb(0,170,255);} QListView{ color: rgb(0,255,255); }")

    def on_realm_change(self, value):
        self.maps.clear()
        self.maps.addItems([r.name for r in maps_from_realm(Realm[value])])
        

    def on_button_press(self):
        
        if len(self.maps.selectedItems()) > 0: GameEntryManager.set_mapvariation(Map[self.maps.selectedItems()[0].text()])
        
        
    def setupUi(self, window):
        func = window.accept
        def callback(*params):
            self.on_button_press()
            func(*params)
        window.accept = callback
        super().setupUi(window)
        self.populate_realms()
        self.realms.currentTextChanged.connect(self.on_realm_change)
        self.maps.itemSelectionChanged.connect(self.on_button_press)
        
        
        
        
        

        
        