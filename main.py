import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QMessageBox
)

class ParquetToCsvConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parquet to CSV Converter")
        self.setGeometry(300, 300, 400, 200)

        # Layout and widgets
        self.layout = QVBoxLayout()

        self.label = QLabel("Select Parquet files to convert to CSV")
        self.layout.addWidget(self.label)

        self.select_button = QPushButton("Select Files")
        self.select_button.clicked.connect(self.select_files)
        self.layout.addWidget(self.select_button)

        self.convert_button = QPushButton("Convert to CSV")
        self.convert_button.clicked.connect(self.convert_to_csv)
        self.layout.addWidget(self.convert_button)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # File paths
        self.selected_files = []

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Parquet Files", "", "Parquet Files (*.parquet)")
        if files:
            self.selected_files = files
            self.label.setText(f"Selected {len(files)} file(s)")

    def convert_to_csv(self):
        if not self.selected_files:
            QMessageBox.warning(self, "No Files Selected", "Please select Parquet files first.")
            return

        for file in self.selected_files:
            try:
                # Read Parquet and save as CSV
                df = pd.read_parquet(file)
                csv_file = file.replace(".parquet", ".csv")
                df.to_csv(csv_file, index=False)
            except Exception as e:
                QMessageBox.critical(self, "Conversion Error", f"Error converting {file}:\n{str(e)}")
                return

        QMessageBox.information(self, "Success", "All files converted successfully!")
        self.label.setText("Select Parquet files to convert to CSV")
        self.selected_files = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParquetToCsvConverter()
    window.show()
    sys.exit(app.exec_())