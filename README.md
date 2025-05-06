# Parquet to CSV Converter

This project provides a graphical user interface (GUI) application for converting Parquet files to CSV format using PyQt5. 

## Features

- Select multiple Parquet files for conversion.
- Convert selected files to CSV format with a single click.
- User-friendly interface with informative messages.

## Requirements

To run this project, you need to have the following Python packages installed:

- pandas
- pyqt5
- pyarrow

You can install the required packages using pip. Make sure to create a virtual environment for your project and run the following command:

```
pip install -r requirements.txt
```

## Usage

1. Run the application by executing the `main.py` file:
   ```
   python main.py
   ```

2. Click on the "Select Files" button to choose the Parquet files you want to convert.

3. After selecting the files, click on the "Convert to CSV" button to start the conversion process.

4. Once the conversion is complete, you will receive a success message, and the CSV files will be saved in the same directory as the original Parquet files.

## License

This project is open-source and available for modification and distribution.