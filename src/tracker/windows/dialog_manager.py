from PyQt5 import QtWidgets

class DialogManager:
    dialog = None

    def open(ui):
        DialogManager.dialog = QtWidgets.QDialog()
        ui.setupUi(DialogManager.dialog)
        DialogManager.dialog.show()