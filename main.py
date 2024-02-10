from PyQt6.QtWidgets import QApplication
from home_page import HOME

if __name__ == "__main__":
    app = QApplication([])
    window = HOME(False)
    window.show()
    app.exec()