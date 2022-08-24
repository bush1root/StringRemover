from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
import pymem

def close():
     sys.exit(0);

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setObjectName("Dialog")
        self.resize(500, 183)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 10, 481, 161))
        self.frame.setStyleSheet("QFrame { \n"
"background-color: rgb(25, 25, 25);\n"
"border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(440, 0, 41, 31))
        self.pushButton.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"border-radius: 15px;\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(close);
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(460, 10, 47, 13))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 461, 30))
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(28, 28, 28);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: white;\n"
"    border: 2px solid rgb(255, 59, 59);\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 461, 30))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(28, 28, 28);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: white;\n"
"    border: 2px solid rgb(255, 59, 59);\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 120, 301, 30))
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(28, 28, 28);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: white;\n"
"    border: 2px solid rgb(255, 59, 59);\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 120, 150, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;    \n"
"    background-color: rgb(255, 59, 59);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(219, 55, 55);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(255, 59, 59);\n"
"    color: rgb(255, 59, 59);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 271, 16))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")

        self.pushButton_2.clicked.connect(self.remove);
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("String Remover", "String Remover"))
        self.label.setText(_translate("Dialog", "X"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "PID"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Address"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Lenght"))
        self.pushButton_2.setText(_translate("Dialog", "Remove"))
        self.label_2.setText(_translate("Dialog", "String Remover v1.0 [Author: @bush1root]"))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def remove(self):
        try:
           pymem.memory.write_string(pymem.process.open(int(self.lineEdit.text(), 0)), int(self.lineEdit_2.text(), 0), bytes(int(self.lineEdit_3.text(), 0)))
           print("Done!")
        except:
           print("Error :(")

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
