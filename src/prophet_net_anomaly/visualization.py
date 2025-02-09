import matplotlib.pyplot as plt

def plot_anomalies(df, metric="packet_count"):
    plt.figure(figsize=(12, 6))

    # Plot actual data
    plt.plot(df["ds"], df["y"], label="Actual", color="blue", alpha=0.6)

    # Plot predicted values
    plt.plot(df["ds"], df["yhat"], label="Predicted", color="green", linestyle="dashed")

    # Plot upper and lower bounds
    plt.fill_between(df["ds"], df["yhat_lower"], df["yhat_upper"], color="gray", alpha=0.3, label="Prediction Range")

    # Highlight anomalies
    anomalies = df[df["is_anomaly"]]
    plt.scatter(anomalies["ds"], anomalies["y"], color="red", label="Anomalies", zorder=3)

    plt.xlabel("Timestamp")
    plt.ylabel(metric.replace("_", " ").title())
    plt.legend()
    plt.title(f"Anomaly Detection in {metric.replace('_', ' ').title()}")
    plt.show()

if __name__ == "__main__":
    import pandas as pd
    from anomaly_detector import AnomalyDetector

    # Load sample data
    df = pd.read_csv("../data/raw/sample_network_data.csv", parse_dates=["timestamp"])

    # Run anomaly detection
    detector = AnomalyDetector()
    anomalies_df = detector.detect_anomalies(df, "packet_count")

    # Plot results
    plot_anomalies(anomalies_df, "packet_count")
