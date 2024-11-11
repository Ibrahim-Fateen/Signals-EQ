from PySide6.QtWidgets import QSlider,  QLabel
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon 
from PySide6.QtCore import QSize

class AudioPlayer:
    def __init__(self, play_button, slider: QSlider, replay_button, time_elapsed_label: QLabel, stop_button):
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.play_button = play_button
        self.slider = slider
        self.slider.sliderMoved.connect(self.set_position)
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.replay_button = replay_button
        self.replay_button.clicked.connect(self.replay)
        self.time_elapsed_label = time_elapsed_label
        self.time_elapsed_label.setText("0:00")
        self.player.positionChanged.connect(self.update_time_elapsed)
        self.stop_button = stop_button
        self.stop_button.clicked.connect(self.stop)
        self.play_button.clicked.connect(self.toggle_play_pause)
        self.pause_icon = QIcon()
        self.pause_icon.addFile(u"icons/pause.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_icon = QIcon()
        self.play_icon.addFile(u"icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.current_position = 0
        self.isRunning = False

        

    def set_audio_file(self, file_name):
        self.player.setSource(QUrl.fromLocalFile(file_name))
        if self.current_position != 0 and self.isRunning:
            self.player.play()
            self.set_position(self.current_position)
            self.update_position(self.current_position)
            self.update_duration(self.player.duration())
            self.update_time_elapsed()
            self.play_button.setIcon(self.pause_icon)

    def remove_audio_file(self):
        self.current_position = self.player.position()
        self.player.setSource(QUrl.fromLocalFile(""))

    def stop(self):
        self.player.stop()
        self.play_button.setIcon(self.play_icon)
        self.isRunning = False

    def toggle_play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play_button.setIcon(self.play_icon)
            self.isRunning = False
        else:
            self.player.play()
            self.play_button.setIcon(self.pause_icon)
            self.isRunning = True

    def set_position(self, position):
        self.player.setPosition(position)
        

    def update_duration(self, duration):
        self.slider.setMaximum(duration)

    def update_position(self, position):
        self.slider.setValue(position)
        

    def replay(self):
        self.player.setPosition(0)
        self.current_position = 0
        self.player.play()
        self.play_button.setIcon(self.pause_icon)
        self.isRunning = True


    def update_time_elapsed(self):
        time = self.player.position() / 1000
        minutes = int(time / 60)
        seconds = int(time % 60)
        time = f"{minutes}:{seconds:02d}"
        self.time_elapsed_label.setText(time)
