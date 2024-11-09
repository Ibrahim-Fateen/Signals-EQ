import sys
import numpy as np
import librosa
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QSlider, QLabel,
                             QWidget, QPushButton, QComboBox, QFileDialog)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QMediaPlayerWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class SpectrogramWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.ax = self.canvas.figure.subplots()
        self.colorbar = None

    def plot_spectrogram(self, data, sample_rate, title="Spectrogram"):
        try:
            self.ax.clear()
            n_fft = 1024
            hop_length = 512
            S = np.abs(librosa.stft(data, n_fft=n_fft, hop_length=hop_length)) ** 2
            S_db = librosa.power_to_db(S, ref=np.max)

            img = librosa.display.specshow(S_db, sr=sample_rate, hop_length=hop_length,
                                           x_axis='time', y_axis='log', ax=self.ax, cmap='viridis')
            self.ax.set_title(title)
            self.ax.set_xlabel("Time (s)")
            self.ax.set_ylabel("Frequency (Hz)")

            if self.colorbar is None:
                self.colorbar = self.canvas.figure.colorbar(img, ax=self.ax, format="%+2.0f dB")
            else:
                self.colorbar.update_normal(img)

            self.canvas.draw()
        except Exception as e:
            print(f"An error occurred while plotting the spectrogram: {e}")

    def apply_slider_values(self, data, slider_values, sample_rate):
        fft_data = np.fft.rfft(data)
        frequencies = np.fft.rfftfreq(len(data), d=1 / sample_rate)

        num_bands = len(slider_values)

        for i, slider_value in enumerate(slider_values):
            band_start = int(i * len(frequencies) / num_bands)
            band_end = int((i + 1) * len(frequencies) / num_bands)
            fft_data[band_start:band_end] *= slider_value

        adjusted_data = np.fft.irfft(fft_data)
        return adjusted_data

    def update_spectrogram(self, data, sample_rate, slider_values):
        adjusted_data = self.apply_slider_values(data, slider_values, sample_rate)
        self.ax.clear()

        n_fft = 1024
        hop_length = 512
        S = np.abs(librosa.stft(adjusted_data, n_fft=n_fft, hop_length=hop_length)) ** 2
        S_db = librosa.power_to_db(S, ref=np.max)

        img = librosa.display.specshow(S_db, sr=sample_rate, hop_length=hop_length,
                                       x_axis='time', y_axis='log', ax=self.ax, cmap='viridis')
        self.ax.set_title("Adjusted Spectrogram")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Frequency (Hz)")

        if self.colorbar is None:
            self.colorbar = self.canvas.figure.colorbar(img, ax=self.ax, format="%+2.0f dB")
        else:
            self.colorbar.update_normal(img)

        self.canvas.draw_idle()

class SignalEqualizerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal Equalizer")
        self.resize(800, 600)

        main_layout = QVBoxLayout(self)
        self.spectrogram_widget = SpectrogramWidget()
        main_layout.addWidget(self.spectrogram_widget)

        self.slider_values = [1.0] * 10
        sliders_layout = QHBoxLayout()
        self.sliders = []

        for i in range(10):
            slider = QSlider(Qt.Orientation.Vertical)
            slider.setMinimum(0)
            slider.setMaximum(200)
            slider.setValue(100)
            slider.setTickPosition(QSlider.TickPosition.TicksBelow)
            slider.setTickInterval(50)
            slider.valueChanged.connect(self.update_slider_values)

            label = QLabel(f"Band {i + 1}")
            band_layout = QVBoxLayout()
            band_layout.addWidget(slider)
            band_layout.addWidget(label)

            sliders_layout.addLayout(band_layout)
            self.sliders.append(slider)

        main_layout.addLayout(sliders_layout)

        control_layout = QHBoxLayout()
        load_button = QPushButton("Load Signal")
        load_button.clicked.connect(self.load_audio_file)  # load_audio_file method to load audio
        control_layout.addWidget(load_button)

        self.mode_selector = QComboBox()
        self.mode_selector.addItems(
            ["Uniform Range Mode", "Musical Instruments Mode", "Animal Sounds Mode", "ECG Abnormalities Mode"])
        control_layout.addWidget(self.mode_selector)

        # Audio Player Controls
        self.play_button = QPushButton("Play Audio")
        self.play_button.clicked.connect(self.toggle_playback)
        control_layout.addWidget(self.play_button)

        main_layout.addLayout(control_layout)

        # Audio player setup
        self.player = QMediaPlayer(self)
        self.audio_file = None  # To hold the loaded audio file
        self.player.setVolume(50)  # Set volume to 100%

        self.data = None
        self.sample_rate = 44100

    def load_audio_file(self):
        try:
            # Open a file dialog to select an audio file
            file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.mp3 *.flac)")

            if file_path:
                # Load the audio file using librosa
                self.data, self.sample_rate = librosa.load(file_path, sr=None)

                # Plot the spectrogram of the loaded audio
                self.spectrogram_widget.plot_spectrogram(self.data, self.sample_rate, title="Audio File Spectrogram")

                # Set the QMediaContent and play the audio
                audio_url = QUrl.fromLocalFile(file_path)  # Convert the file path to a QUrl
                media_content = QMediaContent(audio_url)
                self.player.setMedia(media_content)
                self.player.play()  # Play the audio file
        except Exception as e:
            print(f"An error occurred while loading the audio file: {e}")


    def toggle_playback(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()  # Pause if it's already playing
            self.play_button.setText("Play Audio")
        else:
            self.player.play()  # Play the audio
            self.play_button.setText("Pause Audio")

    # Connect sliders to update_spectrogram with each adjustment
    def update_slider_values(self):
        if self.data is None:
            return

        # Update slider values list based on slider positions
        self.slider_values = [slider.value() / 10 for slider in self.sliders]  # Scale slider range (0-10)

        # Debugging: Print the slider values to verify changes
        print("Slider Values:", self.slider_values)

        # Update spectrogram based on new slider values
        self.spectrogram_widget.update_spectrogram(self.data, self.sample_rate, self.slider_values)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        window = SignalEqualizerUI()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"An error occurred: {e}")
