from PyQt5.QtWidgets import QApplication
from gui import GUI

if __name__ == "__main__":
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec_()
