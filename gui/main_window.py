from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel

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
        
        # Add label
        label = QLabel("Welcome to Meteronome App")
        layout.addWidget(label)
        
