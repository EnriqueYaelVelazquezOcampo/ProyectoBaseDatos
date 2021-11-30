import sys, res
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QWidget

class VentanaCrearEntidades(QMainWindow):

    def __init__(self, widget):
        super(VentanaCrearEntidades, self).__init__()
        loadUi("ventanaCrearEntidades.ui", self)

        self.widget = widget

        self.bandera1 = True
        self.bandera2 = True
        self.bandera3 = True

        self.etNombreTabla.setFocus()

        self.btnCrear.clicked.connect(lambda: self.crearItem())
        self.btnActualizar.clicked.connect(lambda: self.actualizarItem())
        self.btnEliminar.clicked.connect(lambda: self.eliminarItem())

        self.cbTipoDato.currentTextChanged.connect(lambda: self.cambioTextoComboBox())

        self.lwListaAtributos.itemClicked.connect(self.itemSeleccionado)

        self.cbLlavePrimaria.stateChanged.connect(lambda: self.cambioCBLlavePrimaria())
        self.cbPuedeNull.stateChanged.connect(lambda: self.cambioCBPuedeNull())
        self.cbLlaveForanea.stateChanged.connect(lambda: self.cambioCBLlaveForanea())

        self.btnAtras.clicked.connect(lambda: self.irAtras())
        self.btnCrearTabla.clicked.connect(lambda: self.crearTabla())

    def crearTabla(self):
        self.etNombreTabla.setText("")
        self.lwListaAtributos.clear()
        self.etNombreAtributo.setText("")
        self.cbTipoDato.setCurrentIndex(0)
        self.sbTamanio.setValue(0)
        self.cbLlavePrimaria.setChecked(False)
        self.cbPuedeNull.setChecked(False)
        self.cbLlaveForanea.setChecked(False)
    
    def itemSeleccionado(self):
        #print(self.lwListaAtributos.currentItem().text().split(" "))
        elemento = self.lwListaAtributos.currentItem().text().split(" ")
        diccionario = {"llave_primaria": elemento[0],
                        "nombre_atributo": elemento[1],
                        "llave_foranea": elemento[2],
                        "tipo_dato": elemento[4],
                        "es_nulo": elemento[5]}
        #print(diccionario)

        self.etNombreAtributo.setText(diccionario["nombre_atributo"])
        indice = 0
        if(diccionario["tipo_dato"]=="int"):
            indice = 1
            self.sbTamanio.setValue(0)
        elif(diccionario["tipo_dato"]=="float"):
            indice = 2
            self.sbTamanio.setValue(0)
        else:
            self.sbTamanio.setValue(int(diccionario["tipo_dato"][8:10]))
        self.cbTipoDato.setCurrentIndex(indice)

        if(diccionario["llave_primaria"] == "#"):
            self.cbLlavePrimaria.setChecked(True)
        else:
            self.cbLlavePrimaria.setChecked(False)


        if(diccionario["es_nulo"] == "nulo"):
            self.cbPuedeNull.setChecked(True)
        else:
            self.cbPuedeNull.setChecked(False)


        if(diccionario["llave_foranea"] == "FK"):
            self.cbLlaveForanea.setChecked(True)
        else:
            self.cbLlaveForanea.setChecked(False)

    def crearItem(self):
        nombreAtributo = self.etNombreAtributo.text()
        tipoAtributo = self.cbTipoDato.currentText()
        if(tipoAtributo == "varchar"):
            tamanio = self.sbTamanio.value()
            tipoAtributo = tipoAtributo+f"({tamanio})"
        else:
            tamanio = ""
        llavePrimaria = ""
        puedeNull = "no_nulo"
        llaveForanea = ""
        if(self.cbLlavePrimaria.checkState() == 2):
            llavePrimaria = "#"
        if(self.cbPuedeNull.checkState() == 2):
            puedeNull = "nulo"
        if(self.cbLlaveForanea.checkState() == 2):
            llaveForanea = "FK"

        texto = f'{llavePrimaria} {nombreAtributo} {llaveForanea} : {tipoAtributo} {puedeNull}'
        self.lwListaAtributos.addItem(texto)


        self.etNombreAtributo.setText("")
        self.cbTipoDato.setCurrentIndex(0)
        self.sbTamanio.setValue(0)
        self.cbLlavePrimaria.setChecked(False)
        self.cbPuedeNull.setChecked(False)
        self.cbLlaveForanea.setChecked(False)
        self.etNombreAtributo.setFocus()

    def actualizarItem(self):
        if(self.lwListaAtributos.count() > 0 and self.lwListaAtributos.currentRow() > -1):
            row = self.lwListaAtributos.currentRow()

            nombreAtributo = self.etNombreAtributo.text()
            tipoAtributo = self.cbTipoDato.currentText()
            if(tipoAtributo == "varchar"):
                tamanio = self.sbTamanio.value()
                tipoAtributo = tipoAtributo+f"({tamanio})"
            else:
                tamanio = ""
            llavePrimaria = ""
            puedeNull = "no_nulo"
            llaveForanea = ""
            if(self.cbLlavePrimaria.checkState() == 2):
                llavePrimaria = "#"
            if(self.cbPuedeNull.checkState() == 2):
                puedeNull = "nulo"
            if(self.cbLlaveForanea.checkState() == 2):
                llaveForanea = "FK"

            texto = f'{llavePrimaria} {nombreAtributo} {llaveForanea} : {tipoAtributo} {puedeNull}'

            self.lwListaAtributos.takeItem(row)
            self.lwListaAtributos.insertItem(row,QListWidgetItem(texto)) 

    def eliminarItem(self):
        self.lwListaAtributos.takeItem(self.lwListaAtributos.currentRow())

    def irAtras(self):
        self.widget.removeWidget(self)

    def cambioCBLlavePrimaria(self):
        if(self.bandera1):
            self.cbLlaveForanea.setEnabled(False)
            self.cbPuedeNull.setEnabled(False)
            self.bandera1 = False
        else:
            self.cbLlaveForanea.setEnabled(True)
            self.cbPuedeNull.setEnabled(True)
            self.bandera1 = True

    def cambioCBPuedeNull(self):
        if(self.bandera3):
            self.cbLlavePrimaria.setEnabled(False)
            self.bandera3 = False
        else:
            self.cbLlavePrimaria.setEnabled(True)
            self.bandera3 = True

    def cambioCBLlaveForanea(self):
        if(self.bandera2):
            self.cbLlavePrimaria.setEnabled(False)
            self.bandera2 = False
        else:
            self.cbLlavePrimaria.setEnabled(True)
            self.bandera2 = True

    def cambioTextoComboBox(self):
        if(self.cbTipoDato.currentText() == "varchar"):
            self.sbTamanio.setEnabled(True)
        else:
            self.sbTamanio.setEnabled(False)
            self.sbTamanio.setValue(0)


'''
aplicacion = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
v_crearEntidades = VentanaCrearEntidades(widget)
widget.addWidget(v_crearEntidades)
widget.setWindowTitle("Crear Entidades")
widget.resize(800,600)
widget.showMaximized()
widget.show()
sys.exit(aplicacion.exec_())
'''