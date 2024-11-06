from PyQt6.QtWidgets import QApplication, QMainWindow
from Ex133_134.Ex133.MainWindowExt import MainWindowExt
app=QApplication
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()