# import libs
import sys
import numpy as np
import matplotlib.pyplot as plt


# import part of lib
from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# user's classes
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

    def create_input_cells(self, section_number = int()):
        input_list = list()
        for i in range(section_number):
            input_list.append(QtWidgets.QLineEdit())
            input_list[i].setMinimumSize(QtCore.QSize(51, 21))
            input_list[i].setMaximumSize(QtCore.QSize(51, 21))
        return input_list

    def create_output_cells(self, section_number = int()):
        input_list = list()
        for i in range(section_number):
            input_list.append(QtWidgets.QLineEdit())
            input_list[i].setReadOnly(True)
            input_list[i].setMinimumSize(QtCore.QSize(51, 21))
            input_list[i].setMaximumSize(QtCore.QSize(51, 21))
        return input_list

    def parameters_window(self):
        self.prmt_window = WindowBladeParameters(self)
        self.setWindowTitle("second window")
        self.setCentralWidget(self.prmt_window)
        self.prmt_win_add_cells()
        self.prmt_win_add_graph_plot()

        # add btn to check parameters in cells
        self.prmt_window.btnCheck.clicked.connect(self.check_btn_params_window)

        # add btn to return first win with num of sections and row type
        self.prmt_window.btnBack.clicked.connect(self.row_type_section_num_win)
        self.show()

    def prmt_win_add_cells(self):
        # add cells to input data
        self.inlet_angle_cells = self.create_input_cells(self.number_of_sections)
        self.outlet_angle_cells = self.create_input_cells(self.number_of_sections)
        self.le_radius_cells = self.create_input_cells(self.number_of_sections)
        self.te_radius_cells = self.create_input_cells(self.number_of_sections)
        self.chord_cells = self.create_input_cells(self.number_of_sections)
        self.cmax_cells = self.create_input_cells(self.number_of_sections)
        self.cmax_position_cells = self.create_input_cells(self.number_of_sections)
        self.front_camber_angle_cells = self.create_input_cells(self.number_of_sections)
        self.radius_at_le_cells = self.create_input_cells(self.number_of_sections)
        self.radius_at_te_cells = self.create_input_cells(self.number_of_sections)
        self.restagger_section_cells = self.create_input_cells(self.number_of_sections)
        self.theta_displ_cells = self.create_input_cells(self.number_of_sections)
        self.axial_displ_cells = self.create_input_cells(self.number_of_sections)

        # add cells to output data
        self.stagger_angle_cells = self.create_output_cells(self.number_of_sections)
        self.axial_chord_cells = self.create_output_cells(self.number_of_sections)
        self.camber_angle_cells = self.create_output_cells(self.number_of_sections)
        self.le_we_angle_cells = self.create_output_cells(self.number_of_sections)
        self.te_we_angle_cells = self.create_output_cells(self.number_of_sections)
        self.max_thickness_cells = self.create_output_cells(self.number_of_sections)
        self.throat_cells = self.create_output_cells(self.number_of_sections)
        self.solidity_cells = self.create_output_cells(self.number_of_sections)
        self.camber_ratio_cells = self.create_output_cells(self.number_of_sections)
        self.sect_area_cells = self.create_output_cells(self.number_of_sections)

        # add cells to window
        for i in range(self.number_of_sections):
            self.prmt_window.hLayout_inlet_angle.addWidget(self.inlet_angle_cells[i])
            self.prmt_window.hLayout_outlet_angle.addWidget(self.outlet_angle_cells[i])
            self.prmt_window.hLayout_le_rad.addWidget(self.le_radius_cells[i])
            self.prmt_window.hLayout_te_rad.addWidget(self.te_radius_cells[i])
            self.prmt_window.hLayout_chord.addWidget(self.chord_cells[i])
            self.prmt_window.hLayout_cmax.addWidget(self.cmax_cells[i])
            self.prmt_window.hLayout_cmax_pos.addWidget(self.cmax_position_cells[i])
            self.prmt_window.hLayout_front_camber_angle.addWidget(self.front_camber_angle_cells[i])
            self.prmt_window.hLayout_rad_at_le.addWidget(self.radius_at_le_cells[i])
            self.prmt_window.hLayout_rad_at_te.addWidget(self.radius_at_te_cells[i])
            self.prmt_window.hLayout_restagger_sect.addWidget(self.restagger_section_cells[i])
            self.prmt_window.hLayout_theta_displ.addWidget(self.theta_displ_cells[i])
            self.prmt_window.hLayout_axial_displ.addWidget(self.axial_displ_cells[i])

            self.prmt_window.hLayout_stagger_angle.addWidget(self.stagger_angle_cells[i])
            self.prmt_window.hLayout_axial_chord.addWidget(self.axial_chord_cells[i])
            self.prmt_window.hLayout_camber_angle.addWidget(self.camber_angle_cells[i])
            self.prmt_window.hLayout_le_we_ang.addWidget(self.le_we_angle_cells[i])
            self.prmt_window.hLayout_te_we_ang.addWidget(self.te_we_angle_cells[i])
            self.prmt_window.hLayout_value_cmax.addWidget(self.max_thickness_cells[i])
            self.prmt_window.hLayout_throat.addWidget(self.throat_cells[i])
            self.prmt_window.hLayout_solidity.addWidget(self.solidity_cells[i])
            self.prmt_window.hLayout_camber_ratio.addWidget(self.camber_ratio_cells[i])
            self.prmt_window.hLayout_section_area.addWidget(self.sect_area_cells[i])

    # add graphs to win # todo #plug
    def prmt_win_add_graph_plot(self):
        self.b2b_canvas = FigureCanvas(plt.Figure(figsize=(10, 5)))
        self.mer_canvas = FigureCanvas(plt.Figure(figsize=(10, 5)))
        self.prmt_window.hLayout_plot_out.addWidget(self.b2b_canvas)
        self.prmt_window.hLayout_plot_out.addWidget(self.mer_canvas)
        # print("check")
        # try:
        #     self.ax_b2b = self.b2b_canvas.figure.subplots()
        #     self.ax_b2b.grid()
        # except:
        #     pass




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