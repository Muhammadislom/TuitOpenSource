from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)
        MainWindow.setMinimumSize(QtCore.QSize(640, 400))
        MainWindow.setMaximumSize(QtCore.QSize(640, 400))
        MainWindow.setStyleSheet("background: #323450;\n"
                                 "border-radius: 10px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.screanTitle = QtWidgets.QLabel(self.centralwidget)
        self.screanTitle.setGeometry(QtCore.QRect(140, 50, 360, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.screanTitle.setFont(font)
        self.screanTitle.setStyleSheet("font-family: Roboto;\n"
                                       "font-style: normal;\n"
                                       "font-weight: normal;\n"
                                       "font-size: 60px;\n"
                                       "line-height: 70px;\n"
                                       "color: #F5603F;")
        self.screanTitle.setObjectName("screanTitle")
        self.ScreanSubtitleLoad = QtWidgets.QLabel(self.centralwidget)
        self.ScreanSubtitleLoad.setGeometry(QtCore.QRect(160, 160, 310, 31))
        self.ScreanSubtitleLoad.setStyleSheet("font-family: Roboto;\n"
                                              "font-style: normal;\n"
                                              "font-weight: bold;\n"
                                              "font-size: 18px;\n"
                                              "line-height: 21px;\n"
                                              "/* identical to box height */\n"
                                              "color: #F5603F;")
        self.ScreanSubtitleLoad.setObjectName("ScreanSubtitleLoad")
        self.filename = QtWidgets.QLabel(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(10, 280, 61, 16))
        self.filename.setStyleSheet("font-family: Roboto;\n"
                                    "font-style: normal;\n"
                                    "font-weight: normal;\n"
                                    "font-size: 12px;\n"
                                    "line-height: 14px;\n"
                                    "\n"
                                    "color: #F5603F;")
        self.filename.setObjectName("filename")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 310, 640, 1))
        self.progressBar.setStyleSheet("QProgressBar::chunk{\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(255,255,255,1), stop:1 rgba(245,96,63,1));\n"
                                       "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.CreaterName = QtWidgets.QLabel(self.centralwidget)
        self.CreaterName.setGeometry(QtCore.QRect(460, 370, 161, 21))
        self.CreaterName.setStyleSheet("font-family: Roboto;\n"
                                       "font-style: normal;\n"
                                       "font-weight: bold;\n"
                                       "font-size: 12px;\n"
                                       "line-height: 14px;\n"
                                       "/* identical to box height */\n"
                                       "color: #716969;\n"
                                       "")
        self.CreaterName.setObjectName("CreaterName")
        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(290, 330, 60, 16))
        self.loading.setStyleSheet("font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 12px;\n"
                                   "line-height: 14px;\n"
                                   "/* identical to box height */\n"
                                   "\n"
                                   "\n"
                                   "color: #F5603F;")
        self.loading.setObjectName("loading")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.screanTitle.setText(_translate("MainWindow", "Сryptography"))
        self.ScreanSubtitleLoad.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-size:14pt;\">LOADING </span><span style=\" font-size:14pt; font-weight:400;\">Checking files please wait</span></p></body></html>"))
        self.filename.setText(_translate("MainWindow", "File Name"))
        self.CreaterName.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:9pt;\">Creater: </span><span style=\" font-size:9pt; font-weight:400;\">E. Muhammadislom</span></p></body></html>"))
        self.loading.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">loading...</span></p></body></html>"))
