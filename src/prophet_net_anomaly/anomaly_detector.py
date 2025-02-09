import pandas as pd
import numpy as np
from prophet import Prophet

class AnomalyDetector:
    def __init__(self, interval_width=0.95):
        self.interval_width = interval_width

    def detect_anomalies(self, data, metric="packet_count"):
        # Prepare data for Prophet
        df = data.rename(columns={"timestamp": "ds", metric: "y"})

        # Fit Prophet model
        model = Prophet(interval_width=self.interval_width)
        model.fit(df)

        # Make future predictions
        future = model.make_future_dataframe(periods=0)  # Predict only for existing data
        forecast = model.predict(future)

        # Merge predictions with original data
        df = df.merge(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']], on="ds")

        # Identify anomalies (values outside predicted bounds)
        df["is_anomaly"] = (df["y"] > df["yhat_upper"]) | (df["y"] < df["yhat_lower"])

        return df

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv("../data/raw/sample_network_data.csv", parse_dates=["timestamp"])
    detector = AnomalyDetector()
    anomalies_df = detector.detect_anomalies(df, "packet_count")
    print(anomalies_df[anomalies_df["is_anomaly"]])
