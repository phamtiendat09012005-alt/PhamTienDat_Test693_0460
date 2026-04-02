# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450) # Đã thu nhỏ lại vì bỏ bớt phần sign/verify
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Tiêu đề
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Nhãn và ô nhập Plain Text
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 70, 13))
        self.label_2.setObjectName("label_2")
        
        self.txt_plaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(110, 80, 440, 71))
        self.txt_plaintext.setObjectName("txt_plaintext")
        
        # Nhãn và ô nhập Cipher Text
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 80, 13))
        self.label_3.setObjectName("label_3")
        
        self.txt_ciphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(110, 170, 440, 71))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        
        # --- THÊM MỚI: Nhãn và ô nhập Key (Số Rails) ---
        self.label_key = QtWidgets.QLabel(self.centralwidget)
        self.label_key.setGeometry(QtCore.QRect(30, 270, 80, 13))
        self.label_key.setObjectName("label_key")
        
        self.txt_key = QtWidgets.QLineEdit(self.centralwidget) # Dùng QLineEdit cho nhập 1 dòng ngắn
        self.txt_key.setGeometry(QtCore.QRect(110, 265, 100, 25))
        self.txt_key.setObjectName("txt_key")
        
        # Nút Encrypt
        self.btn_encypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encypt.setGeometry(QtCore.QRect(200, 330, 100, 30))
        self.btn_encypt.setObjectName("btn_encypt")
        
        # Nút Decrypt
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(350, 330, 100, 30))
        self.btn_decrypt.setObjectName("btn_decrypt")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rail Fence Cipher Tool"))
        self.label.setText(_translate("MainWindow", "Rail Fence Cipher"))
        self.label_2.setText(_translate("MainWindow", "Plain Text:"))
        self.label_3.setText(_translate("MainWindow", "Cipher Text:"))
        self.label_key.setText(_translate("MainWindow", "Key (Rails):")) # Label cho Key
        self.btn_encypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))