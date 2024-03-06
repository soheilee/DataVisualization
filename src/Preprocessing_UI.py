import os
import csv
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QListWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from Preprocessing_UI_Layout import Ui_winMain
import pandas as pd



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

         # Enable multi-selection mode for the list widget
        self.ui.SelectedFile_listWidget.setSelectionMode(QListWidget.MultiSelection)

        

    def load_icons(self):
        # Get the path to the icons directory relative to the current file
        icons_dir = os.path.join(os.path.dirname(__file__), 'icons')
        # Define icon paths and their corresponding widget attributes
        icon_paths = {
            'ScreeningFile': 'Data_Visualization.png',
            'filterButton' : 'Filter_Button.png',
            'addButton' : 'Add_Button.png',
            'removeButton' : 'Remove_Button.png',
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
            icon = QIcon(icon_path)
            getattr(self.ui, widget_name).setIcon(icon)
            # Set the icon size directly
            getattr(self.ui, widget_name).setIconSize(QSize(40, 40))  # Adjust the width and height as needed
        # Load icons for tab icons
        for tab_index, icon_name in tab_icon_paths.items():
            icon_path = os.path.join(icons_dir, icon_name)
            self.ui.tbwMain.setTabIcon(tab_index, QIcon(icon_path))
        # Set application icon
        app_icon_path = os.path.join(icons_dir, 'app_icon.png')
        self.setWindowIcon(QIcon(app_icon_path))

    def connect_signals(self):
        # Connect signals to slots
        self.ui.ScreeningFile.clicked.connect(self.visualizeFile)
        self.ui.addButton.clicked.connect(self.openFileDialog)
        self.ui.removeButton.clicked.connect(self.removeSelectedFiles)
        

    def openFileDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        filenames, _ = file_dialog.getOpenFileNames(self, "Open CSV Files", "", "CSV files (*.csv)")
        if filenames:
                # Add selected file names to the text edit
            self.ui.SelectedFile_listWidget.addItems(filenames)
        self.updateRemoveButtonState()   
    

    def removeSelectedFiles(self):
        # Get the currently selected items
        selected_items = self.ui.SelectedFile_listWidget.selectedItems()
        for item in selected_items:
            self.ui.SelectedFile_listWidget.takeItem(self.ui.SelectedFile_listWidget.row(item))
        self.updateRemoveButtonState()


    def updateRemoveButtonState(self):
        selected_items_count = self.ui.SelectedFile_listWidget.count()
        self.ui.removeButton.setEnabled(selected_items_count > 0)

    def visualizeFile(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        filename, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV files (*.csv)")
        if filename:
            data = self.read_csv(filename)
            if data:
                self.ui.figure.clear()
                ax = self.ui.figure.add_subplot(111)
                ax.scatter(data["Index"], data["15.0"])
                ax.set_xlabel("Index", labelpad=15, fontsize=12)
                ax.set_ylabel("15.0", fontsize=12)

                plt.subplots_adjust(bottom=0.25)
                self.ui.canvas.draw()

    def read_csv(self, filename):
        try:
            # Read CSV file using pandas
            df = pd.read_csv(filename, sep=';', decimal=',')
    
            # Extract required columns
            data = {
                "Index": df.index.tolist(),  # Use the DataFrame index as x-axis values
                "15.0": df["15.0"].astype(float).tolist()
            }
    
            # Set plot label
            filename_without_path = os.path.basename(filename)
            self.ui.Plot_label.setText(f"Preview: {filename_without_path}")
    
            return data
        except Exception as e:
            print("Error reading CSV:", e)
            return None


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.setWindowIcon(QIcon(r'C:\Users\Leyla Roohisefat\DataVisualization\src\icons\app_icon.ico'))
    window.show()
    sys.exit(app.exec_())
