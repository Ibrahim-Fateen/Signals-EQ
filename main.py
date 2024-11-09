from PySide6.QtWidgets import QApplication, QMainWindow

import sys
from main_window import Ui_MainWindow
from PySide6.QtWidgets import QWidget
import pyqtgraph as pg
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.controls_frame.setMinimumHeight(280)
        plot_widget = pg.PlotWidget()
        plot_widget.setBackground('#13131F')
        plot_widget.showGrid(x=True, y=True)

        # Add the plot widget to the layout
        self.ui.graph2_widget.layout().addWidget(plot_widget)
        # Create another plot widget
        plot_widget2 = pg.PlotWidget()
        plot_widget2.setBackground('#13131F')
        plot_widget2.showGrid(x=True, y=True)
        # Add the second plot widget to the layout
        self.ui.graph1_widget.layout().addWidget(plot_widget2)

        # Plot some other data
        x2 = [1, 2, 3, 4, 5]
        y2 = [50, 40, 30, 20, 10]
        plot_data_item = pg.PlotDataItem(x2, y2, pen=pg.mkPen(color='r', width=2))
        plot_widget2.addItem(plot_data_item)
        # Plot some data
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 30, 40, 50]
        plot_data_item2 = pg.PlotDataItem(x, y, pen=pg.mkPen(color='g', width=2))
        plot_widget.addItem(plot_data_item2)
        # Create plot widgets for spectro1 and spectro2
        spectro1_widget = pg.PlotWidget()
        spectro2_widget = pg.PlotWidget()

        # Set the background color
        spectro1_widget.setBackground('#1e1d23')
        spectro2_widget.setBackground('#1e1d23')

        # Show grid
        spectro1_widget.showGrid(x=True, y=True)
        spectro2_widget.showGrid(x=True, y=True)
        

        # Add the plot widgets to the respective layouts
        self.ui.spectro1_widget.layout().addWidget(spectro1_widget)
        self.ui.spectro2_widget.layout().addWidget(spectro2_widget)

        # Plot some data for spectro1
        x3 = [1, 2, 3, 4, 5]
        y3 = [15, 25, 35, 45, 55]
        spectro1_widget.plot(x3, y3)

        # Plot some data for spectro2
        x4 = [1, 2, 3, 4, 5]
        y4 = [55, 45, 35, 25, 15]
        spectro2_widget.plot(x4, y4)
        self.ui.spectrogram_checkbox.stateChanged.connect(lambda state: self.show_hide_layout(self.ui.spectrograph_layout, state))
        self.show_hide_layout(self.ui.spectrograph_layout, False)

        # Add layouts to the combo box
        self.ui.modes_combo.addItem("Animal")
        self.ui.modes_combo.addItem("Music")
        self.ui.modes_combo.addItem("ECG")
        self.ui.modes_combo.addItem("Uniform")

        # Connect combo box selection change to a function
        self.ui.modes_combo.currentIndexChanged.connect(lambda index: self.show_selected_layout(index))
        self.show_selected_layout(0)

    def show_selected_layout(self, index):
        # Hide all layouts
        self.show_hide_widget(self.ui.animal_widget, False)
        self.show_hide_widget(self.ui.music_widget, False)
        self.show_hide_widget(self.ui.ECG_widget, False)
        self.show_hide_widget(self.ui.uniform_widget, False)

        # Show the selected layout
        if index == 0:
            self.show_hide_widget(self.ui.animal_widget, True)
        elif index == 1:
            self.show_hide_widget(self.ui.music_widget, True)
        elif index == 2:
            self.show_hide_widget(self.ui.ECG_widget, True)
        elif index == 3:
            self.show_hide_widget(self.ui.uniform_widget, True)
        

    def show_hide_widget(self, layout:QWidget, state):
        if layout:
            if state == 0:
                layout.hide()
            else:
                layout.show()
                
    def show_hide_layout(self, layout, state):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                if state == 0:
                    item.widget().hide()
                else:
                    item.widget().show()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

#cf66ea