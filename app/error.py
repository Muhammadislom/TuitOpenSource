from PyQt5.QtWidgets import QMessageBox


class Error:
    def __init__(self, title, messages):
        self.error = QMessageBox()
        self.error.setWindowTitle(title)
        self.error.setText(messages)
        self.error.setIcon(QMessageBox.Warning)
        self.error.setStandardButtons(QMessageBox.Ok)
        self.error.exec_()
