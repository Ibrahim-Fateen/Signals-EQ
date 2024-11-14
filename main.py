from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QErrorMessage, QPushButton, QWidget, QSlider, \
    QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QCheckBox
import sys
from PySide6.QtWidgets import QWidget
from enum import Enum
from Graph import Graph
from main_window import Ui_MainWindow
from Spectrogram import SpectrogramWidget
from Signal import Signal
from copy import deepcopy
from AudioPlayer import AudioPlayer
import tempfile
import os
from scipy.io.wavfile import write


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
        self.modified_audio_path = None
        self.graph1 = Graph()
        self.graph2 = Graph()

        self.frequencies = {
            # Animals
            "Owl": [(100, 500)],
            "Turkey": [(500, 1200)],
            "Frog": [(1000, 2500)],
            "Bird": [(2000, 8000)],

            # Musical Instruments
            "Oud": [(140, 300)],
            "Nay": [(450, 8000)],
            "Violin": [(300, 600)],
            "Drums": [(20, 170)],

            # ECG
            "Normal": [(0.5, 3), (10, 40)],
            "Atrial Fibrillation": [(3, 7)],
            "Ventricular Tachycardia": [(1.5, 4), (40, 200)],
            "Ventricular Flutter": [(4, 6), (20, 40)],
        }

        self.sliders = {
            self.ui.animal_slider1: "Frog",
            self.ui.animal_slider2: "Owl",
            self.ui.animal_slider3: "Bird",
            self.ui.animal_slider4: "Turkey",
            self.ui.music_slider1: "Oud",
            self.ui.music_slider2: "Nay",
            self.ui.music_slider3: "Violin",
            self.ui.music_slider4: "Drums",
            self.ui.ECG_slider1: "Normal",
            self.ui.ECG_slider2: "Atrial Fibrillation",
            self.ui.ECG_slider3: "Ventricular Tachycardia",
            self.ui.ECG_slider4: "Ventricular Flutter",
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

        for slider in self.sliders.keys():
            slider.setOrientation(Qt.Vertical)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setTickPosition(QSlider.TicksLeft)
            slider.setTickInterval(5)
            slider.setValue(50)

            # Create a layout to hold the slider and labels
            slider_layout = QHBoxLayout()

            # Add labels for each tick position
            labels_layout = QVBoxLayout()
            labels_layout.addWidget(QLabel("+50 dB"))
            labels_layout.addStretch()
            labels_layout.addWidget(QLabel("+25 dB"))
            labels_layout.addStretch()
            labels_layout.addWidget(QLabel("0 dB"))
            labels_layout.addStretch()
            labels_layout.addWidget(QLabel("-25 dB"))
            labels_layout.addStretch()
            labels_layout.addWidget(QLabel("-50 dB"))

            # Add slider and labels layout side by side
            slider_layout.addLayout(labels_layout)
            slider_layout.addWidget(slider)

            # Add slider layout to the parent layout
            parent_layout = slider.parent().layout()
            parent_layout.addLayout(slider_layout)

        self.ui.animal_label1.setPixmap(QPixmap(u"icons/dog.png"))
        self.ui.animal_label1.setText("Frog")
        self.ui.animal_label2.setPixmap(QPixmap(u"icons/wolf.png"))
        self.ui.animal_label2.setText("Owl")
        self.ui.animal_label3.setPixmap(QPixmap(u"icons/bird.png"))
        self.ui.animal_label3.setText("Bird")
        self.ui.animal_label4.setPixmap(QPixmap(u"icons/lion.png"))
        self.ui.animal_label4.setText("Turkey")

        self.ui.ECG_label1.setText("Normal ECG")
        self.ui.ECG_label2.setText("Atrial Fibrillation")
        self.ui.ECG_label3.setText("Ventricular Tachycardia")
        self.ui.ECG_label4.setText("Ventricular Flutter")

        self.ui.music_label1.setText("Oud")
        self.ui.music_label2.setText("Nay")
        self.ui.music_label3.setText("Violin")
        self.ui.music_label4.setText("Drums")

        self.ui.uniform_label1.setText("Uniform 1")
        self.ui.uniform_label2.setText("Uniform 2")
        self.ui.uniform_label3.setText("Uniform 3")
        self.ui.uniform_label4.setText("Uniform 4")
        self.ui.uniform_label5.setText("Uniform 5")
        self.ui.uniform_label6.setText("Uniform 6")
        self.ui.uniform_label7.setText("Uniform 7")
        self.ui.uniform_label8.setText("Uniform 8")
        self.ui.uniform_label9.setText("Uniform 9")
        self.ui.uniform_label10.setText("Uniform 10")

        for slider in self.sliders.keys():
            slider.setValue(slider.maximum() // 2)
        self.current_mode = Mode.ANIMAL_SOUNDS
        for slider in self.sliders.keys():
            slider.sliderReleased.connect(self.update_signal)

        # Add the plot widget to the layout
        self.ui.graph2_widget.layout().addWidget(self.graph1)
        self.ui.graph1_widget.layout().addWidget(self.graph2)

        self.original_spectrogram = SpectrogramWidget()
        self.modified_spectrogram = SpectrogramWidget()

        # Add the plot widgets to the respective layouts
        self.ui.spectro1_widget.layout().addWidget(self.original_spectrogram)
        self.ui.spectro2_widget.layout().addWidget(self.modified_spectrogram)
        self.ui.spectro1_widget.layout().setContentsMargins(0, 0, 0, 0)
        self.ui.spectro2_widget.layout().setContentsMargins(0, 0, 0, 0)

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
        self.connect_graph_controls()
        original_stop_btn = QPushButton("")
        stop_icon = QIcon()
        stop_icon.addFile(u"icons/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        original_stop_btn.setIcon(stop_icon)

        self.ui.horizontalLayout.addWidget(original_stop_btn)
        #change its order 
        self.original_audio = AudioPlayer(self.ui.aduio1_play_btn, self.ui.audio1_slider, self.ui.audio1_replay_btn, self.ui.audio1_time_label, original_stop_btn)
        modified_stop_btn = QPushButton("")
        modified_stop_btn.setIcon(stop_icon)
        self.ui.horizontalLayout_2.addWidget(modified_stop_btn)
        self.modified_audio = AudioPlayer(self.ui.audio2_play_btn, self.ui.audio2_slider, self.ui.audio2_replay_btn, self.ui.audio2_time_label, modified_stop_btn)
        self.log_scale_checkbox = QCheckBox("Use Audiogram Scale")
        self.log_scale_checkbox.setMaximumWidth(200)
        self.ui.verticalLayout_20.addWidget(self.log_scale_checkbox)
        self.log_scale_checkbox.stateChanged.connect(lambda state: self.update_spectrogram())

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
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Signal File", "", "Audio Files (*.wav *.mp3 *.flac *.csv)")
        #clear the previous signal
        self.signal = Signal()
        self.graph1.plots = []
        self.graph2.plots = []
        self.graph1.plot_to_track = None
        self.graph2.plot_to_track = None
        self.graph1.plot_widget.clear()
        self.graph2.plot_widget.clear()

        try:
            if not file_path.endswith(".csv"):
                self.signal = Signal.load_signal_from_file(file_path)
            else:
                self.signal = Signal.load_signal_from_csv(file_path)

            self.update_spectrogram()
            non_modified_signal = deepcopy(self.signal)
            self.graph1.plot_signal(self.signal)
            self.graph2.plot_signal(non_modified_signal)
            self.graph1.change_speed(10)
            self.graph2.change_speed(10)
            is_audio = not file_path.endswith(".csv")
            if is_audio:
                self.original_audio.set_audio_file(file_path)
                self.modified_audio_path = self.save_modified_audio_to_temp()
                self.modified_audio.set_audio_file(self.modified_audio_path)
            else:
                self.original_audio.remove_audio_file()
                self.modified_audio.remove_audio_file()
                self.modified_audio_path = None

            self.original_audio.slider.setDisabled(not is_audio)
            self.original_audio.play_button.setDisabled(not is_audio)
            self.original_audio.replay_button.setDisabled(not is_audio)
            self.original_audio.stop_button.setDisabled(not is_audio)
            self.modified_audio.slider.setDisabled(not is_audio)
            self.modified_audio.play_button.setDisabled(not is_audio)
            self.modified_audio.replay_button.setDisabled(not is_audio)
            self.modified_audio.stop_button.setDisabled(not is_audio)

        except Exception as e:
            QErrorMessage(self).showMessage(f"An error occurred while loading the file: {e}")

    def update_spectrogram(self):
        scale = 'audiogram' if self.log_scale_checkbox.isChecked() else 'linear'

        self.original_spectrogram.plot_spectrogram(self.signal.original_data,
                                                   self.signal.sample_rate,
                                                   "Original Signal", scale)
        self.modified_spectrogram.plot_spectrogram(self.signal.get_modified_data(),
                                                   self.signal.sample_rate,
                                                   "Modified Signal", scale)

    def save_modified_audio_to_temp(self):
        temp_dir = tempfile.gettempdir()
        temp_file_path = os.path.join(temp_dir, "modified_audio.wav")
        write(temp_file_path, self.signal.sample_rate, self.signal.get_modified_data())
        return temp_file_path

    def update_modified_audio(self):
        write(self.modified_audio_path, self.signal.sample_rate, self.signal.get_modified_data())
        self.modified_audio.remove_audio_file()
        self.modified_audio.set_audio_file(self.modified_audio_path)

    def update_signal(self):
        if self.signal.original_data is None:
            return

        slider_values = self.get_slider_values()

        if self.current_mode == Mode.UNIFORM:
            self.signal.equalize_uniform(slider_values)
        else:
            if self.current_mode == Mode.ANIMAL_SOUNDS:
                relevant_sounds = ["Frog", "Owl", "Bird", "Turkey"]
            elif self.current_mode == Mode.MUSICAL_INSTRUMENTS:
                relevant_sounds = ["Oud", "Nay", "Violin", "Drums"]
            elif self.current_mode == Mode.ECG:
                relevant_sounds = ["Normal", "Atrial Fibrillation", "Ventricular Tachycardia", "Ventricular Flutter"]

            frequency_ranges = {sound: self.frequencies[sound] for sound in relevant_sounds}

            self.signal.equalize(slider_values, frequency_ranges)

        self.update_spectrogram()
        if self.modified_audio_path:
            self.update_modified_audio()
        
        plot = self.graph1.plot_to_track
        plot.signal.data_pnts = self.signal.modified_data_pnts
        plot.plot.setData([point[0] for point in plot.signal.data_pnts[:plot.last_point]],
                          [point[1] for point in plot.signal.data_pnts[:plot.last_point]])

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
            relevant_sliders = [slider for slider in relevant_sliders if slider.objectName().startswith("ECG")]

        return {sound: slider.value() for slider, sound in self.sliders.items() if slider in relevant_sliders}

    def connect_graph_controls(self):
        #zooming and panning for both graphs
        self.graph1.custom_viewbox.setXLink(self.graph2.custom_viewbox)
        self.graph1.custom_viewbox.setYLink(self.graph2.custom_viewbox)
        def set_user_panning(flag : bool):
            self.graph1.custom_viewbox.is_user_panning = flag
            self.graph2.custom_viewbox.is_user_panning = flag
            self.graph1.custom_viewbox.elapsed_timer.start()
            self.graph2.custom_viewbox.elapsed_timer.start()

        self.graph1.custom_viewbox.user_panning_action = set_user_panning
        self.graph2.custom_viewbox.user_panning_action = set_user_panning
        def update_y_range():
            min_y = min(self.graph1.min_Y, self.graph2.min_Y)
            max_y = max(self.graph1.max_Y, self.graph2.max_Y)
            self.graph1.plot_widget.setYRange(min_y, max_y)
            self.graph2.plot_widget.setYRange(min_y, max_y)
        self.graph1.update_y_range = update_y_range
        self.graph2.update_y_range = update_y_range

        self.ui.graph_play_btn.clicked.connect(lambda:{
            self.graph1.play_pause(),
            self.graph2.play_pause(),
            self.ui.graph_play_btn.setIcon(QIcon(u"icons/pause.png")) if self.graph1.plot_to_track and self.graph1.plot_to_track.isRunning else self.ui.graph_play_btn.setIcon(QIcon(u"icons/play.png"))
        })
        self.ui.speed_slider.valueChanged.connect(lambda value: {
            self.graph1.change_speed(value),
            self.graph2.change_speed(value)
        })
        self.ui.zoomin_btn.clicked.connect(lambda: {
            self.graph1.x_zoom(-0.05),
            self.graph2.x_zoom(-0.05)
        })
        self.ui.zoomout_btn.clicked.connect(lambda: {
            self.graph1.x_zoom(0.05),
            self.graph2.x_zoom(0.05)
        })
        self.ui.graph_replay_btn.clicked.connect(lambda: {
            self.graph1.rewind(),
            self.graph2.rewind(),
            self.ui.graph_play_btn.setIcon(QIcon(u"icons/play.png"))
        })
        self.ui.speed_slider.setValue(50)
        self.ui.speed_slider.setRange(1, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
