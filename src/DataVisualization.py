import sys
import csv
import matplotlib.pyplot as plt
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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class ScatterPlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Scatter Plot")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.plot_button = QPushButton("Plot Scatter")
        self.plot_button.clicked.connect(self.plot_scatter)
        self.layout.addWidget(self.plot_button)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Add a toolbar for zoom, pan, and home
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout.addWidget(self.toolbar)

        # Add keyboard shortcuts for zoom and pan
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.triggered.connect(self.zoom_in)
        self.addAction(zoom_in_action)
        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.triggered.connect(self.zoom_out)
        self.addAction(zoom_out_action)
        pan_action = QAction("Pan", self)
        pan_action.triggered.connect(self.pan)
        self.addAction(pan_action)
        home_action = QAction("Home", self)
        home_action.triggered.connect(self.home)
        self.addAction(home_action)

        # Set keyboard shortcuts
        zoom_in_action.setShortcut(Qt.CTRL + Qt.Key_Plus)
        zoom_out_action.setShortcut(Qt.CTRL + Qt.Key_Minus)
        pan_action.setShortcut(Qt.CTRL + Qt.Key_P)
        home_action.setShortcut(Qt.CTRL + Qt.Key_H)

    def zoom_in(self):
        self.toolbar.zoom()

    def zoom_out(self):
        self.toolbar.zoom(-1)

    def pan(self):
        self.toolbar.pan()

    def home(self):
        self.toolbar.home()

    def plot_scatter(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        filename, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV files (*.csv)")

        if filename:
            data = self.read_csv(filename)
            if data:
                self.figure.clear()
                ax = self.figure.add_subplot(111)
                ax.scatter(data["time"], data["counts"])
                ax.set_xlabel("time")
                ax.set_ylabel("counts")
                self.canvas.draw()

    def read_csv(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                data = {"time": [], "counts": []}
                for row in reader:
                    data["time"].append(float(row["time"]))
                    data["counts"].append(float(row["counts"]))
                return data
        except Exception as e:
            print("Error reading CSV:", e)
            return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScatterPlotWindow()
    window.show()
    sys.exit(app.exec_())
