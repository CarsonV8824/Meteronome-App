from PySide6.QtWidgets import QApplication, QWidget

from gui.main_window import MainWindow

def main():
    app = QApplication()
    with open("assets/styles.css") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()