from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QSlider, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtCore import QThread, Signal

from gui.worker import AudioWorker

import json
from pathlib import Path

def get_markings() -> dict:
    tempo_file = str(Path(__file__).parent / "config/tempos.json")
    new_dict = {}
    with open(tempo_file) as f:
        data = json.load(f)
    for line in data:
        new_dict[line["name"]] = list(range(line["min_bpm"], line["max_bpm"] + 1))
    
    print(new_dict.items())
    return new_dict

class MainWindow(QMainWindow):
    play_signal = Signal(int)
    stop_signal = Signal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meteronome App")
        self.setGeometry(100, 100, 800, 600)
        self.is_playing = False

        self.markings = get_markings()
        
        # Create central widget and layout
        container_widget = QWidget()
        self.setCentralWidget(container_widget)
        layout = QVBoxLayout()
        container_widget.setLayout(layout)
        
        # bpm text
        self.btm_text = QLabel("60")
        self.btm_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.btm_text)
        self.btm_text.setObjectName("tempoDisplay")

        self.marking_text = QLabel("Largo - Lento - Adagio")
        self.marking_text.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        layout.addWidget(self.marking_text)

        # slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(40, 200)
        self.slider.setValue(60)
        self.slider.setTickInterval(1)   
        self.slider.valueChanged.connect(self.on_slider_move)
        layout.addWidget(self.slider)

        # Threading stuff
        self.audio_thread = QThread()
        self.worker = AudioWorker()
        self.worker.moveToThread(self.audio_thread)
        self.audio_thread.start()

        self.play_signal.connect(self.worker.play_file)
        self.stop_signal.connect(self.worker.stop)

        # Play button
        self.play_button = QPushButton("Start")
        self.play_button.clicked.connect(self.toggle_playback)
        layout.addWidget(self.play_button)
        self.play_button.setObjectName("startButton")

    
        

    def on_slider_move(self, value):
        self.btm_text.setText(str(value))

        if self.is_playing:
            self.play_signal.emit(value)
        markings = []
        for marking, tempos in self.markings.items():
            if value in tempos:
                markings.append(marking)
        
        new = " - ".join(markings)
        self.marking_text.setText(new)

    def toggle_playback(self):
        if self.is_playing:
            self.stop_signal.emit()
            self.play_button.setText("Start")
            self.is_playing = False
        else:
            bpm = self.slider.value()
            self.play_signal.emit(bpm)
            self.play_button.setText("Stop")
            self.is_playing = True
        
