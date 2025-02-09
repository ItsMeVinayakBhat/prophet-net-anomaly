import plotly.graph_objects as go
import pandas as pd
from anomaly_detector import AnomalyDetector

def plot_anomalies_interactive(df, metric="packet_count"):
    fig = go.Figure()

    # Actual values
    fig.add_trace(go.Scatter(
        x=df["ds"], y=df["y"],
        mode="lines", name="Actual",
        line=dict(color="blue"),
    ))

    # Predicted values
    fig.add_trace(go.Scatter(
        x=df["ds"], y=df["yhat"],
        mode="lines", name="Predicted",
        line=dict(color="green", dash="dash"),
    ))

    # Upper and Lower Bounds (Shaded Area)
    fig.add_trace(go.Scatter(
        x=df["ds"], y=df["yhat_upper"],
        mode="lines", name="Upper Bound",
        line=dict(color="gray"),
    ))
    fig.add_trace(go.Scatter(
        x=df["ds"], y=df["yhat_lower"],
        mode="lines", name="Lower Bound",
        line=dict(color="gray"),
        fill="tonexty", fillcolor="rgba(169, 169, 169, 0.3)",
    ))

    # Anomalies (Scatter points)
    anomalies = df[df["is_anomaly"]]
    fig.add_trace(go.Scatter(
        x=anomalies["ds"], y=anomalies["y"],
        mode="markers", name="Anomalies",
        marker=dict(color="red", size=8, symbol="x"),
    ))

    # Layout settings
    fig.update_layout(
        title=f"Interactive Anomaly Detection in {metric.replace('_', ' ').title()}",
        xaxis_title="Timestamp",
        yaxis_title=metric.replace("_", " ").title(),
        template="plotly_white",
    )

    # Show the interactive plot
    fig.show()

if __name__ == "__main__":
    # Load sample data
    df = pd.read_csv("../data/raw/sample_network_data.csv", parse_dates=["timestamp"])

    # Run anomaly detection
    detector = AnomalyDetector()
    anomalies_df = detector.detect_anomalies(df, "packet_count")

    # Show interactive plot
    plot_anomalies_interactive(anomalies_df, "packet_count")
