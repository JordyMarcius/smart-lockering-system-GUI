import sys
import serial
import icon_rc # import icon pada GUI
import gspread
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget, QWidget, QMessageBox
from PyQt5.QtGui import QIntValidator
from datetime import datetime


class data_praktikan:

    def __init__(self, nama, npm, id, w1, w2, w3, w4, w5, w6):
        self.nama = nama
        self.npm = npm
        self.id = id
        self.week1 = w1
        self.week2 = w2
        self.week3 = w3
        self.week4 = w4
        self.week5 = w5
        self.week6 = w6


class catat_data:

    def __init__(self, nama):
        self.nama1 = nama
        self.nama2 = nama
        self.nama3 = nama
        self.nama4 = nama
        self.nama5 = nama


class edit_data:

    def __init__(self, id, number):
        self.id = id
        self.number = number
        self.data_praktikan = ""


class menu_utama(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_utama.ui", self)
        self.pushButton.clicked.connect(self.goto_menu_daftar)
        self.pushButton_2.clicked.connect(self.goto_menu_admin)
        self.pushButton_3.clicked.connect(self.goto_menu_help)
        self.pushButton_4.clicked.connect(self.goto_exit)

    def goto_menu_daftar(self):
        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_admin(self):
        menu_admin_var = menu_admin()
        widget.addWidget(menu_admin_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_help(self):
        menu_help_var = menu_help()
        widget.addWidget(menu_help_var)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goto_exit(self):
        ret = QMessageBox.information(self, "Exit GUI", "Are you sure want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            sys.exit()
        else:
            None


class menu_admin(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_admin.ui", self)
        self.pushButton.clicked.connect(self.goto_menu_daftar)
        self.pushButton_3.clicked.connect(self.goto_menu_help)
        self.pushButton_4.clicked.connect(self.goto_exit)
        self.pushButton_5.clicked.connect(self.goto_menu_utama)
        self.pushButton_6.clicked.connect(self.goto_menu_admin2)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password) # hide password
        self.checkBox.clicked.connect(self.click)

    def goto_menu_daftar(self):
        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_help(self):
        menu_help_var = menu_help()
        widget.addWidget(menu_help_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_exit(self):
        ret = QMessageBox.information(self, "Exit GUI", "Are you sure want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            sys.exit()
        else:
            None

    def goto_menu_utama(self):
        menu_utama_var = menu_utama()
        widget.addWidget(menu_utama_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_admin2(self):
        id = self.lineEdit.text()
        pin = self.lineEdit_2.text()
        if len(id) == 0 or len(pin) == 0:
            self.label_5.setText("Incorrect username or password")
        else:
            data = worksheet3.get_all_values()
            row = len(data)
            for i in range(row-1):
                username = data[i+1][0]
                password = data[i+1][1]
                if str(id.lower()) == str(username.lower()) and str(pin.lower()) == str(password.lower()):
                    self.label_5.setText("Login successful!")
                    menu_admin_2_var = menu_admin_2()
                    widget.addWidget(menu_admin_2_var)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    self.label_5.setText("Incorrect username or password")

    def click(self):
        if(self.checkBox.isChecked()):
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)


class menu_admin_2(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_admin_2.ui", self)
        self.pushButton.clicked.connect(self.goto_menu_admin)
        self.load_data()
    
    def goto_menu_admin(self):
        menu_admin_var = menu_admin()
        widget.addWidget(menu_admin_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def load_data(self):
        data = worksheet1.get_all_values()
        row = len(data)
        column = len(data[1])
        self.tableWidget.setRowCount(row-2)
        for i in range(row-2):
            for j in range(column):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(data[i+2][j]))


class menu_help(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_help.ui", self)
        self.pushButton.clicked.connect(self.goto_menu_daftar)
        self.pushButton_2.clicked.connect(self.goto_menu_admin)
        self.pushButton_4.clicked.connect(self.goto_exit)
        self.pushButton_5.clicked.connect(self.goto_menu_utama)
        self.pushButton_6.clicked.connect(self.submit)

    def goto_menu_daftar(self):
        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_admin(self):
        menu_admin_var = menu_admin()
        widget.addWidget(menu_admin_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_exit(self):
        ret = QMessageBox.information(self, "Exit GUI", "Are you sure want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            sys.exit()
        else:
            None

    def goto_menu_utama(self):
        menu_utama_var = menu_utama()
        widget.addWidget(menu_utama_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def submit(self):
        teks = self.textEdit.toPlainText()
        if len(teks) == 0:
            self.label_13.setText("")
        else:
            row_now = len(worksheet4.get_all_values())
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            worksheet4.update_cell(row_now+1, 1, dt_string)
            worksheet4.update_cell(row_now+1, 2, teks)
            self.label_13.setText("Your response has been recorded")


class menu_daftar(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_daftar.ui", self)
        self.pushButton_2.clicked.connect(self.goto_menu_admin)
        self.pushButton_3.clicked.connect(self.goto_menu_help)
        self.pushButton_4.clicked.connect(self.goto_exit)
        self.pushButton_5.clicked.connect(self.goto_menu_utama)
        self.pushButton_6.clicked.connect(self.goto_menu_daftar_1)
        self.pushButton_7.clicked.connect(self.goto_menu_edit_1)
        if len(catat_data.nama1) == 0:
            self.label_4.setText("No activity yet")
        else:    
            self.label_4.setText(catat_data.nama1.upper() + " successfully registered")
        
        if len(catat_data.nama2) == 0:
            self.label_5.setText("No activity yet")
        else:
            self.label_5.setText(catat_data.nama2.upper() + " successfully registered")

        if len(catat_data.nama3) == 0:
            self.label_6.setText("No activity yet")
        else:
            self.label_6.setText(catat_data.nama3.upper() + " successfully registered")
        
        if len(catat_data.nama4) == 0:
            self.label_7.setText("No activity yet")
        else:
            self.label_7.setText(catat_data.nama4.upper() + " successfully registered")

        if len(catat_data.nama5) == 0:
            self.label_8.setText("No activity yet")
        else:
            self.label_8.setText(catat_data.nama5.upper() + " successfully registered")

    def goto_menu_admin(self):
        menu_admin_var = menu_admin()
        widget.addWidget(menu_admin_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_help(self):
        menu_help_var = menu_help()
        widget.addWidget(menu_help_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_exit(self):
        ret = QMessageBox.information(self, "Exit GUI", "Are you sure want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            sys.exit()
        else:
            None

    def goto_menu_utama(self):
        menu_utama_var = menu_utama()
        widget.addWidget(menu_utama_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_daftar_1(self):
        menu_daftar_1_var = menu_daftar_1()
        widget.addWidget(menu_daftar_1_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_edit_1(self):
        edit_data.id = ""
        edit_data.number = ""
        edit_data.data_praktikan = ""
        menu_edit_1_var = menu_edit_1()
        widget.addWidget(menu_edit_1_var)
        widget.setCurrentIndex(widget.currentIndex()+1)


class menu_daftar_1(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_daftar_1.ui", self)
        self.onlyInt = QIntValidator()
        self.lineEdit_2.setValidator(self.onlyInt)
        self.pushButton.clicked.connect(self.goto_menu_daftar)
        self.pushButton_2.clicked.connect(self.goto_menu_daftar_2)

    def goto_menu_daftar(self):
        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goto_menu_daftar_2(self):
        nama = self.lineEdit.text()
        npm = self.lineEdit_2.text()
        data_praktikan.nama = nama
        data_praktikan.npm = npm
        if len(nama) == 0 or len(npm) == 0:
            self.label_4.setText("Enter a name or npm")
        else:
            menu_daftar_2_var = menu_daftar_2()
            widget.addWidget(menu_daftar_2_var)
            widget.setCurrentIndex(widget.currentIndex()+1)


class menu_daftar_2(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_daftar_2.ui", self)
        self.label_9.setText(data_praktikan.nama)
        self.label_10.setText(data_praktikan.npm)
        self.pushButton.clicked.connect(self.goto_menu_daftar_1)
        self.pushButton_2.clicked.connect(self.goto_menu_daftar_3)
        self.pushButton_3.clicked.connect(self.goto_refresh)

    def goto_menu_daftar_1(self):
        menu_daftar_1_var = menu_daftar_1()
        widget.addWidget(menu_daftar_1_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_daftar_3(self):
        data_praktikan.week1 = 0
        data_praktikan.week2 = 0
        data_praktikan.week3 = 0
        data_praktikan.week4 = 0
        data_praktikan.week5 = 0
        data_praktikan.week6 = 0
        menu_daftar_3_var = menu_daftar_3()
        widget.addWidget(menu_daftar_3_var)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goto_refresh(self):
        id = str(ser.readline()[1:].decode("utf-8").strip())
        self.label_11.setText(id) 
        data_praktikan.id = id


class menu_daftar_3(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_daftar_3.ui", self)
        self.pushButton.clicked.connect(self.goto_menu_daftar_2)
        self.pushButton_2.clicked.connect(self.goto_menu_daftar_4)

    def goto_menu_daftar_2(self):
        menu_daftar_2_var = menu_daftar_2()
        widget.addWidget(menu_daftar_2_var)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goto_menu_daftar_4(self):
        if self.radioButton.isChecked():
            data_praktikan.week1 = 1
        elif self.radioButton_2.isChecked():
            data_praktikan.week1 = 2
        elif self.radioButton_3.isChecked():
            data_praktikan.week1 = 3
        elif self.radioButton_4.isChecked():
            data_praktikan.week1 = 4
        elif self.radioButton_5.isChecked():
            data_praktikan.week1 = 5
        elif self.radioButton_6.isChecked():
            data_praktikan.week1 = 6
        else:
            data_praktikan.week1 = 0
        
        if self.radioButton_7.isChecked():
            data_praktikan.week2 = 1
        elif self.radioButton_8.isChecked():
            data_praktikan.week2 = 2
        elif self.radioButton_10.isChecked():
            data_praktikan.week2 = 3
        elif self.radioButton_9.isChecked():
            data_praktikan.week2 = 4
        elif self.radioButton_11.isChecked():
            data_praktikan.week2 = 5
        elif self.radioButton_12.isChecked():
            data_praktikan.week2 = 6
        else:
            data_praktikan.week2 = 0
        
        if self.radioButton_16.isChecked():
            data_praktikan.week3 = 1
        elif self.radioButton_15.isChecked():
            data_praktikan.week3 = 2
        elif self.radioButton_18.isChecked():
            data_praktikan.week3 = 3
        elif self.radioButton_17.isChecked():
            data_praktikan.week3 = 4
        elif self.radioButton_14.isChecked():
            data_praktikan.week3 = 5
        elif self.radioButton_13.isChecked():
            data_praktikan.week3 = 6
        else:
            data_praktikan.week3 = 0

        if self.radioButton_21.isChecked():
            data_praktikan.week4 = 1
        elif self.radioButton_20.isChecked():
            data_praktikan.week4 = 2
        elif self.radioButton_19.isChecked():
            data_praktikan.week4 = 3
        elif self.radioButton_24.isChecked():
            data_praktikan.week4 = 4
        elif self.radioButton_22.isChecked():
            data_praktikan.week4 = 5
        elif self.radioButton_23.isChecked():
            data_praktikan.week4 = 6
        else:
            data_praktikan.week4 = 0

        if self.radioButton_30.isChecked():
            data_praktikan.week5 = 1
        elif self.radioButton_25.isChecked():
            data_praktikan.week5 = 2
        elif self.radioButton_27.isChecked():
            data_praktikan.week5 = 3
        elif self.radioButton_28.isChecked():
            data_praktikan.week5 = 4
        elif self.radioButton_26.isChecked():
            data_praktikan.week5 = 5
        elif self.radioButton_29.isChecked():
            data_praktikan.week5 = 6
        else:
            data_praktikan.week5 = 0

        if self.radioButton_32.isChecked():
            data_praktikan.week6 = 1
        elif self.radioButton_36.isChecked():
            data_praktikan.week6 = 2
        elif self.radioButton_34.isChecked():
            data_praktikan.week6 = 3
        elif self.radioButton_35.isChecked():
            data_praktikan.week6 = 4
        elif self.radioButton_33.isChecked():
            data_praktikan.week6 = 5
        elif self.radioButton_31.isChecked():
            data_praktikan.week6 = 6
        else:
            data_praktikan.week6 = 0

        menu_daftar_4_var = menu_daftar_4()
        widget.addWidget(menu_daftar_4_var)
        widget.setCurrentIndex(widget.currentIndex()+1)


class menu_daftar_4(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_daftar_4.ui", self)
        self.label_9.setText(data_praktikan.nama)
        self.label_10.setText(data_praktikan.npm)
        self.label_11.setText(data_praktikan.id)
        self.label_13.setText(str(data_praktikan.week1) + " " + str(data_praktikan.week2) + " " + str(data_praktikan.week3) + " " + str(data_praktikan.week4) + " " + str(data_praktikan.week5) + " " + str(data_praktikan.week6))
        self.pushButton.clicked.connect(self.goto_menu_daftar_3)
        self.pushButton_2.clicked.connect(self.goto_menu_daftar)

    def goto_menu_daftar_3(self):
        menu_daftar_3_var = menu_daftar_3()
        widget.addWidget(menu_daftar_3_var)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goto_menu_daftar(self):
        catat_data.nama5 = catat_data.nama4
        catat_data.nama4 = catat_data.nama3
        catat_data.nama3 = catat_data.nama2
        catat_data.nama2 = catat_data.nama1
        catat_data.nama1 = data_praktikan.nama

        row_now = len(worksheet1.get_all_values())
        worksheet1.update_cell(row_now + 1, 1, data_praktikan.nama.upper())
        worksheet1.update_cell(row_now + 1, 2, data_praktikan.npm)
        worksheet1.update_cell(row_now + 1, 3, data_praktikan.id)
        worksheet1.update_cell(row_now + 1, 4, data_praktikan.week1)
        worksheet1.update_cell(row_now + 1, 5, data_praktikan.week2)
        worksheet1.update_cell(row_now + 1, 6, data_praktikan.week3)
        worksheet1.update_cell(row_now + 1, 7, data_praktikan.week4)
        worksheet1.update_cell(row_now + 1, 8, data_praktikan.week5)
        worksheet1.update_cell(row_now + 1, 9, data_praktikan.week6)

        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)


class menu_edit_1(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_edit_1.ui", self)
        self.pushButton.clicked.connect(self.goto_menu_daftar)
        self.pushButton_2.clicked.connect(self.goto_menu_edit_2)
        self.pushButton_3.clicked.connect(self.goto_refresh)
    
    def goto_menu_daftar(self):
        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goto_menu_edit_2(self):
        if len(edit_data.id) == 0:
            self.label.setText("Scan your ID card to login")
        else:
            data = worksheet1.get_all_values()
            row = len(data)
            for i in range(row-2):
                if str(data[i+2][2]) == edit_data.id:
                    self.label.setText("Login successful!")
                    edit_data.number = i+2
                    edit_data.data_praktikan = data[i+2]
                    menu_edit_2_var = menu_edit_2()
                    widget.addWidget(menu_edit_2_var)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    self.label.setText("This ID has not been registered")
    
    def goto_refresh(self):
        id = str(ser.readline()[1:].decode("utf-8").strip())
        self.label_11.setText(id) 
        edit_data.id = id


class menu_edit_2(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_edit_2.ui", self)
        self.label_14.setText(edit_data.data_praktikan[0].upper())
        self.label_15.setText(edit_data.data_praktikan[1])
        self.label_16.setText(str(edit_data.data_praktikan[3]) + " " + str(edit_data.data_praktikan[4]) + " " + str(edit_data.data_praktikan[5]) + " " + str(edit_data.data_praktikan[6]) + " " + str(edit_data.data_praktikan[7]) + " " + str(edit_data.data_praktikan[8]))
        self.pushButton.clicked.connect(self.goto_menu_edit_1)
        self.pushButton_2.clicked.connect(self.goto_menu_daftar)
        self.pushButton_3.clicked.connect(self.goto_update)
        self.pushButton_5.clicked.connect(self.goto_menu_edit_3)
        self.pushButton_6.clicked.connect(self.goto_menu_edit_4)
    
    def goto_menu_edit_1(self):
        menu_edit_1_var = menu_edit_1()
        widget.addWidget(menu_edit_1_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_daftar(self):
        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goto_update(self): 
        nama_baru = self.lineEdit.text()
        edit_data.data_praktikan[0] = nama_baru
        self.label_14.setText(edit_data.data_praktikan[0].upper())
        worksheet1.update_cell(edit_data.number+1, 1, nama_baru.upper())
        self.label_5.setText("Nama sucessfully updated")
    
    def goto_menu_edit_3(self):
        menu_edit_3_var = menu_edit_3()
        widget.addWidget(menu_edit_3_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_edit_4(self):
        menu_edit_4_var = menu_edit_4()
        widget.addWidget(menu_edit_4_var)
        widget.setCurrentIndex(widget.currentIndex()+1)


class menu_edit_3(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_edit_3.ui", self)
        self.onlyInt = QIntValidator()
        self.lineEdit.setValidator(self.onlyInt)
        self.label_14.setText(edit_data.data_praktikan[0].upper())
        self.label_15.setText(edit_data.data_praktikan[1])
        self.label_16.setText(str(edit_data.data_praktikan[3]) + " " + str(edit_data.data_praktikan[4]) + " " + str(edit_data.data_praktikan[5]) + " " + str(edit_data.data_praktikan[6]) + " " + str(edit_data.data_praktikan[7]) + " " + str(edit_data.data_praktikan[8]))
        self.pushButton.clicked.connect(self.goto_menu_edit_1)
        self.pushButton_2.clicked.connect(self.goto_menu_daftar)
        self.pushButton_3.clicked.connect(self.goto_update)
        self.pushButton_4.clicked.connect(self.goto_menu_edit_2)
        self.pushButton_6.clicked.connect(self.goto_menu_edit_4)
    
    def goto_menu_edit_1(self):
        menu_edit_1_var = menu_edit_1()
        widget.addWidget(menu_edit_1_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_daftar(self):
        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_update(self):
        npm_baru = self.lineEdit.text()
        edit_data.data_praktikan[1] = npm_baru
        self.label_15.setText(edit_data.data_praktikan[1])
        worksheet1.update_cell(edit_data.number+1, 2, npm_baru)
        self.label_5.setText("NPM sucessfully updated")

    def goto_menu_edit_2(self):
        menu_edit_2_var = menu_edit_2()
        widget.addWidget(menu_edit_2_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_edit_4(self):
        menu_edit_4_var = menu_edit_4()
        widget.addWidget(menu_edit_4_var)
        widget.setCurrentIndex(widget.currentIndex()+1)


class menu_edit_4(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        loadUi("menu_edit_4.ui", self)
        self.label_14.setText(edit_data.data_praktikan[0].upper())
        self.label_15.setText(edit_data.data_praktikan[1])
        self.label_16.setText(str(edit_data.data_praktikan[3]) + " " + str(edit_data.data_praktikan[4]) + " " + str(edit_data.data_praktikan[5]) + " " + str(edit_data.data_praktikan[6]) + " " + str(edit_data.data_praktikan[7]) + " " + str(edit_data.data_praktikan[8]))
        self.pushButton.clicked.connect(self.goto_menu_edit_1)
        self.pushButton_2.clicked.connect(self.goto_menu_daftar)
        self.pushButton_3.clicked.connect(self.goto_update)
        self.pushButton_4.clicked.connect(self.goto_menu_edit_2)
        self.pushButton_5.clicked.connect(self.goto_menu_edit_3)
    
    def goto_menu_edit_1(self):
        menu_edit_1_var = menu_edit_1()
        widget.addWidget(menu_edit_1_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu_daftar(self):
        menu_daftar_var = menu_daftar()
        widget.addWidget(menu_daftar_var)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_update(self):
        if self.radioButton.isChecked():
            w1 = 1
        elif self.radioButton_2.isChecked():
            w1 = 2
        elif self.radioButton_3.isChecked():
            w1 = 3
        elif self.radioButton_4.isChecked():
            w1 = 4
        elif self.radioButton_5.isChecked():
            w1 = 5
        elif self.radioButton_6.isChecked():
            w1 = 6
        else:
            w1 = 0
        
        if self.radioButton_7.isChecked():
            w2 = 1
        elif self.radioButton_8.isChecked():
            w2 = 2
        elif self.radioButton_10.isChecked():
            w2 = 3
        elif self.radioButton_9.isChecked():
            w2 = 4
        elif self.radioButton_11.isChecked():
            w2 = 5
        elif self.radioButton_12.isChecked():
            w2 = 6
        else:
            w2 = 0
        
        if self.radioButton_16.isChecked():
            w3 = 1
        elif self.radioButton_15.isChecked():
            w3 = 2
        elif self.radioButton_18.isChecked():
            w3 = 3
        elif self.radioButton_17.isChecked():
            w3 = 4
        elif self.radioButton_14.isChecked():
            w3 = 5
        elif self.radioButton_13.isChecked():
            w3 = 6
        else:
            w3 = 0

        if self.radioButton_21.isChecked():
            w4 = 1
        elif self.radioButton_20.isChecked():
            w4 = 2
        elif self.radioButton_19.isChecked():
            w4 = 3
        elif self.radioButton_24.isChecked():
            w4 = 4
        elif self.radioButton_22.isChecked():
            w4 = 5
        elif self.radioButton_23.isChecked():
            w4 = 6
        else:
            w4 = 0

        if self.radioButton_30.isChecked():
            w5 = 1
        elif self.radioButton_25.isChecked():
            w5 = 2
        elif self.radioButton_27.isChecked():
            w5 = 3
        elif self.radioButton_28.isChecked():
            w5 = 4
        elif self.radioButton_26.isChecked():
            w5 = 5
        elif self.radioButton_29.isChecked():
            w5 = 6
        else:
            w5 = 0

        if self.radioButton_32.isChecked():
            w6 = 1
        elif self.radioButton_36.isChecked():
            w6 = 2
        elif self.radioButton_34.isChecked():
            w6 = 3
        elif self.radioButton_35.isChecked():
            w6 = 4
        elif self.radioButton_33.isChecked():
            w6 = 5
        elif self.radioButton_31.isChecked():
            w6 = 6
        else:
            w6 = 0
            
        edit_data.data_praktikan[3] = w1
        edit_data.data_praktikan[4] = w2
        edit_data.data_praktikan[5] = w3
        edit_data.data_praktikan[6] = w4
        edit_data.data_praktikan[7] = w5
        edit_data.data_praktikan[8] = w6
        self.label_16.setText(str(edit_data.data_praktikan[3]) + " " + str(edit_data.data_praktikan[4]) + " " + str(edit_data.data_praktikan[5]) + " " + str(edit_data.data_praktikan[6]) + " " + str(edit_data.data_praktikan[7]) + " " + str(edit_data.data_praktikan[8]))
        
        worksheet1.update_cell(edit_data.number+1, 4, w1)
        worksheet1.update_cell(edit_data.number+1, 5, w2)
        worksheet1.update_cell(edit_data.number+1, 6, w3)
        worksheet1.update_cell(edit_data.number+1, 7, w4)
        worksheet1.update_cell(edit_data.number+1, 8, w5)
        worksheet1.update_cell(edit_data.number+1, 9, w6)
    
    def goto_menu_edit_2(self):
        menu_edit_2_var = menu_edit_2()
        widget.addWidget(menu_edit_2_var)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goto_menu_edit_3(self):
        menu_edit_3_var = menu_edit_3()
        widget.addWidget(menu_edit_3_var)
        widget.setCurrentIndex(widget.currentIndex()+1)


service_account = gspread.service_account("E:/Semester 7/Desain Proyek 2/GUI_Pendaftaran/despro_kelompok6.json")
sheet = service_account.open("Database")
worksheet1 = sheet.worksheet("Data Praktikan")
worksheet2 = sheet.worksheet("Data Peminjaman")
worksheet3 = sheet.worksheet("Admin")
worksheet4 = sheet.worksheet("Response")

ser = serial.Serial('COM3', baudrate = 115200, timeout = 1)

data_praktikan.nama = ""
catat_data.nama1 = ""
catat_data.nama2 = ""
catat_data.nama3 = ""
catat_data.nama4 = ""
catat_data.nama5 = ""

edit_data.id = ""
edit_data.number = ""
edit_data.data_praktikan = ""

app = QApplication(sys.argv)
menu = menu_utama()
widget = QStackedWidget()
widget.addWidget(menu)
widget.setFixedHeight(500)
widget.setFixedWidth(800)
widget.setWindowTitle("Desain Proyek 2 Kelompok 06")
widget.show()
sys.exit(app.exec_())