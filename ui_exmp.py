import sys

from PyQt5 import QtWidgets, QtGui, QtCore

# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc


class NumSections(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(NumSections, self).__init__(parent)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.lblNumOfSect = QtWidgets.QLabel("number of sections", self)
        self.lblNumOfSect.setFixedSize(100, 20)
        self.btnAcceptNumOfSect = QtWidgets.QPushButton("accept", self)
        self.btnAcceptNumOfSect.setFixedSize(100, 20)
        self.txtNumOfSect = QtWidgets.QTextEdit(self)
        self.txtNumOfSect.setFixedSize(150, 25)
        self.hBxLt = QtWidgets.QHBoxLayout()
        self.hBxLt.addWidget(self.lblNumOfSect)
        self.hBxLt.addWidget(self.txtNumOfSect)
        # self.mainLayout.addWidget(self.lblNumOfSect)
        self.mainLayout.addLayout(self.hBxLt)
        self.mainLayout.addWidget(self.btnAcceptNumOfSect)
        self.setLayout(self.mainLayout)


class InputOutputParameters(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(InputOutputParameters, self).__init__(parent)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.btnBack = QtWidgets.QPushButton("back", self)
        self.mainLayout.addWidget(self.btnBack)

        self.btnCalc = QtWidgets.QPushButton("calculate", self)
        self.mainLayout.addWidget(self.btnCalc)
        self.setLayout(self.mainLayout)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(400, 450)
        self.firstWindow()

    def firstWindow(self):
        self.fstWin = NumSections(self)
        self.setWindowTitle("set number of sections")
        self.setCentralWidget(self.fstWin)
        self.fstWin.btnAcceptNumOfSect.clicked.connect(self.secondWindow)
        self.show()

    def secondWindow(self):
        self.sndWin = InputOutputParameters(self)
        self.setWindowTitle("input/output paramters, output graphs")
        self.setCentralWidget(self.sndWin)
        self.sndWin.btnBack.clicked.connect(self.firstWindow)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())