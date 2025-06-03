import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
import openpyxl
import logging
import config

def read_window(encoding="utf-8"):
    """
    Opens a file selection dialog for a CSV or Excel file and loads it into a DataFrame.

    Parameters:
    - encoding (str): The encoding to use when reading a CSV file (default is "utf-8").

    Returns:
    - pd.DataFrame or None: Returns a DataFrame if a valid file is selected and loaded;
                            otherwise, returns None.
    """
    logging.info("Opening file selection window...")

    # Hide the main Tkinter window
    root = tk.Tk()
    root.withdraw()

    # Open file dialog
    file_link = askopenfilename(
        title="Select a file",
        filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
    )

    # If no file is selected
    if not file_link:
        logging.warning("No file was selected by the user.")
        return None

    try:
        # Load based on file extension
        if file_link.endswith(".csv"):
            df = pd.read_csv(file_link, encoding=encoding)
        elif file_link.endswith(".xlsx"):
            df = pd.read_excel(file_link, engine="openpyxl")
        else:
            raise ValueError("Unsupported file format. Please select a .csv or .xlsx file.")

        logging.info(f"File successfully loaded from: {file_link}")
        return df

    except FileNotFoundError:
        logging.error(f"The file at {file_link} was not found.")
    except Exception as e:
        logging.error(f"Error reading the file: {e}")