from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QErrorMessage
import sys
from PySide6.QtWidgets import QWidget
import pyqtgraph as pg
from enum import Enum

from main_window import Ui_MainWindow
from Spectrogram import SpectrogramWidget
from Signal import Signal


class Mode(Enum):
    ANIMAL_SOUNDS = 0
    MUSICAL_INSTRUMENTS = 1
    ECG = 2
    UNIFORM = 3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.controls_frame.setMinimumHeight(280)
        self.showMaximized()
        plot_widget = pg.PlotWidget()
        plot_widget.setBackground('#13131F')
        plot_widget.showGrid(x=True, y=True)

        self.frequencies = {
            # Animals
            "Dog": [(300, 800), (2000, 4000)],
            "Cat": [(500, 1000), (2000, 4000)],
            "Bird": [(1000, 3000), (4000, 8000)],
            "Lion": [(50, 300)],

            # Musical Instruments
            "Piano": [(27.5, 1000), (1000, 4186)],
            "Guitar": [(82, 500), (500, 1200)],
            "Violin": [(196, 1000), (1000, 4000)],
            "Bass Drums": [(40, 100), (100, 200)],

            "Normal ECG": [(0.05, 1), (1, 50)],
            "Atrial Fibrillation": [(0.05, 1), (1, 10), (10, 50)],
            "Ventricular Fibrillation": [(0.05, 0.5), (0.5, 5), (5, 20)],
            "Tachycardia": [(0.05, 0.5), (0.5, 5), (5, 20)]
        }

        self.sliders = {
            self.ui.animal_slider1: "Dog",
            self.ui.animal_slider2: "Cat",
            self.ui.animal_slider3: "Bird",
            self.ui.animal_slider4: "Lion",
            self.ui.music_slider1: "Piano",
            self.ui.music_slider2: "Guitar",
            self.ui.music_slider3: "Violin",
            self.ui.music_slider4: "Bass Drums",
            # self.ui.ecg_slider1: "Normal ECG",  # replace numbers with corresponding sliders
            # self.ui.ecg_slider2: "Atrial Fibrillation",  # replace with actual slider
            # self.ui.ecg_slider3: "Ventricular Fibrillation",  # replace with actual slider
            # self.ui.ecg_slider4: "Tachycardia",  # replace with acutal slider
            self.ui.uniform_slider1: "Uniform 1",
            self.ui.uniform_slider2: "Uniform 2",
            self.ui.uniform_slider3: "Uniform 3",
            self.ui.uniform_slider4: "Uniform 4",
            self.ui.uniform_slider5: "Uniform 5",
            self.ui.uniform_slider6: "Uniform 6",
            self.ui.uniform_slider7: "Uniform 7",
            self.ui.uniform_slider8: "Uniform 8",
            self.ui.uniform_slider9: "Uniform 9",
            self.ui.uniform_slider10: "Uniform 10"
        }

        self.current_mode = Mode.ANIMAL_SOUNDS
        for slider in self.sliders.keys():
            slider.valueChanged.connect(self.update_signal)

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
        # spectro1_widget = pg.PlotWidget()
        # spectro2_widget = pg.PlotWidget()

        # Set the background color
        # spectro1_widget.setBackground('#1e1d23')
        # spectro2_widget.setBackground('#1e1d23')

        # Show grid
        # spectro1_widget.showGrid(x=True, y=True)
        # spectro2_widget.showGrid(x=True, y=True)
        self.original_spectrogram = SpectrogramWidget()
        self.modified_spectrogram = SpectrogramWidget()

        # Add the plot widgets to the respective layouts
        self.ui.spectro1_widget.layout().addWidget(self.original_spectrogram)
        self.ui.spectro2_widget.layout().addWidget(self.modified_spectrogram)

        # Plot some data for spectro1
        # x3 = [1, 2, 3, 4, 5]
        # y3 = [15, 25, 35, 45, 55]
        # spectro1_widget.plot(x3, y3)

        # Plot some data for spectro2
        # x4 = [1, 2, 3, 4, 5]
        # y4 = [55, 45, 35, 25, 15]
        # spectro2_widget.plot(x4, y4)
        self.ui.spectrogram_checkbox.stateChanged.connect(
            lambda state: self.show_hide_layout(self.ui.spectrograph_layout, state))
        self.show_hide_layout(self.ui.spectrograph_layout, False)

        # Add layouts to the combo box
        self.ui.modes_combo.addItem("Animal")
        self.ui.modes_combo.addItem("Music")
        self.ui.modes_combo.addItem("ECG")
        self.ui.modes_combo.addItem("Uniform")

        # Connect combo box selection change to a function
        self.ui.modes_combo.currentIndexChanged.connect(lambda index: self.show_selected_layout(index))
        self.show_selected_layout(0)

        self.ui.browse_btn.clicked.connect(self.load_file)

        self.signal = Signal()

    def show_selected_layout(self, index):
        # Hide all layouts
        self.show_hide_widget(self.ui.animal_widget, False)
        self.show_hide_widget(self.ui.music_widget, False)
        self.show_hide_widget(self.ui.ECG_widget, False)
        self.show_hide_widget(self.ui.uniform_widget, False)

        # Show the selected layout
        if index == 0:
            self.show_hide_widget(self.ui.animal_widget, True)
            self.current_mode = Mode.ANIMAL_SOUNDS
        elif index == 1:
            self.show_hide_widget(self.ui.music_widget, True)
            self.current_mode = Mode.MUSICAL_INSTRUMENTS
        elif index == 2:
            self.show_hide_widget(self.ui.ECG_widget, True)
            self.current_mode = Mode.ECG
        elif index == 3:
            self.show_hide_widget(self.ui.uniform_widget, True)
            self.current_mode = Mode.UNIFORM

    def show_hide_widget(self, layout: QWidget, state):
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

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.mp3 *.flac)")
        try:
            self.signal = Signal.from_file(file_path)
            self.update_spectrogram()
        except Exception as e:
            QErrorMessage(self).showMessage(f"An error occurred while loading the file: {e}")

    def update_spectrogram(self):
        self.original_spectrogram.plot_spectrogram(self.signal.original_data,
                                                   self.signal.sample_rate,
                                                   "Original Signal")
        self.modified_spectrogram.plot_spectrogram(self.signal.get_modified_data(),
                                                   self.signal.sample_rate,
                                                   "Modified Signal")

    def update_signal(self):
        if self.signal.original_data is None:
            return

        slider_values = self.get_slider_values()

        if self.current_mode == Mode.UNIFORM:
            self.signal.equalize_uniform(slider_values)
        else:
            if self.current_mode == Mode.ANIMAL_SOUNDS:
                relevant_sounds = ["Dog", "Cat", "Bird", "Lion"]
            elif self.current_mode == Mode.MUSICAL_INSTRUMENTS:
                relevant_sounds = ["Piano", "Guitar", "Violin", "Bass Drums"]
            elif self.current_mode == Mode.ECG:
                relevant_sounds = ["Normal ECG", "Atrial Fibrillation", "Ventricular Fibrillation", "Tachycardia"]

            frequency_ranges = {sound: self.frequencies[sound] for sound in relevant_sounds}

            self.signal.equalize(slider_values, frequency_ranges)

        self.update_spectrogram()

    def get_slider_values(self):
        relevant_sliders = self.sliders.keys()

        # filter sliders based on mode selected
        if self.current_mode == Mode.UNIFORM:
            relevant_sliders = [slider for slider in relevant_sliders if slider.objectName().startswith("uniform")]
        elif self.current_mode == Mode.ANIMAL_SOUNDS:
            relevant_sliders = [slider for slider in relevant_sliders if slider.objectName().startswith("animal")]
        elif self.current_mode == Mode.MUSICAL_INSTRUMENTS:
            relevant_sliders = [slider for slider in relevant_sliders if slider.objectName().startswith("music")]
        elif self.current_mode == Mode.ECG:
            relevant_sliders = [slider for slider in relevant_sliders if slider.objectName().startswith("ecg")]

        return {sound: slider.value() / 50 for slider, sound in self.sliders.items() if slider in relevant_sliders}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
