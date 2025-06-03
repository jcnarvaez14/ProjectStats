import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging


# Pandas display configuration
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.6f' % x)
pd.set_option('display.width', 1000)

# Seaborn & Matplotlib visualization configuration
sns.set(style="whitegrid", palette="gray")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.edgecolor'] = 'gray'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'
plt.rcParams['grid.color'] = 'gray'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['figure.dpi'] = 100

# Define log path relative to project (for logging)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Optional: basic logging configuration
def setup_logging():
    logging.basicConfig(
        #filemode='w',  # 'w' = overwrite the file; 'a' = append (default)
        filename=os.path.join(LOG_DIR, 'test.log'),
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def plot_correlation_heatmap(corr_matrix):
    plt.figure(figsize=(12, 8))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(
        corr_matrix,
        mask=mask,
        annot=True,
        cmap='coolwarm',
        fmt='.2f',
        linewidths=0.5
    )
    plt.title('Correlation Matrix Heatmap')
    plt.tight_layout()
    return plt.gcf()