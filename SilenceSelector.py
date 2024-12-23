from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl


class SilenceSelector(QDialog):
    def __init__(self, signal, parent=None):
        super().__init__(parent)
        self.signal = signal
        if self.signal.sample_rate is None:
            self.signal.sample_rate = 44100

        self.setWindowTitle("Select Silence Region")
        self.resize(800, 400)

        layout = QVBoxLayout(self)

        self.plot_widget = pg.PlotWidget()
        self.plot_item = self.plot_widget.getPlotItem()
        self.plot_item.showGrid(x=True, y=True)
        layout.addWidget(self.plot_widget)

        self.playback_line = pg.InfiniteLine(pos=0, movable=False, pen='r')
        self.plot_item.addItem(self.playback_line)

        self.start_region = pg.InfiniteLine(pos=0, movable=True,
                                            label='Start', labelOpts={'color': 'g'},
                                            pen=pg.mkPen('g', width=2))
        self.end_region = pg.InfiniteLine(pos=5, movable=True,
                                          label='End', labelOpts={'color': 'r'},
                                          pen=pg.mkPen('r', width=2))
        self.plot_item.addItem(self.start_region)
        self.plot_item.addItem(self.end_region)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        controls_layout = QHBoxLayout()

        self.prev_btn = QPushButton("Previous 5s")
        self.play_btn = QPushButton("Play")
        self.next_btn = QPushButton("Next 5s")
        self.confirm_btn = QPushButton("Confirm Selection")

        marker_controls = QHBoxLayout()
        self.center_start_btn = QPushButton("Center Start")
        self.center_end_btn = QPushButton("Center End")
        marker_controls.addWidget(self.center_start_btn)
        marker_controls.addWidget(self.center_end_btn)

        controls_layout.addWidget(self.prev_btn)
        controls_layout.addWidget(self.play_btn)
        controls_layout.addWidget(self.next_btn)
        controls_layout.addWidget(self.confirm_btn)

        layout.addLayout(controls_layout)
        layout.addLayout(marker_controls)

        self.time_label = QLabel("0:00 - 5:00")
        layout.addWidget(self.time_label)

        # Connect signals
        self.prev_btn.clicked.connect(self.show_previous)
        self.next_btn.clicked.connect(self.show_next)
        self.play_btn.clicked.connect(self.toggle_playback)
        self.confirm_btn.clicked.connect(self.accept)
        self.center_start_btn.clicked.connect(lambda: self.center_marker(self.start_region))
        self.center_end_btn.clicked.connect(lambda: self.center_marker(self.end_region))
        self.start_region.sigPositionChanged.connect(self.stop_playback)
        self.end_region.sigPositionChanged.connect(self.stop_playback)

        # Setup playback timer
        self.playback_timer = QTimer()
        self.playback_timer.setInterval(50)  # 50ms update interval
        self.playback_timer.timeout.connect(self.update_playback_line)
        self.player.playbackStateChanged.connect(self.handle_play_back_state)

        self.current_start = 0
        self.window_size = 5
        self.create_temp_audio()
        self.update_view()
        self.playback_start_time = 0

        # Ensure the dialog stops playback on close
        self.finished.connect(self.stop_playback)

    def handle_play_back_state(self, state):
        if state == QMediaPlayer.PlayingState:
            self.playback_timer.start()
            self.playback_start_time = self.start_region.value()
            self.play_btn.setText("Stop")
        else:
            self.playback_timer.stop()
            # self.playback_line.setPos(self.start_region.value())
            self.play_btn.setText("Play")

    def toggle_playback(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.stop()
        else:
            self.play_current_segment()

    def stop_playback(self):
        self.player.stop()
        self.play_btn.setText("Play")

    def update_playback_line(self):
        if self.player.position() >= 0:
            relative_pos = self.playback_start_time + (self.player.position() / 1000.0)
            self.playback_line.setPos(relative_pos)

    def update_view(self):
        if self.signal.original_data is None:
            return

        start_idx = int(self.current_start * self.signal.sample_rate)
        end_idx = min(int((self.current_start + self.window_size) * self.signal.sample_rate),
                      len(self.signal.original_data))

        self.plot_item.clear()
        time = np.arange(start_idx, end_idx) / self.signal.sample_rate
        self.plot_item.plot(time, self.signal.original_data[start_idx:end_idx])

        self.plot_item.addItem(self.playback_line)
        self.plot_item.addItem(self.start_region)
        self.plot_item.addItem(self.end_region)

        self.plot_widget.setXRange(self.current_start, self.current_start + self.window_size)
        self.plot_item.setLimits(xMin=self.current_start, xMax=self.current_start + self.window_size)

        start_time = f"{int(self.current_start // 60)}:{int(self.current_start % 60):02d}"
        end_time = f"{int((self.current_start + self.window_size) // 60)}:{int((self.current_start + self.window_size) % 60):02d}"
        self.time_label.setText(f"{start_time} - {end_time}")

    def center_marker(self, marker):
        center_time = self.current_start + (self.window_size / 2)
        marker.setValue(center_time)
        self.update_selection()

    def create_temp_audio(self):
        self.temp_dir = tempfile.gettempdir()
        self.temp_file = os.path.join(self.temp_dir, "temp_segment.wav")

    def show_previous(self):
        if self.current_start >= self.window_size:
            self.current_start -= self.window_size
            self.update_view()

    def show_next(self):
        max_start = len(self.signal.original_data) / self.signal.sample_rate - self.window_size
        if self.current_start < max_start:
            self.current_start += self.window_size
            self.update_view()

    def play_current_segment(self):
        start_time = self.start_region.value()
        end_time = self.end_region.value()

        start_idx = int(start_time * self.signal.sample_rate)
        end_idx = int(end_time * self.signal.sample_rate)

        segment = self.signal.original_data[start_idx:end_idx]
        write(self.temp_file, self.signal.sample_rate, segment)

        self.player.setSource(QUrl.fromLocalFile(self.temp_file))
        self.player.play()

    def update_selection(self):
        start_time = self.start_region.value()
        end_time = self.end_region.value()

        if start_time < self.current_start:
            self.start_region.setValue(self.current_start)
        if end_time > self.current_start + self.window_size:
            self.end_region.setValue(self.current_start + self.window_size)

    def get_selection(self):
        return (int(self.start_region.value() * 1000),
                int(self.end_region.value() * 1000))
