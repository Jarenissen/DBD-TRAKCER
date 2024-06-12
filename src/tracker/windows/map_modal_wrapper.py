from PyQt5 import QtWidgets
from generated.MapModal import Ui_Dialog
from tracker.util.game_entry import GameEntryManager
from .dialog_manager import DialogManager
from generated.enums.realms import Realm
from generated.enums.maps import Map
from tracker.util.realm_map import maps_from_realm



class NoMapSelected(Exception): pass

class MapModalWrapper(Ui_Dialog):
    def show(self):
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        Dialog.show()

    

    

    def populate_realms(self):
        self.realms.addItems([m.name for m in Realm])

    def on_realm_change(self, value):
        self.maps.clear()
        self.maps.addItems([r.name for r in maps_from_realm(Realm[value])])


    def on_button_press(self):
        
        GameEntryManager.set_mapvariation(Map[self.maps.selectedItems()[0].text()])
        

        
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
        