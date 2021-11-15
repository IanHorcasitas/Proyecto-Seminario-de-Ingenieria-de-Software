from PySide2.QtWidgets import QApplication #Libreria de Qt
from mainwindow import MainWindow #Interfaz
import sys

app = QApplication()  #Se crea la aplicacion
window = MainWindow()  #Se crea la interfaz
window.show()  #Se muestra la interfaz
sys.exit(app.exec_())