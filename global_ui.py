import sys

from PyQt5 import QtWidgets, QtCore, QtGui


from main_window import Ui_MainWindow
from window_row_type_section_num import Ui_winRowType
from window_parameters import Ui_windowParameters


class WindowRowTypeSectNum(QtWidgets.QWidget, Ui_winRowType):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class WindowBladeParameters(QtWidgets.QWidget, Ui_windowParameters):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rtsn_window = None
        self.prmt_window = None
        self.number_of_sections = int()
        self.setupUi(self)
        self.row_type_section_num_win()

    def row_type_section_num_win(self):
        self.rtsn_window = WindowRowTypeSectNum(self)
        self.setWindowTitle("first window")
        self.setCentralWidget(self.rtsn_window)
        self.rtsn_window.btnCheck.clicked.connect(self.push_check_btn)

        self.rtsn_window.lineEditErrorCheck.setReadOnly(True)

        self.rtsn_window.rBtn_igv.clicked.connect(self.radio_buttons)
        self.rtsn_window.rBtn_ogv.clicked.connect(self.radio_buttons)
        self.rtsn_window.rBtn_strout.clicked.connect(self.radio_buttons)
        self.rtsn_window.rBtn_rotor.clicked.connect(self.radio_buttons)
        self.rtsn_window.rBtn_stator.clicked.connect(self.radio_buttons)
        self.rtsn_window.btnNext.clicked.connect(self.try_to_go_params_window)
        self.show()

    def push_check_btn(self):
        try:
            float(self.rtsn_window.lineEditNUmSect.text())
            if isinstance(int(self.rtsn_window.lineEditNUmSect.text()), int):
                radio_buttons = [self.rtsn_window.rBtn_igv,
                                 self.rtsn_window.rBtn_ogv,
                                 self.rtsn_window.rBtn_strout,
                                 self.rtsn_window.rBtn_stator,
                                 self.rtsn_window.rBtn_rotor]
                for i in radio_buttons:
                    if i.isChecked():
                        self.rtsn_window.lineEditErrorCheck.setText("true")
                        self.number_of_sections = int(self.rtsn_window.lineEditNUmSect.text())
                        break
                    else:
                        if i == radio_buttons[-1]:
                            self.rtsn_window.lineEditErrorCheck.setText("false")
        except:
            self.rtsn_window.lineEditErrorCheck.setText("false")

    def radio_buttons(self):
        if self.rtsn_window.rBtn_igv.isChecked():
            self.row_type = "IGV"
        if self.rtsn_window.rBtn_ogv.isChecked():
            self.row_type = "OGV"
        if self.rtsn_window.rBtn_strout.isChecked():
            self.row_type = "STROUT"
        if self.rtsn_window.rBtn_rotor.isChecked():
            self.row_type = "RB"
        if self.rtsn_window.rBtn_stator.isChecked():
            self.row_type = "SB"

    def create_cells(self, section_number = int()):
        input_list = list()
        for i in range(section_number):
            input_list.append(QtWidgets.QLineEdit())
            input_list[i].setMinimumSize(QtCore.QSize(51, 21))
            input_list[i].setMaximumSize(QtCore.QSize(51, 21))
        return input_list

    def parameters_window(self):
        self.prmt_window = WindowBladeParameters(self)
        self.setWindowTitle("second window")
        self.setCentralWidget(self.prmt_window)

        self.inlet_angle_cells = self.create_cells(self.number_of_sections)
        self.outlet_angle_cells = self.create_cells(self.number_of_sections)


        for i in range(self.number_of_sections):
            self.prmt_window.hLayout_inlet_angle.addWidget(self.inlet_angle_cells[i])
            self.prmt_window.hLayout_outlet_angle.addWidget(self.outlet_angle_cells[i])

        self.prmt_window.btnCheck.clicked.connect(self.check_btn_params_window)

        self.prmt_window.btnBack.clicked.connect(self.row_type_section_num_win)
        self.show()

    def try_to_go_params_window(self):
        if self.rtsn_window.lineEditErrorCheck.text() == "true":
            self.parameters_window()
        else:
            self.rtsn_window.lineEditErrorCheck.setText("try to change input data")

    def check_btn_params_window(self):
        if self.inlet_angle_cells[0].text() != "":
            print("checked")
        else:
            print("wrong")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())