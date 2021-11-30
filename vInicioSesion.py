import sys
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
import segundaVentana

class VentanaInicio(QMainWindow):

    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi("ventanaIniciarSesion.ui", self)
        self.usuarios = []

        archivo = open('administradores.txt', 'r')
        registros = archivo.readlines()
        archivo.close()
        c = 0
        for i in registros:
            self.usuarios.append([])
            v_aux = i.split(',')
            self.usuarios[c].append(v_aux[0])
            self.usuarios[c].append(v_aux[1][0:v_aux[1].find('\n')])
            c+=1

        self.btnIniciarSesion.clicked.connect(lambda: self.iniciarSesion())
        self.etContrasenia.returnPressed.connect(lambda: self.iniciarSesion())

    def iniciarSesion(self):
        usuario = self.etUsuario.text()
        contrasenia = self.etContrasenia.text()
        #print(usuario, contrasenia)
        for i in range(len(self.usuarios)):
            if(usuario == self.usuarios[i][0]):
                if(contrasenia == self.usuarios[i][1]):
                    self.lbIndicador.setText("Usuario correcto")
                    self.iniciarSegundaVentana(self.usuarios[i][0])
                    break
            else:
                self.lbIndicador.setText("Usuario/Contraseña incorrectos")

    def iniciarSegundaVentana(self, usuario):
        v2 = segundaVentana.SegundaVentana(widget, usuario)
        widget.addWidget(v2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.etUsuario.setText("")
        self.etContrasenia.setText("")
        self.lbIndicador.setText("")

aplicacion = QApplication(sys.argv)
v_inicio = VentanaInicio()
widget = QtWidgets.QStackedWidget()
widget.addWidget(v_inicio)
widget.setWindowTitle("Iniciar Sesion")
widget.showMaximized()
widget.setWindowIcon(QIcon("Iconos\logo.png"))
widget.show()
sys.exit(aplicacion.exec_())