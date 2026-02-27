# FraudGuard AI: Credit Card Spend Anomaly Detection

A premium machine learning system for detecting and explaining suspicious credit card spending behavior.

## 📊 Project Structure

- **`data/`**: Contains raw and processed transaction datasets.
- **`models/`**: Serialized machine learning models (Isolation Forest).
- **`scripts/`**: Core analysis pipeline and individual processing steps.
- **`plots/`**: Visualizations of anomalous spending patterns.
- **`templates/` & `static/`**: Dashboard frontend (HTML/CSS).
- **`app.py`**: Main Flask application entry point.

## 🚀 Getting Started

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Run the Analysis
Execute the full 5-step pipeline to process data, train models, and generate explainable results:
```bash
python scripts/full_pipeline.py
```

### 3. Launch the Dashboard
Start the premium "Security Command Center" dashboard:
```bash
python app.py
```
Then visit `http://127.0.0.1:5001` in your browser.

## 📋 Features
- **User-Specific Normalization**: Detects anomalies relative to a user's historical baseline.
- **Dual-Model Detection**: Integration of Isolation Forest and Local Outlier Factor (LOF).
- **Explainable AI**: Every flag comes with a human-readable reason (e.g., "Personal deviation", "Global outlier").
- **Premium UI**: Glassmorphic, dark-mode "Command Center" aesthetic.
