from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QFileDialog,
    QAction,
)
from PyQt5.QtCore import Qt
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Ui_winMain(object):
    def setupUi(self, winMain):
        winMain.setObjectName("winMain")
        winMain.resize(928, 722)
        winMain.setFixedSize(winMain.size()) 
        self.centralwidget = QtWidgets.QWidget(winMain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tbwMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tbwMain.setEnabled(True)
        self.tbwMain.setIconSize(QtCore.QSize(50, 50))
        self.tbwMain.setObjectName("tbwMain")
        self.wDataScreening = QtWidgets.QWidget()
        self.wDataScreening.setEnabled(True)
        self.wDataScreening.setObjectName("wDataScreening")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.wDataScreening)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.wDataScreening)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 884, 574))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(711, 500, 171, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ScreeningFile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ScreeningFile.setObjectName("ScreeningFile")
        self.horizontalLayout_3.addWidget(self.ScreeningFile)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 871, 491))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Plot_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Plot_label.setObjectName("Plot_label")
        self.verticalLayout_4.addWidget(self.Plot_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.gridLayout_8.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainTab/icons/main_engineering.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbwMain.addTab(self.wDataScreening, icon, "")
        self.wFiltering = QtWidgets.QWidget()
        self.wFiltering.setEnabled(False)
        self.wFiltering.setObjectName("wFiltering")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mainTab/icons/main_diagnosis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbwMain.addTab(self.wFiltering, icon1, "")
        self.wSetting = QtWidgets.QWidget()
        self.wSetting.setObjectName("wSetting")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.wSetting)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 911, 561))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mainTab/icons/main_setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbwMain.addTab(self.wSetting, icon2, "")
        self.wHelp = QtWidgets.QWidget()
        self.wHelp.setObjectName("wHelp")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.wHelp)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tbwHelp = QtWidgets.QTabWidget(self.wHelp)
        self.tbwHelp.setTabPosition(QtWidgets.QTabWidget.South)
        self.tbwHelp.setObjectName("tbwHelp")
        self.wVideo = QtWidgets.QWidget()
        self.wVideo.setObjectName("wVideo")
        self.tbwHelp.addTab(self.wVideo, "")
        self.wManual = QtWidgets.QWidget()
        self.wManual.setObjectName("wManual")
        self.tbwHelp.addTab(self.wManual, "")
        self.gridLayout_6.addWidget(self.tbwHelp, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mainTab/icons/main_help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbwMain.addTab(self.wHelp, icon3, "")
        self.gridLayout.addWidget(self.tbwMain, 0, 1, 1, 1)
        winMain.setCentralWidget(self.centralwidget)
        self.mbMain = QtWidgets.QMenuBar(winMain)
        self.mbMain.setGeometry(QtCore.QRect(0, 0, 928, 22))
        self.mbMain.setObjectName("mbMain")
        winMain.setMenuBar(self.mbMain)
        self.stbStatusbar = QtWidgets.QStatusBar(winMain)
        self.stbStatusbar.setObjectName("stbStatusbar")
        winMain.setStatusBar(self.stbStatusbar)
        

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_4.addWidget(self.canvas)
        # Add a toolbar for zoom, pan, and home
        self.toolbar = NavigationToolbar(self.canvas)
        self.verticalLayout_4.addWidget(self.toolbar)

        self.retranslateUi(winMain)
        self.tbwMain.setCurrentIndex(0)
        self.tbwHelp.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        _translate = QtCore.QCoreApplication.translate
        winMain.setWindowTitle(_translate("winMain", "Roche HTP Internal Tool"))
        self.ScreeningFile.setText(_translate("winMain", "Select File"))
        self.Plot_label.setText(_translate("winMain", "Data Preview:"))
        self.tbwMain.setTabText(self.tbwMain.indexOf(self.wDataScreening), _translate("winMain", "Data Screening"))
        self.tbwMain.setTabToolTip(self.tbwMain.indexOf(self.wDataScreening), _translate("winMain", "DataScreening"))
        self.tbwMain.setTabText(self.tbwMain.indexOf(self.wFiltering), _translate("winMain", "Filtering"))
        self.tbwMain.setTabToolTip(self.tbwMain.indexOf(self.wFiltering), _translate("winMain", "Filtering"))
        self.tbwMain.setTabText(self.tbwMain.indexOf(self.wSetting), _translate("winMain", "Setting"))
        self.tbwMain.setTabToolTip(self.tbwMain.indexOf(self.wSetting), _translate("winMain", "Setting"))
        self.tbwHelp.setTabText(self.tbwHelp.indexOf(self.wVideo), _translate("winMain", "Video"))
        self.tbwHelp.setTabText(self.tbwHelp.indexOf(self.wManual), _translate("winMain", "Manual"))
        self.tbwMain.setTabText(self.tbwMain.indexOf(self.wHelp), _translate("winMain", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    winMain = QtWidgets.QMainWindow()
    ui = Ui_winMain()
    ui.setupUi(winMain)
    winMain.show()
    sys.exit(app.exec_())
