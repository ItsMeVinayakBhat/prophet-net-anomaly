import argparse
import pandas as pd
import plotly.io as pio
from .anomaly_detector import AnomalyDetector
from .visualization import plot_anomalies_interactive

def main():
    parser = argparse.ArgumentParser(description="Prophet-Net-Anomaly: Detect anomalies in network time series data.")

    parser.add_argument("data_file", type=str, help="Path to the CSV file containing network time series data.")
    parser.add_argument("--metric", type=str, default="packet_count", help="Column to analyze for anomalies.")
    parser.add_argument("--interval_width", type=float, default=0.95, help="Confidence interval width for Prophet.")
    parser.add_argument("--save", type=str, help="Path to save the plot (e.g., anomalies_plot.html).", default=None)

    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.data_file, parse_dates=["timestamp"])

    # Run anomaly detection
    detector = AnomalyDetector(interval_width=args.interval_width)
    anomalies_df = detector.detect_anomalies(df, args.metric)

    # Generate interactive plot
    fig = plot_anomalies_interactive(anomalies_df, args.metric)

    if args.save:
        # Save as an interactive HTML file
        pio.write_html(fig, args.save)
        print(f"Plot saved to {args.save}")
    else:
        # Show interactive plot in browser
        fig.show()

if __name__ == "__main__":
    main()
