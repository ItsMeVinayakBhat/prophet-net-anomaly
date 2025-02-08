# Prophet-Net-Anomaly 🚀
A lightweight, open-source network anomaly detection package leveraging **Facebook Prophet** for time-series modeling.  
🔹 **Key Features**:  
✔ Anomaly detection based on Prophet’s upper/lower confidence bounds  
✔ **Persistence & Proximity Analysis** to minimize false positives  
✔ Optimized for network data: traffic volume, packet loss, DDoS detection  
✔ Sensitivity options to tune the model  

📌 **Getting Started**
```bash
pip install prophet-net-anomaly
```
**Project Structure**
```bash
prophet-net-anomaly/
├── src/
│   ├── prophet_net_anomaly/
│   │   ├── __init__.py
│   │   ├── anomaly_detector.py   # Core anomaly detection logic
│   │   ├── utils.py              # Helper functions (e.g., data preprocessing)
│   │   ├── visualization.py      # Functions for plotting anomalies
│   ├── tests/
│   │   ├── test_anomaly_detector.py  # Unit tests
│   │   ├── test_utils.py
│   ├── data/
│   │   ├── raw/                  # Raw network traffic data
│   │   │   ├── sample_network_data.csv
│   │   ├── processed/             # Preprocessed data files
│   │   │   ├── cleaned_data.csv
│   ├── notebooks/
│   │   ├── anomaly_detection_demo.ipynb  # Jupyter notebook example
├── examples/
│   ├── example_usage.py          # Example script demonstrating package usage
├── docs/
│   ├── README.md                 # Project documentation
│   ├── CONTRIBUTING.md           # Guidelines for contributors
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                 # GitHub Actions CI/CD workflow
├── setup.py                      # Package setup script
├── requirements.txt              # Dependencies
├── LICENSE                       # Open-source license
├── .gitignore                     # Ignore unnecessary files
```
