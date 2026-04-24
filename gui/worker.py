from PySide6.QtCore import QObject, Slot, QUrl, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from pathlib import Path

class AudioWorker(QObject):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.timer = None
        self.bpm = 60
        # Use absolute path for audio file
        self.audio_file = str(Path(__file__).parent / "config/metronome_click.wav")

    @Slot(int)
    def play_file(self, bpm):
        self.bpm = bpm
        interval = int(60_000 / int(bpm))  # Convert BPM to milliseconds
        
        # Stop existing timer if running
        if self.timer is not None:
            self.timer.stop()
        
        # Create timer in the worker's thread
        self.timer = QTimer()
        self.timer.timeout.connect(self.play_click)
        self.timer.start(interval)

    def play_click(self):
        self.player.setSource(QUrl.fromLocalFile(self.audio_file))
        self.player.play()

    @Slot()
    def stop(self):
        if self.timer is not None:
            self.timer.stop()
            self.timer.deleteLater()
            self.timer = None
        self.player.stop()
