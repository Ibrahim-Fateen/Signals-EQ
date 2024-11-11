import librosa
import numpy as np
from PySide6.QtWidgets import (QVBoxLayout, QWidget)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class SpectrogramWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.canvas = FigureCanvas(Figure(figsize=(1, 0.5)))
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.ax = self.canvas.figure.subplots()
        self.colorbar = None
        self.canvas.figure.patch.set_facecolor('#13131F')
        self.canvas.figure.subplots_adjust(left=0.1, right=1) 

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

            # Set the color of the numbers to green
            self.colorbar.ax.yaxis.set_tick_params(color='#04b97f')
            self.colorbar.ax.yaxis.set_ticklabels(self.colorbar.ax.yaxis.get_ticklabels(), color='#04b97f')

            # Set the color of the axes to green
            self.ax.tick_params(axis='x', colors='#04b97f')
            self.ax.tick_params(axis='y', colors='#04b97f')
            self.ax.xaxis.label.set_color('#04b97f')
            self.ax.yaxis.label.set_color('#04b97f')
            self.ax.title.set_color('#04b97f')

            self.canvas.draw()
        except Exception as e:
            print(f"An error occurred while plotting the spectrogram: {e}")

    # def apply_slider_values(self, data, slider_values, sample_rate):
    #     fft_data = np.fft.rfft(data)
    #     frequencies = np.fft.rfftfreq(len(data), d=1 / sample_rate)
    #
    #     num_bands = len(slider_values)
    #
    #     for i, slider_value in enumerate(slider_values):
    #         band_start = int(i * len(frequencies) / num_bands)
    #         band_end = int((i + 1) * len(frequencies) / num_bands)
    #         fft_data[band_start:band_end] *= slider_value
    #
    #     adjusted_data = np.fft.irfft(fft_data)
    #     return adjusted_data

    # def update_spectrogram(self, data, sample_rate, slider_values):
    #     adjusted_data = self.apply_slider_values(data, slider_values, sample_rate)
    #     self.ax.clear()
    #
    #     n_fft = 1024
    #     hop_length = 512
    #     S = np.abs(librosa.stft(adjusted_data, n_fft=n_fft, hop_length=hop_length)) ** 2
    #     S_db = librosa.power_to_db(S, ref=np.max)
    #
    #     img = librosa.display.specshow(S_db, sr=sample_rate, hop_length=hop_length,
    #                                    x_axis='time', y_axis='log', ax=self.ax, cmap='viridis')
    #     self.ax.set_title("Adjusted Spectrogram")
    #     self.ax.set_xlabel("Time (s)")
    #     self.ax.set_ylabel("Frequency (Hz)")
    #
    #     if self.colorbar is None:
    #         self.colorbar = self.canvas.figure.colorbar(img, ax=self.ax, format="%+2.0f dB")
    #     else:
    #         self.colorbar.update_normal(img)
    #
    #     self.canvas.draw_idle()


# class SignalEqualizerUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Signal Equalizer")
#         self.resize(800, 600)
#
#         main_layout = QVBoxLayout(self)
#         self.spectrogram_widget = SpectrogramWidget()  # Assuming SpectrogramWidget is defined elsewhere
#         main_layout.addWidget(self.spectrogram_widget)
#
#         self.slider_values = [1.0] * 10
#         sliders_layout = QHBoxLayout()
#         self.sliders = []
#
#         for i in range(10):
#             slider = QSlider(Qt.Orientation.Vertical)
#             slider.setMinimum(0)
#             slider.setMaximum(200)
#             slider.setValue(100)
#             slider.setTickPosition(QSlider.TickPosition.TicksBelow)
#             slider.setTickInterval(50)
#             slider.valueChanged.connect(self.update_slider_values)
#
#             label = QLabel(f"Band {i + 1}")
#             band_layout = QVBoxLayout()
#             band_layout.addWidget(slider)
#             band_layout.addWidget(label)
#
#             sliders_layout.addLayout(band_layout)
#             self.sliders.append(slider)
#
#         main_layout.addLayout(sliders_layout)
#
#         control_layout = QHBoxLayout()
#         load_button = QPushButton("Load Signal")
#         load_button.clicked.connect(self.load_audio_file)
#         control_layout.addWidget(load_button)
#
#         self.mode_selector = QComboBox()
#         self.mode_selector.addItems(
#             ["Uniform Range Mode", "Musical Instruments Mode", "Animal Sounds Mode", "ECG Abnormalities Mode"])
#         control_layout.addWidget(self.mode_selector)
#
#         # Add the Play Button
#         self.play_button = QPushButton("Play")
#         self.play_button.clicked.connect(self.play_audio)
#         control_layout.addWidget(self.play_button)
#
#         main_layout.addLayout(control_layout)
#
#         # Create the QMediaPlayer to play the audio
#         self.player = QMediaPlayer()
#         self.player.setVolume(100)  # Set volume to 100%
#
#         self.data = None
#         self.sample_rate = 44100
#
#     def load_audio_file(self):
#         try:
#             # Open a file dialog to select an audio file
#             file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.mp3 *.flac)")
#
#             if file_path:
#                 # Load the audio file using librosa
#                 self.data, self.sample_rate = librosa.load(file_path, sr=None)
#
#                 # Plot the spectrogram of the loaded audio
#                 self.spectrogram_widget.plot_spectrogram(self.data, self.sample_rate, title="Audio File Spectrogram")
#
#                 # Set the initial audio for playback
#                 self.update_audio_for_playback()
#
#         except Exception as e:
#             print(f"An error occurred while loading the audio file: {e}")
#
#     def update_slider_values(self):
#         if self.data is None:
#             return
#
#         # Update slider values list based on slider positions
#         self.slider_values = [slider.value() / 10 for slider in self.sliders]  # Scale slider range (0-10)
#
#         # Debugging: Print the slider values to verify changes
#         print("Slider Values:", self.slider_values)
#
#         # Apply equalization (filtering) based on slider values
#         self.apply_equalization()
#
#         # Update spectrogram based on new slider values
#         self.spectrogram_widget.update_spectrogram(self.data, self.sample_rate, self.slider_values)
#
#         # Update the audio for playback with the applied equalization
#         self.update_audio_for_playback()
#
#     def apply_equalization(self):
#         # Apply simple gain control to different frequency bands (this is a placeholder for more complex equalization)
#         num_bands = len(self.slider_values)
#         frequency_bands = np.linspace(20, 20000, num_bands)  # Frequency bands (from 20Hz to 20kHz)
#
#         # For each frequency band, apply a gain factor based on the slider value
#         for i, band in enumerate(frequency_bands):
#             gain_factor = self.slider_values[i]
#             # Apply simple gain control for this band (this could be a more complex filtering operation)
#             self.data = self.apply_band_gain(self.data, band, gain_factor)
#
#     def apply_band_gain(self, data, frequency, gain_factor):
#         # Clip the gain factor to avoid overflow
#         MAX_GAIN = 5.0  # Limit gain to 5 times the original signal
#         gain_factor = np.clip(gain_factor, 0, MAX_GAIN)
#
#         # Apply the gain to the signal
#         data = data * gain_factor
#
#         # Clip the values to avoid overflow: For float32 data, we clip to the range [-1, 1]
#         data = np.clip(data, -1.0, 1.0)
#
#         return data
#
#     def update_audio_for_playback(self):
#         # Create a temporary file path for the modified audio
#         with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
#             try:
#                 # Write the modified audio data to the temporary file
#                 sf.write(tmpfile.name, self.data, self.sample_rate)
#                 print(f"File written to {tmpfile.name}")
#
#                 # Set the QMediaContent for the updated audio
#                 audio_url = QUrl.fromLocalFile(tmpfile.name)  # Convert the file path to a QUrl
#                 media_content = QMediaContent(audio_url)
#                 self.player.setMedia(media_content)
#             except Exception as e:
#                 print(f"Error saving audio file: {e}")
#                 return
#
#     def play_audio(self):
#         if self.data is not None:
#             # Stop any currently playing audio before starting new playback
#             self.player.stop()
#             # Play the audio (this will play the modified audio with the current slider settings)
#             self.player.play()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     try:
#         window = SignalEqualizerUI()
#         window.show()
#         sys.exit(app.exec())
#     except Exception as e:
#         print(f"An error occurred: {e}")
