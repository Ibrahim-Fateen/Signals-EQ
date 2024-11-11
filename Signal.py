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
        # self.modified_data = None
        self.modified = False
        self.modified_data_pnts = None

    def equalize(self, slider_values, frequency_ranges_dict):
        """
        Apply equalization with handling for overlapping frequency ranges.

        Args:
            slider_values: Dictionary mapping sound names to their slider values (0-2) (0.5 = -6dB, 1 = 0dB, 2 = +6dB)
            frequency_ranges_dict: Dictionary mapping sound names to their frequency ranges
        """
        # Initialize gain array with ones
        gain_array = np.ones_like(self.frequencies, dtype=float)

        # First pass: Calculate the combined gain for each frequency
        for sound_name, ranges in frequency_ranges_dict.items():
            slider_value = slider_values[sound_name]
            if not isinstance(ranges, list):
                ranges = [ranges]

            for freq_range in ranges:
                start, end = freq_range

                # Create masks for positive and negative frequencies
                pos_mask = (self.frequencies >= start) & (self.frequencies <= end)
                neg_mask = (self.frequencies >= -end) & (self.frequencies <= -start)

                # Apply smoother transition at range boundaries using a window function
                pos_window = self.create_smooth_window(self.frequencies[pos_mask], start, end)
                neg_window = self.create_smooth_window(self.frequencies[neg_mask], -end, -start)

                # Combine gains multiplicatively
                gain_array[pos_mask] *= np.power(slider_value, pos_window)
                gain_array[neg_mask] *= np.power(slider_value, neg_window)

        # Apply the combined gain to the spectrum
        self.modified_spectrum = self.original_spectrum * gain_array
        self.modified = True
        # self.get_modified_data()

    def equalize_uniform(self, slider_values):
        """
        Apply equalization to the signal based on 10 sliders with uniform frequency ranges.
        Calls equalize() with appropriate frequency ranges for each slider.

        Args:
            slider_values: Dictionary mapping sound names to their slider values (0-2) (0.5 = -6dB, 1 = 0dB, 2 = +6dB)
        """
        # Define frequency ranges for each slider
        maximum_frequency = self.get_maximum_frequency()
        num_sliders = len(slider_values)
        slider_width = maximum_frequency / num_sliders
        frequency_ranges = [(i * slider_width, (i + 1) * slider_width) for i in range(num_sliders)]
        self.equalize(slider_values, {f"Uniform {i + 1}": freq_range for i, freq_range in enumerate(frequency_ranges)})
        self.modified = True

    def create_smooth_window(self, freq_range, start, end):
        """
        Create a smooth transition window for frequency range boundaries.
        Uses a raised cosine (Hanning) window to prevent sharp transitions.
        """
        width = end - start
        transition_width = min(width * 0.1, 50)  # 10% of width or 50 Hz, whichever is smaller

        window = np.ones_like(freq_range, dtype=float)

        # Apply smooth transition at start
        start_transition = (freq_range >= start) & (freq_range <= start + transition_width)
        if np.any(start_transition):
            window[start_transition] = 0.5 * (
                        1 - np.cos(np.pi * (freq_range[start_transition] - start) / transition_width))

        # Apply smooth transition at end
        end_transition = (freq_range >= end - transition_width) & (freq_range <= end)
        if np.any(end_transition):
            window[end_transition] = 0.5 * (1 + np.cos(
                np.pi * (freq_range[end_transition] - (end - transition_width)) / transition_width))

        return window

    def get_modified_data(self):
        if self.modified:
            self.modified_data = ifft(self.modified_spectrum).real
            self.modified_data_pnts = [(i, y) for i, y in enumerate(self.modified_data)]
            self.modified = False
        return self.modified_data
            

    def get_maximum_frequency(self):
        return np.max(self.frequencies)

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
            signal.color = "red"
            signal.ID = file_path
            return signal
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
    def load_signal_from_csv(file_path):
        try:
            signal = Signal()
            df = pd.read_csv(file_path)
            if df.shape[1] != 2:
                raise ValueError("CSV file must have exactly two columns: time and amplitude.")
            time = df.iloc[:, 0].values
            data = df.iloc[:, 1].values
            sample_rate = 1 / np.mean(np.diff(time))
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
            signal.color = "red"
            signal.ID = file_path
            return signal
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
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
            signal.color = "red"
            signal.ID = file_path
            return signal
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
    def convert_to_data_pnts(self):
        data_pnts = [(i, y) for i, y in enumerate(self.original_data)]
        return data_pnts
