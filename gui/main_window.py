from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QSlider, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meteronome App")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and layout
        container_widget = QWidget()
        self.setCentralWidget(container_widget)
        layout = QVBoxLayout()
        container_widget.setLayout(layout)
        
        # bpm text

        self.btm_text = QLabel("60")
        self.btm_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.btm_text)

        # slider

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(40, 200)
        self.slider.setValue(100)
        self.slider.setTickInterval(1)   

        self.slider.valueChanged.connect(self.on_slider_move)

        layout.addWidget(self.slider)

        # Play button
        self.play_button = QPushButton("start")
        layout.addWidget(self.play_button)

    def on_slider_move(self):
        value = self.slider.value()
        self.btm_text.setText(str(value))
        
