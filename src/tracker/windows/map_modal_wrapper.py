
from PyQt5 import QtWidgets
from generated.MapModal import Ui_Dialog
from tracker.util.game_entry import GameEntryManager
from dialog_manager import DialogManager
from tracker.windows.mapvariationsThemcmillanestate_modal_wrapper import MapVariationMacMillanModalWrapper
from tracker.windows.mapvariationAutohavenWreckers import MapvariationAutohavenWreckers

class NoMapSelected(Exception): pass

class MapModalWrapper(Ui_Dialog):
    def show(self):
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        Dialog.show()

    

    

    def setupUi(self, window):
        func = window.accept
        def callback(*params):
            self.save_callback()
            func(*params)
        window.accept = callback
        super().setupUi(window)


        self.mapvariation.clicked.connect(lambda _: DialogManager.open(MapvariationAutohavenWreckers()))
        self.mapvariation.clicked.connect(lambda _: DialogManager.open(MapVariationMacMillanModalWrapper()))