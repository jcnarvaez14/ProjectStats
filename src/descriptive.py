import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from config import plot_correlation_heatmap
import config

def descriptives(df_descrip, exclude_columns=None, hist_size_base=(5, 4), scatter_size_base=(5, 4)):
    if exclude_columns is None:
        exclude_columns = []

    df_analysis = df_descrip.drop(columns=exclude_columns, errors='ignore')
    descriptive_stats = df_analysis.describe().round(2)

    numeric_columns = df_analysis.select_dtypes(include=[np.number]).columns
    num_cols = len(numeric_columns)
    histograms = []

    # 1. Histograms
    if num_cols > 0:
        rows_hist = (num_cols + 2) // 3
        hist_figsize = (hist_size_base[0] * 3, hist_size_base[1] * rows_hist)
        fig_hist, axes_hist = plt.subplots(rows_hist, 3, figsize=hist_figsize)
        axes_hist = axes_hist.flatten()

        for idx, column in enumerate(numeric_columns):
            sns.histplot(df_analysis[column], kde=True, ax=axes_hist[idx])
            axes_hist[idx].axvline(df_analysis[column].mean(), color='red', linestyle='--', linewidth=2)
            axes_hist[idx].set_title(f'Histogram of {column}')
            axes_hist[idx].set_xlabel(column)
            axes_hist[idx].set_ylabel('Frequency')
            histograms.append(axes_hist[idx])

        for i in range(num_cols, len(axes_hist)):
            axes_hist[i].axis('off')

        plt.tight_layout()
        fig_hist.subplots_adjust(hspace=0.4)

    # 2. Scatterplots (3x3 per figure)
    scatterplots = []
    scatterplot_pairs = list(itertools.combinations(numeric_columns, 2))

    for i in range(0, len(scatterplot_pairs), 9):
        fig_scatter, axes = plt.subplots(3, 3, figsize=(scatter_size_base[0] * 3, scatter_size_base[1] * 3))
        axes = axes.flatten()
        for j, (col_x, col_y) in enumerate(scatterplot_pairs[i:i + 9]):
            sns.scatterplot(x=df_analysis[col_x], y=df_analysis[col_y], ax=axes[j])
            axes[j].set_title(f'{col_x} vs {col_y}')
            axes[j].set_xlabel(col_x)
            axes[j].set_ylabel(col_y)
            scatterplots.append(axes[j])
        for k in range(j + 1, 9):
            axes[k].axis('off')
        plt.tight_layout()

    # 3. Correlation heatmap (image only)
    corr_matrix = df_analysis.corr()
    correlation_heatmap = plot_correlation_heatmap(corr_matrix)

    # 4. Descriptive statistics table as image
    fig_desc, ax_desc = plt.subplots(figsize=(12, 2 + 0.25 * len(descriptive_stats)))
    ax_desc.axis('off')
    tbl = ax_desc.table(cellText=descriptive_stats.values,
                        colLabels=descriptive_stats.columns,
                        rowLabels=descriptive_stats.index,
                        cellLoc='center',
                        loc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    fig_desc.tight_layout()

    return fig_desc, histograms, scatterplots, correlation_heatmap