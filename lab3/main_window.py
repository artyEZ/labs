from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


import sys

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

