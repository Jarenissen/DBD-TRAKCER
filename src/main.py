from PyQt5 import QtWidgets
from qt_material import apply_stylesheet
from tracker.windows.main_window_wrapper import MainWindowWrapper
from tracker.util.database import Database

class LaunchException(Exception): pass

if __name__ == "__main__":
    import sys
    try:
        Database()
    except:
        raise LaunchException("Could not open database")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowWrapper()
    ui.setupUi(MainWindow)
    apply_stylesheet(app, theme="dark_teal.xml")
    MainWindow.show()
    sys.exit(app.exec_())