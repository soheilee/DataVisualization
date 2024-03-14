import os
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from Preprocessing_UI_Layout import Ui_winMain

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_winMain()
        self.ui.setupUi(self)
        self.load_icons()
        self.connect_signals()
        self.ui.SelectedFile_listWidget.setSelectionMode(QListWidget.MultiSelection)

    def load_icons(self):
        icons_dir = os.path.join(os.path.dirname(__file__), 'icons')
        icon_paths = {
            'ScreeningFile': 'Data_Visualization.png',
            'filterButton': 'Filter_Button.png',
            'addButton': 'Add_Button.png',
            'removeButton': 'Remove_Button.png',
        }
        tab_icon_paths = {
            0: 'main_screening.png',
            1: 'main_filtering.png',
            2: 'main_setting.png',
            3: 'main_help.png'
        }
        for widget_name, icon_name in icon_paths.items():
            icon_path = os.path.join(icons_dir, icon_name)
            icon = QIcon(icon_path)
            getattr(self.ui, widget_name).setIcon(icon)
            getattr(self.ui, widget_name).setIconSize(QSize(40, 40))  
        for tab_index, icon_name in tab_icon_paths.items():
            icon_path = os.path.join(icons_dir, icon_name)
            self.ui.tbwMain.setTabIcon(tab_index, QIcon(icon_path))
        app_icon_path = os.path.join(icons_dir, 'app_icon.png')
        self.setWindowIcon(QIcon(app_icon_path))

    def connect_signals(self):
        self.ui.ScreeningFile.clicked.connect(self.visualize_file)
        self.ui.addButton.clicked.connect(self.open_file_dialog)
        self.ui.removeButton.clicked.connect(self.remove_selected_files)
        self.ui.filterButton.clicked.connect(self.save_last_100_data_for_each_file)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        filenames, _ = file_dialog.getOpenFileNames(self, "Open CSV Files", "", "CSV files (*.csv)")
        if filenames:
            self.ui.SelectedFile_listWidget.addItems(filenames)
        self.update_remove_button_state()

    def remove_selected_files(self):
        selected_items = self.ui.SelectedFile_listWidget.selectedItems()
        for item in selected_items:
            self.ui.SelectedFile_listWidget.takeItem(self.ui.SelectedFile_listWidget.row(item))
        self.update_remove_button_state()

    def update_remove_button_state(self):
        selected_items_count = self.ui.SelectedFile_listWidget.count()
        self.ui.removeButton.setEnabled(selected_items_count > 0)

    def visualize_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        filename, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV files (*.csv)")
        if filename:
            data = self.read_csv(filename)
            if data is not None and not data.empty:  
                self.ui.figure.clear()
                ax = self.ui.figure.add_subplot(111)
                if "Methan" in filename:
                    ax.scatter(data.index, data["15.0"])
                    ax.set_xlabel("Index", labelpad=15, fontsize=12)
                    ax.set_ylabel("15.0", fontsize=12)
                elif "Lachgas" in filename:
                    ax.scatter(data.index, data["44.0"])
                    ax.set_xlabel("Index", labelpad=15, fontsize=12)
                    ax.set_ylabel("44.0", fontsize=12)
                plt.subplots_adjust(bottom=0.25)
                self.ui.canvas.draw()

    def read_csv(self, filename):
        try:
            df = pd.read_csv(filename, sep=';', decimal=',')
            if "Methan" in filename:
                data = df[["15.0", "19.0","40.0","44.0"]]
            elif "Lachgas" in filename:
                data = df[["30.0", "19.0", "40.0", "44.0"]]
            filename_without_path = os.path.basename(filename)
            self.ui.Plot_label.setText(f"Preview: {filename_without_path}")
            return data
        except Exception as e:
            print("Error reading CSV:", e)
            return None

    def filter_data(self):
        try:
            last_100_data = []
            file_names = [self.ui.SelectedFile_listWidget.item(index).text() for index in range(self.ui.SelectedFile_listWidget.count())]
            for filename in file_names:
                data = self.read_csv(filename)
                if data is not None:
                    last_100_data.append(data.iloc[-100:, :])
            return last_100_data
        except Exception as e:
            print("Error reading CSV:", e)
            return None

    def save_last_100_data(self, data_list, file_prefix):
        try:
            script_directory = os.path.dirname(__file__)
            output_directory = os.path.join(script_directory, 'last_100_data')

            # Print the output directory for debugging
            print("Output directory:", output_directory)

            # Create the directory if it doesn't exist
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            for i, data in enumerate(data_list):
                filename = f"{file_prefix.rstrip('_last_100.csv')}_last_100_{i+1}.csv"
                output_file = os.path.join(output_directory, filename)
                data.to_csv(output_file, index=False)
                    
        except Exception as e:
            print("Error saving CSV:", e)



    def concatenate_csv(self):
        try:
            # Get all CSV files with '_last_100.csv' in their names
            script_directory = os.path.dirname(__file__)
            output_directory = os.path.join(script_directory, 'last_100_data')
            csv_files = [file for file in os.listdir(output_directory)]

            # Concatenate rows from all CSV files
            concatenated_df = pd.DataFrame()  # Initialize an empty DataFrame
            for file in csv_files:
                df = pd.read_csv(os.path.join(output_directory, file))
                df = df.reset_index(drop=True)  # Reset index
                concatenated_df = pd.concat([concatenated_df, df], axis=0, ignore_index=True)

            concatenated_filename = os.path.join(output_directory, "15°C_Concatenated.csv")
            concatenated_df.to_csv(concatenated_filename, index=False)

        except Exception as e:
            print("Error concatenating CSV files:", e)


    def save_last_100_data_for_each_file(self):
        try:
            last_100_data = self.filter_data()
            if last_100_data is not None:
                output_directory = os.path.join(os.path.dirname(__file__), 'last_100_data')
                for index, data in enumerate(last_100_data):
                    output_filename = self.ui.SelectedFile_listWidget.item(index).text() 
                    file_name_without_extension, file_extension = os.path.splitext(output_filename)
                    output_filename = os.path.basename(file_name_without_extension)+"_last_100.csv"
                    output_file = os.path.join(output_directory, output_filename)
                    self.save_last_100_data([data], output_file)
                    self.ui.FilteredFile_listWidget.addItems([output_filename])
            self.concatenate_csv()
        except Exception as e:
            print("Error saving last 100 data:", e)


    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
