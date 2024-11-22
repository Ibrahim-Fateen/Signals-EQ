import numpy as np
import librosa
from scipy.fft import fft, fftfreq, ifft
from DynamicSignal import DynamicSignal
import pandas as pd


class Signal(DynamicSignal):
    def __init__(self, data_pnts=None, label=None, color=None, is_normalized=False):
        super().__init__(data_pnts, label, color, is_normalized)
        self.sample_rate = None
        self.original_data = None
        self.plotting_timespace = None
        self.original_spectrum = None
        self.frequencies = None
        self.modified_spectrum = None
        self.modified_data = None
        self.modified = False
        self.modified_data_pnts = None

    def equalize(self, slider_values, frequency_ranges_dict):
        """
        Apply equalization with handling for overlapping frequency ranges.

        Args:
            slider_values: Dictionary mapping sound names to their slider values (0-100)
            frequency_ranges_dict: Dictionary mapping sound names to their frequency ranges
        """
        gain_array = np.ones_like(self.frequencies, dtype=float)

        for sound_name, ranges in frequency_ranges_dict.items():
            db_gain = slider_values[sound_name]
            linear_gain = 10 ** (db_gain / 20)

            if not isinstance(ranges, list):
                ranges = [ranges]

            for freq_range in ranges:
                start, end = freq_range

                pos_mask = (self.frequencies >= start) & (self.frequencies <= end)
                neg_mask = (self.frequencies >= -end) & (self.frequencies <= -start)

                gain_array[pos_mask] *= linear_gain
                gain_array[neg_mask] *= linear_gain

        # Apply the combined gain to the spectrum
        self.modified_spectrum = self.original_spectrum * gain_array
        self.modified = True
        # self.get_modified_data()

    def equalize_uniform(self, slider_values):
        """
        Apply equalization to the signal based on 10 sliders with uniform frequency ranges.
        Calls equalize() with appropriate frequency ranges for each slider.

        Args:
            slider_values: Dictionary mapping sound names to their slider values (0-100)
        """
        # Define frequency ranges for each slider
        maximum_frequency = self.get_maximum_frequency()
        num_sliders = len(slider_values)
        slider_width = maximum_frequency / num_sliders
        frequency_ranges = [(i * slider_width, (i + 1) * slider_width) for i in range(num_sliders)]
        self.equalize(slider_values, {f"Uniform {i + 1}": freq_range for i, freq_range in enumerate(frequency_ranges)})
        self.modified = True

    def get_modified_data(self):
        if self.modified:
            self.modified_data = ifft(self.modified_spectrum).real
            self.modified_data_pnts = [(i, y) for i, y in enumerate(self.modified_data)]
            self.modified = False
        return self.modified_data

    def get_maximum_frequency(self):
        """
        Gets the maximum significant frequency present in the signal.
        Uses the magnitude spectrum to determine where the signal content becomes negligible.

        Returns:
            float: The maximum significant frequency in Hz
        """
        # Get the magnitude spectrum (absolute values)
        magnitude_spectrum = np.abs(self.original_spectrum)

        noise_threshold = 0.05  # 5% of maximum magnitude
        noise_floor = np.max(magnitude_spectrum) * noise_threshold

        positive_freqs = self.frequencies[:len(self.frequencies) // 2]
        positive_magnitudes = magnitude_spectrum[:len(self.frequencies) // 2]

        significant_freq_indices = np.where(positive_magnitudes > noise_floor)[0]

        if len(significant_freq_indices) == 0:
            return self.sampling_rate / 2  # Return Nyquist frequency if no significant frequencies found

        max_significant_freq = positive_freqs[significant_freq_indices[-1]]

        # max_significant_freq = np.ceil(max_significant_freq / 1000) * 1000

        return max_significant_freq

    @staticmethod
    def load_signal_from_file(file_path):
        try:
            signal = Signal()
            data, sample_rate = librosa.load(file_path)
            signal.sample_rate = sample_rate
            signal.original_data = data
            signal.plotting_timespace = np.arange(len(data)) / sample_rate
            signal.original_spectrum = fft(data)
            signal.frequencies = fftfreq(len(data), 1 / sample_rate)
            signal.modified_spectrum = signal.original_spectrum.copy()
            signal.modified_data = data
            signal.data_pnts = signal.convert_to_data_pnts()
            signal.modified_data_pnts = signal.data_pnts.copy()
            signal.label = file_path.split("/")[-1]
            signal.color = "blue"
            signal.ID = file_path
            return signal
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    @staticmethod
    def load_signal_from_csv(file_path):
        try:
            signal = Signal()
            df = pd.read_csv(file_path)
            if df.shape[1] == 1:
                return Signal.load_signal_from_csv_y_only(file_path)
            elif df.shape[1] != 2:
                raise ValueError("CSV file must have exactly two columns: time and amplitude.")
            time = df.iloc[:, 0].values
            data = df.iloc[:, 1].values
            sample_rate = 1 / np.mean(np.diff(time)) * 1000
            signal.sample_rate = sample_rate
            signal.original_data = data
            signal.plotting_timespace = time
            signal.original_spectrum = fft(data)
            signal.frequencies = fftfreq(len(data), 1 / sample_rate)
            signal.modified_spectrum = signal.original_spectrum.copy()
            signal.modified_data = data
            signal.data_pnts = signal.convert_to_data_pnts()
            signal.modified_data_pnts = signal.data_pnts.copy()
            signal.label = file_path.split("/")[-1]
            signal.color = "blue"
            signal.ID = file_path
            return signal
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")

    @staticmethod
    def load_signal_from_csv_y_only(file_path, sample_rate=100):
        try:
            signal = Signal()
            df = pd.read_csv(file_path)
            if df.shape[1] != 1:
                raise ValueError("CSV file must have exactly one column: amplitude.")
            data = df.iloc[:, 0].values.astype(float)
            
            # Normalize data to be between -10 and 10
            data_min = np.min(data)
            data_max = np.max(data)
            data = 2 * (data - data_min) / (data_max - data_min) - 1
            
            signal.sample_rate = sample_rate
            signal.original_data = data
            signal.plotting_timespace = np.arange(len(data)) / sample_rate
            signal.original_spectrum = fft(data)
            signal.frequencies = fftfreq(len(data), 1 / sample_rate)
            signal.modified_spectrum = signal.original_spectrum.copy()
            signal.modified_data = data
            signal.data_pnts = signal.convert_to_data_pnts()
            signal.modified_data_pnts = signal.data_pnts.copy()
            signal.label = file_path.split("/")[-1]
            signal.color = "blue"
            signal.ID = file_path
            return signal
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")

    def convert_to_data_pnts(self):
        data_pnts = [(i, y) for i, y in enumerate(self.original_data)]
        return data_pnts
