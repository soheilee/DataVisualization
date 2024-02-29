import os
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QRadioButton
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon
from Preprocessing_UI_Layout import Ui_winMain  # Import the generated UI class
import subprocess
import matplotlib.pyplot as plt

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI from the generated class
        self.ui = Ui_winMain()
        self.ui.setupUi(self)

        # Load icons
        self.load_icons()

        # Connect signals to slots
        self.connect_signals()

    def load_icons(self):
        # Get the path to the icons directory relative to the current file
        icons_dir = os.path.join(os.path.dirname(__file__), 'icons')
        # Define icon paths and their corresponding widget attributes
        icon_paths = {
            'ScreeningFile': 'Data_Visualization.png',
        }
        tab_icon_paths = {
        0: 'main_screening.png',
        1: 'main_filtering.png',
        2: 'main_setting.png',
        3: 'main_help.png'
        }
        # Load icons for individual widgets
        for widget_name, icon_name in icon_paths.items():
            icon_path = os.path.join(icons_dir, icon_name)
            getattr(self.ui, widget_name).setIcon(QIcon(icon_path))
        # Load icons for tab icons
        for tab_index, icon_name in tab_icon_paths.items():
            icon_path = os.path.join(icons_dir, icon_name)
            self.ui.tbwMain.setTabIcon(tab_index, QIcon(icon_path))
        # Set application icon
        app_icon_path = os.path.join(icons_dir, 'app_icon.png')
        app.setWindowIcon(QIcon(app_icon_path))

    def connect_signals(self):
        # Connect signals to slots
        self.ui.ScreeningFile.clicked.connect(self.visualizeFile)

    def zoom_in(self):
        self.ui.toolbar.zoom()
    def zoom_out(self):
        self.ui.toolbar.zoom(-1)
    def pan(self):
        self.ui.toolbar.pan()
    def home(self):
        self.ui.toolbar.home()
    
    def visualizeFile(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        filename, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV files (*.csv)")
        if filename:
            data = self.read_csv(filename)
            if data:
                print("great!")
                self.ui.figure.clear()
                ax = self.ui.figure.add_subplot(111)
                ax.scatter(data["time"], data["adc_counts"])
                # Adjust x-axis label position:
                ax.set_xlabel("time (s)", labelpad=15) # Increase labelpad to 15 points
                ax.set_ylabel("adc_counts")
                # Optionally, adjust bottom margin for more space:
                plt.subplots_adjust(bottom=0.25)
                self.ui.canvas.draw()

    def read_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                data = {"time": [], "adc_counts": []}
                for row in reader:
                    data["time"].append(float(row["time"]))
                    data["adc_counts"].append(float(row["adc_counts"]))
                    # Extract filename without the path
            filename_without_path = os.path.basename(filename)
            self.ui.Plot_label.setText(f"Bright Cycle Preview:{filename_without_path}")
            return data
        except Exception as e:
            print("Error reading CSV:", e)
            return None



            
            
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
