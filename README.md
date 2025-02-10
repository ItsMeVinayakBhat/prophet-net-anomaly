# Propano 🚀
A lightweight, open-source network anomaly detection package leveraging **Facebook Prophet** for time-series modeling.  
🔹 **Key Features**:  
✔ Anomaly detection based on Prophet’s upper/lower confidence bounds  
✔ **Persistence & Proximity Analysis** to minimize false positives  
✔ Optimized for network data: traffic volume, packet loss, DDoS detection  
✔ Sensitivity options to tune the model  

📌 **Getting Started**
```bash
pip install propano
```
**Project Structure**
```bash
propano/
├── src/
│   ├── propano/
│   │   ├── __init__.py
│   │   ├── anomaly_detector.py   # Core anomaly detection logic
│   │   ├── cli.py                # Command-line interface (CLI)
│   │   ├── utils.py              # Helper functions (e.g., data preprocessing)
│   │   ├── visualization.py      # Functions for plotting anomalies
│   ├── tests/
│   │   ├── test_anomaly_detector.py  # Unit tests
│   │   ├── test_cli.py               # Unit tests for CLI
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
├── .gitignore                    # Ignore unnecessary files
```


**Useful Commands for the Developers**

*To install the dependencies*
```
pip install -r requirements.txt
```

*To Build and Upload to PyPI*

```
python3 -m build
```

```
twine upload dist/*
```

*To Uninstall and Reinstall the propano*

```
pip uninstall propano -y
```

```
pip install .
```
