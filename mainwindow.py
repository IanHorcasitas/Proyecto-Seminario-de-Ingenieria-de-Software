from PySide2.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem #Elementos de Qt
from ui_mainwindow import Ui_MainWindow #Interfaz
from PySide2.QtCore import Slot #Para conectar los botones
from datetime import date #Para conseguir la fecha


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Elementos para probar el programa
        self.producto = [0, 10.50, 8.30, 6.50, 12.50, 10.00, 11.00, 13.50]
        self.id = 1
        self.total = 0.00


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  #Interfaz
        #Conexion de los botones
        self.ui.agregar_registro_pushButton.clicked.connect(self.click_agregar_registro)
        self.ui.buscar_pushButton.clicked.connect(self.click_buscar)
        self.ui.eliminar_pushButton.clicked.connect(self.click_eliminar)
        self.ui.cambiar_precio_pushButton.clicked.connect(self.click_cambiar_precio)
        self.ui.mostrar_precio_pushButton.clicked.connect(self.click_mostrar_precio)

    @Slot() #Para conectar los botones
    def click_agregar_registro(self): #Para agregar registros
        #Se reciben los datos
        polloProduc = self.ui.pollo_pro_spinBox.value()
        polloSobr = self.ui.pollo_sob_spinBox.value()
        tacoProduc = self.ui.taco_pro_spinBox.value()
        tacoSobr = self.ui.taco_sob_spinBox.value()
        pescuezoProduc = self.ui.pescuezo_pro_spinBox.value()
        pescuezoSobr = self.ui.pescuezo_sob_spinBox.value()
        papaProduc = self.ui.papa_pro_spinBox.value()
        papaSobr = self.ui.papa_sob_spinBox.value()
        moleProduc = self.ui.mole_pro_spinBox.value()
        moleSobr = self.ui.mole_sob_spinBox.value()
        ensaladaProduc = self.ui.ensalada_pro_spinBox.value()
        ensaladaSobr = self.ui.ensalada_sob_spinBox.value()
        chamorroProduc = self.ui.chamorro_pro_spinBox.value()
        chamorroSobr = self.ui.chamorro_sob_spinBox.value()
        if self.ui.agregar_fecha_checkBox.isChecked(): #Se revisa si se quiere usar la fecha indicada
            fecha = self.ui.agregar_dateEdit.date()
        else:
            fecha = date.today()     #Se usa la fecha actual
        if fecha != fecha:  #Para probar el programa, ignorar
            pass
        #if fecha in self.registros:  #Mandar mensaje si la fecha ya fue registrada
        #    QMessageBox.warning(
        #        self,
        #        "Atencion",
        #        f'Fecha ya registrada con anterioridad'
        #    )
        else:  #En caso que no este registrado el dia
            polloVend = polloProduc - polloSobr #Se calcula la cantidad total de elementos vendidos
            valor1= self.producto[1]*polloVend  #Se calcula el valor total de lo vendido
            print(fecha,self.id,1,polloProduc,polloVend,polloSobr,valor1) #Se imprime provisionalmente en pantalla los datos
            self.id += 1 #El id aumenta solo para probar el programa

            tacoVend = tacoProduc - tacoSobr
            valor2 = self.producto[2] * tacoVend
            print(fecha,self.id,2,tacoProduc,tacoVend,tacoSobr,valor2)
            self.id += 1

            pescuezoVend = pescuezoProduc - pescuezoSobr
            valor3 = self.producto[3] * pescuezoVend
            print(fecha,self.id,3,pescuezoProduc,pescuezoVend,pescuezoSobr,valor3)
            self.id += 1

            papaVend = papaProduc - papaSobr
            valor4 = self.producto[4] * papaVend
            print(fecha,self.id,4,papaProduc,papaVend,papaSobr,valor4)
            self.id += 1

            moleVend = moleProduc - moleSobr
            valor5 = self.producto[5] * moleVend
            print(fecha,self.id,5,moleProduc,moleVend,moleSobr,valor5)
            self.id += 1

            ensaladaVend = ensaladaProduc - ensaladaSobr
            valor6 = self.producto[6] * ensaladaVend
            print(fecha,self.id,6,ensaladaProduc,ensaladaVend,ensaladaSobr,valor6)
            self.id += 1

            chamorroVend = chamorroProduc - chamorroSobr
            valor7 = self.producto[7] * chamorroVend
            print(fecha,self.id,7,chamorroProduc,chamorroVend,chamorroSobr,valor7)
            self.id += 1

            self.total = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7 #Se calcula el total de los registros

            self.mostrarRegistro(fecha, 1) #Se muestra el registro en pantalla

    @Slot()
    def click_buscar(self): #Para buscar registros de una fecha
        self.ui.buscar_tableWidget.clear() #Se limpia la pantalla
        fecha = self.ui.agregar_dateEdit.date() #Se toma la fecha indicada
        encontrado = False #Para verificar si fue encontrado
        #if fecha in self.registros:
        #    encontrado = True
        #    self.mostrarRegistro(fecha, 2) #Si fue encontrado, mostrarlo
        self.mostrarRegistro(fecha, 2) #Se muestra el registro, funcion para probar el programa
        #if not encontrado: #Si no se encuentra se manda mensaje de advertencia
        #    QMessageBox.warning(
        #        self,
        #        "Atencion",
        #        f'Los registros con fecha "{fecha}" no fueron encontrados'
        #    )

    def mostrarRegistro(self, fecha, tabla): #Para mostrar los registros de agregar y buscar
        headers = ["Fecha", "Id", "Producto", "Producido", "Vendido", "Sobrante", "Valor"] #Encabezados de la tabla
        row = 0 #Fila de la tabla
        id =1 #Id hardcodeado
        i = 0 #Contador para mostrar los registros en la tabla, para probar el programa
        if tabla ==1: #Si proviene de la funcion agregar
            self.ui.agregar_tableWidget.clear() #Se limpia la tabla de agregar
            self.ui.agregar_plainTextEdit.clear() #Se limpia el texto del valor total de agregar
        elif tabla==2: #Si proviene de la funcion buscar
            self.ui.buscar_tableWidget.clear() #Se limpia la tabla de buscar
            self.ui.buscar_plainTextEdit.clear() #Se limpia el texto del valor total de buscar

        while i < 7: #Ciclo para mostrar los registros
            #Datos hardcodeados para probar el programa
            fecha_widget = QTableWidgetItem("2021-11-14") #Los elementos se convierten en elementos de tabla
            id_widget = QTableWidgetItem(str(id))
            producto_widget = QTableWidgetItem("Agua")
            producido_widget = QTableWidgetItem(str(10))
            vendido_widget = QTableWidgetItem(str(10))
            sobrante_widget = QTableWidgetItem(str(10))
            valor_widget = QTableWidgetItem(str(10.50))
            id+=1

            if tabla == 1: #Si se proviene de agregar, las siguientes operaciones se hacen en la tabla agregar
                self.ui.agregar_tableWidget.setColumnCount(7) #7 columnas
                self.ui.agregar_tableWidget.setRowCount(7) #7 filas, para probar el programa
                self.ui.agregar_tableWidget.setHorizontalHeaderLabels(headers) #Se insertan los encabezados

                #Se insertan los elementos a la tabla de agregar
                self.ui.agregar_tableWidget.setItem(row, 0, fecha_widget) #Fila, columna, elemento
                self.ui.agregar_tableWidget.setItem(row, 1, id_widget)
                self.ui.agregar_tableWidget.setItem(row, 2, producto_widget)
                self.ui.agregar_tableWidget.setItem(row, 3, producido_widget)
                self.ui.agregar_tableWidget.setItem(row, 4, vendido_widget)
                self.ui.agregar_tableWidget.setItem(row, 5, sobrante_widget)
                self.ui.agregar_tableWidget.setItem(row, 6, valor_widget)
                row+=1 #Cambia a la siguiente fila
                i+=1

            elif tabla == 2: #Si se proviene de buscar, las siguientes operaciones se hacen en la tabla buscar
                self.ui.buscar_tableWidget.setColumnCount(7)
                self.ui.buscar_tableWidget.setRowCount(7)
                self.ui.buscar_tableWidget.setHorizontalHeaderLabels(headers)

                self.ui.buscar_tableWidget.setItem(row, 0, fecha_widget)
                self.ui.buscar_tableWidget.setItem(row, 1, id_widget)
                self.ui.buscar_tableWidget.setItem(row, 2, producto_widget)
                self.ui.buscar_tableWidget.setItem(row, 3, producido_widget)
                self.ui.buscar_tableWidget.setItem(row, 4, vendido_widget)
                self.ui.buscar_tableWidget.setItem(row, 5, sobrante_widget)
                self.ui.buscar_tableWidget.setItem(row, 6, valor_widget)
                row += 1
                i+=1

        if tabla == 1:
            self.ui.agregar_plainTextEdit.insertPlainText(str(self.total)) #Se ingresa el valor total a la pestania agregar
        elif tabla == 2:
            self.ui.buscar_plainTextEdit.insertPlainText(str(self.total)) #Se ingresa el valor total a la pestania buscar

    @Slot()
    def click_eliminar(self): #Para eliminar un registro
        fecha = self.ui.agregar_dateEdit.date() #Se consigue la fecha
        encontrado = False #Para indicar que fue encontrado
        print("Eliminar") #Se elimina si fue encontrado, por el momento se deja asi para probar el programa


        if not encontrado: #Si no se encuentra se manda mensaje de error
            QMessageBox.warning(
                self,
                "Atencion",
                f'Los registros con fecha "{fecha}" no fueron encontrados'
            )

    @Slot()
    def click_cambiar_precio(self): #Para cambiar el precio de los elementos del menu
        #Se mueven los datos a variables
        polloPrec = self.ui.pollo_precio_doubleSpinBox.value()
        tacoPrec = self.ui.taco_precio_doubleSpinBox.value()
        pescuezoPrec = self.ui.pescuezo_precio_doubleSpinBox.value()
        papaPrec = self.ui.papa_precio_doubleSpinBox.value()
        molePrec = self.ui.mole_precio_doubleSpinBox.value()
        ensaladaPrec = self.ui.ensalada_precio_doubleSpinBox.value()
        chamorroPrec = self.ui.chamorro_precio_doubleSpinBox.value()
        #Se modifican los valores
        self.producto[1] = polloPrec
        self.producto[2] = tacoPrec
        self.producto[3] = pescuezoPrec
        self.producto[4] = papaPrec
        self.producto[5] = molePrec
        self.producto[6] = ensaladaPrec
        self.producto[7] = chamorroPrec
        print(self.producto) #Se imprimen los nuevos valores, para probar el programa

        self.click_mostrar_precio() #Para mostrar los precios nuevos

    @Slot()
    def click_mostrar_precio(self): #Para ver los precios
        row = 0 #Fila 0
        headers = ["Pollo", "Taco", "Pescuezo", "Orden Papas", "Orden Mole", "Orden Ensalada", "Orden Chamorro"] #Encabezados
        #Se convierten los elementos en elementos para insertar en la tabla
        pollo_widget = QTableWidgetItem(str(self.producto[1]))
        taco_widget = QTableWidgetItem(str(self.producto[2]))
        pescuezo_widget = QTableWidgetItem(str(self.producto[3]))
        papa_widget = QTableWidgetItem(str(self.producto[4]))
        mole_widget = QTableWidgetItem(str(self.producto[5]))
        ensalada_widget = QTableWidgetItem(str(self.producto[6]))
        chamorro_widget = QTableWidgetItem(str(self.producto[7]))
        self.ui.cambiar_precio_tableWidget.clear()  #Se limpia la pantalla de la tabla
        self.ui.cambiar_precio_tableWidget.setColumnCount(7) #Se indica la cantidad de columnas
        self.ui.cambiar_precio_tableWidget.setRowCount(1) #Se indica la cantidad de filas, para probar el programa
        self.ui.cambiar_precio_tableWidget.setHorizontalHeaderLabels(headers) #Se insertan los encabezados

        #Se muestran los precios
        self.ui.cambiar_precio_tableWidget.setItem(row, 0, pollo_widget) #Fila, columna, elemento
        self.ui.cambiar_precio_tableWidget.setItem(row, 1, taco_widget)
        self.ui.cambiar_precio_tableWidget.setItem(row, 2, pescuezo_widget)
        self.ui.cambiar_precio_tableWidget.setItem(row, 3, papa_widget)
        self.ui.cambiar_precio_tableWidget.setItem(row, 4, mole_widget)
        self.ui.cambiar_precio_tableWidget.setItem(row, 5, ensalada_widget)
        self.ui.cambiar_precio_tableWidget.setItem(row, 6, chamorro_widget)
