from PyQt5 import QtWidgets
from generated.MapVariations import Ui_Mapvariations
from tracker.util.game_entry import GameEntryManager
from tracker.data.maps import Map



class NoMapSelected(Exception): pass

class MapVariationMacMillanModalWrapper(Ui_Mapvariations):
    def show(self):
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        Dialog.show()



    def get_map_radio(self):
        if self.greenville.isChecked():
            return Map.GreenvilleSquare
        else:
            raise NoMapSelected



    def save_callback(self):
        var = self.get_map_radio()
        GameEntryManager.set_mapvariation(var)
    


    def setupUi(self, window):
        func = window.accept
        def callback(*params):
            self.save_callback()
            func(*params)
        window.accept = callback
        super().setupUi(window)