import sys, res
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
import crearEntidades

class SegundaVentana(QMainWindow):

    def __init__(self, widget, usuario=None):
        super(SegundaVentana, self).__init__()
        loadUi("segundaVentana.ui", self)
        self.btnCerrarSesion.clicked.connect(lambda: self.cerrarSesion())
        self.btnCrearEntidades.clicked.connect(lambda: self.crearEntidades())

        if(usuario[len(usuario)-1:len(usuario)] == "a"):
            self.lblMensaje.setText("Bienvenida "+usuario)
        else:
            self.lblMensaje.setText("Bienvenido "+usuario)

        self.widget = widget
        

    def cerrarSesion(self):
        self.widget.removeWidget(self)

    def crearEntidades(self):
        v_crearEntidades = crearEntidades.VentanaCrearEntidades(self.widget)
        self.widget.addWidget(v_crearEntidades)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
        v_crearEntidades.etNombreTabla.setFocus()

    def actualizarUsuario(self, usuario):
        pass




'''
aplicacion = QApplication(sys.argv)
v_segunda = SegundaVentana("Yael")
widget = QtWidgets.QStackedWidget()
widget.addWidget(v_segunda)
widget.setWindowTitle("Bienvenida")
widget.showMaximized()
widget.show()
sys.exit(aplicacion.exec_())

'''