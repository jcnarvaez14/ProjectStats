import os
import pickle
import json
import pandas as pd
import logging

import config
from read import read_window
from descriptive import descriptives
from display import display_descriptive, export_pdf_report



# Define base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "df.pkl")
RESULTS_PATH = os.path.join(BASE_DIR, "..", "data", "results.pkl")
PDF_PATH = os.path.join(BASE_DIR, "..", "results", "descriptive_report.pdf")

def run_read():
    """
    Opens a file selection dialog, loads the dataset, saves it as a pickle file,
    and exports the column headers to a JSON file.
    """
    df = read_window()
    if df is not None:
        df.to_pickle(DATA_PATH)
        logging.info("Data loaded and saved to disk.")
        export_column_headers()

def export_column_headers():
    """
    Loads the saved DataFrame and exports its column headers to a JSON file.
    """
    try:
        df = pd.read_pickle(DATA_PATH)
        columns = list(df.columns)
        columns_path = os.path.join(BASE_DIR, "..", "data", "columns.json")
        with open(columns_path, "w") as f:
            json.dump(columns, f)
        logging.info("Column headers exported.")
    except Exception as e:
        logging.error(f"Error exporting column headers: {e}")

def run_descriptive():
    """
    Loads the dataset and selected columns, computes descriptive statistics, and
    saves the analysis results to a pickle file.
    """
    try:
        df = pd.read_pickle(DATA_PATH)
    except FileNotFoundError:
        logging.error("Data file not found. Run `run_read` first.")
        return

    selected_path = os.path.join(BASE_DIR, "..", "data", "selected_columns.json")
    if not os.path.exists(selected_path):
        logging.warning("selected_columns.json not found.")
        return

    with open(selected_path, "r", encoding="utf-8") as f:
        selected_columns = json.load(f)

    if not selected_columns:
        logging.warning("No columns selected for analysis.")
        return

    exclude_columns = [col for col in df.columns if col not in selected_columns]

    try:
        fig_desc, histograms, scatterplots, correlation_heatmap = descriptives(df, exclude_columns)
    except Exception as e:
        logging.error(f"Error running descriptives: {e}")
        return

    with open(RESULTS_PATH, "wb") as f:
        pickle.dump((fig_desc, histograms, scatterplots, correlation_heatmap), f)

    logging.info("Descriptive analysis completed and results saved.")

def run_display():
    """
    Loads the descriptive analysis results and displays them. Cleans up temporary files afterward.
    """
    try:
        with open(RESULTS_PATH, "rb") as f:
            fig_desc, histograms, scatterplots, correlation_heatmap = pickle.load(f)
            if fig_desc is None or correlation_heatmap is None:
                logging.warning("Analysis results incomplete. Please rerun `run_descriptive`.")
                return
    except FileNotFoundError:
        logging.error("Results file not found. Run `run_descriptive` first.")
        return

    display_descriptive(fig_desc, histograms, scatterplots, correlation_heatmap)

def clear_data_folder():
    """
    Deletes all temporary files in the /data folder.
    """
    data_folder = os.path.join(BASE_DIR, "..", "data")
    if not os.path.exists(data_folder):
        return
    for filename in os.listdir(data_folder):
        file_path = os.path.join(data_folder, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            logging.warning(f"Could not delete {file_path}: {e}")

def run_print():
    """
    Exports the descriptive analysis results into a multi-page PDF report.
    """
    try:
        with open(RESULTS_PATH, "rb") as f:
            fig_desc, histograms, scatterplots, correlation_heatmap = pickle.load(f)
    except FileNotFoundError:
        logging.error("Results file not found. Run `run_descriptive` first.")
        return

    export_pdf_report(fig_desc, histograms, scatterplots, correlation_heatmap, PDF_PATH)
    logging.info(f"PDF report successfully created at {PDF_PATH}.")
    
    clear_data_folder()
    logging.info("Temporary files in /data have been deleted.")