# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from screan import *
from main import *
from rsa import *
import hashlib
import sys

counter = 0



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main = Ui_main()
        self.main.setupUi(self)
        self.main.rsa.clicked.connect(self.test)
        self.show()

    def test(self):
        self.rsa = Ui_RSA()
        self.rsa.setupUi(self)
        self.show()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)
        self.show()

    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            if '3dd0be2e96de4838d0903453b8d2b786' == self.get_hash_md5():

                self.main = MainWindow()
                self.main.show()
                self.close()
            else:
                self.close()
        counter += 1

    def get_hash_md5(self, filename="screan.py"):
        with open(filename, 'rb') as f:
            m = hashlib.md5()
            while True:
                data = f.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
