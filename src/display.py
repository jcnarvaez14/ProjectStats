import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import logging
import config


def display_descriptive(
    descriptive_table_fig,
    histograms,
    scatterplots,
    correlation_heatmap
):
    """
    Displays descriptive table, histograms, scatter plots, and a correlation heatmap.

    Parameters:
    - descriptive_table_fig (plt.Figure): Descriptive statistics table figure.
    - histograms (list): List of histogram Axes.
    - scatterplots (list): List of scatterplot Axes.
    - correlation_heatmap (plt.Figure): Heatmap figure object.
    """
    logging.info("Displaying descriptive statistics as a table (image).")
    try:
        descriptive_table_fig.show()
    except Exception as e:
        logging.warning(f"Could not render descriptive table: {e}")

    logging.info("Displaying correlation matrix heatmap.")
    try:
        correlation_heatmap.show()
    except Exception as e:
        logging.warning(f"Could not render heatmap: {e}")

    logging.info("Rendering histograms...")
    for hist in histograms:
        try:
            hist.figure.show()
        except Exception as e:
            logging.warning(f"Could not render histogram: {e}")

    logging.info("Rendering scatterplots...")
    for scatter in scatterplots:
        try:
            scatter.figure.show()
        except Exception as e:
            logging.warning(f"Could not render scatterplot: {e}")

    # Optional: keep figures open
    plt.show()
    
def export_pdf_report(fig_desc, histograms, scatterplots, correlation_heatmap, output_path):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        logging.info("Generating PDF report...")

        with PdfPages(output_path) as pdf:
            # 1. Descriptive Table
            fig_desc.set_size_inches(8.27, 11.69)  # A4 portrait
            fig_desc.tight_layout()
            pdf.savefig(fig_desc)
            plt.close(fig_desc)

            # 2. Correlation Heatmap
            correlation_heatmap.set_size_inches(8.27, 11.69)
            correlation_heatmap.tight_layout()
            pdf.savefig(correlation_heatmap)
            plt.close(correlation_heatmap)

            # 3. Histograms
            hist_figures = set(hist.figure for hist in histograms)
            for fig in hist_figures:
                fig.set_size_inches(8.27, 11.69)
                fig.tight_layout()
                pdf.savefig(fig)
                plt.close(fig)
            logging.info(f"{len(hist_figures)} histogram pages added.")

            # 4. Scatterplots
            scatter_figures = set(scatter.figure for scatter in scatterplots)
            for fig in scatter_figures:
                fig.set_size_inches(8.27, 11.69)
                fig.tight_layout()
                pdf.savefig(fig)
                plt.close(fig)
            logging.info(f"{len(scatter_figures)} scatterplot pages added.")

        logging.info(f"PDF report saved to: {output_path}")

        # Open PDF automatically (only Windows)
        try:
            os.startfile(output_path)
        except AttributeError:
            logging.warning("Auto-opening is only supported on Windows.")

    except Exception as e:
        logging.error(f"Failed to generate PDF report: {e}")