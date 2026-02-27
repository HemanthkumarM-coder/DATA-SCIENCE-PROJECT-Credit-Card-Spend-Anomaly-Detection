# 🛡️ FraudGuard AI: Credit Card Anomaly Detection Walkthrough

This project implements a professional-grade unsupervised learning system to detect and explain suspicious credit card spending behavior.

## 📋 5-Step Technical Workflow

### 1. Data Ingestion
- **Source**: Transaction-level spending data (100MB+ dataset).
- **Processing**: Structured over 50,000 transactions with timestamps, user IDs, and amounts.

### 2. Personal Context Normalization
- **Strategy**: Instead of a global baseline, we calculated **Per-User Normalization**.
- **Metric**: Computed individual Z-scores for every transaction to identify spending that is unusual *specifically for that user*.

### 3. Model Implementation (Unsupervised)
- **Isolation Forest**: Identified global outliers in the high-dimensional feature space (Amount, Quantity, Z-score).
- **LOF (Local Outlier Factor)**: Detected anomalies based on local density variations, identifying suspicious patterns that might look "normal" at a global scale.
- **Outcome**: Detected **~950 unique anomalies** across the test sample.

### 4. Interactive Visualization
- **Dynamic Charting**: Created a time-series visualization (`plots/anomalies_over_time.png`) showing perfectly-timed fraud alerts across the spending timeline.

### 5. AI Reasoning & Explainability
The system doesn't just flag transactions; it explains **why**:
- **Personal Outliers**: "Spending value is significantly higher than user average (Z=4.2)"
- **Global Outliers**: "Amount is a global outlier among all users"
- **Operational Flags**: "Unusually high quantity of items in a single transaction"

---

## 🎨 FraudGuard AI: Security Command Center
We have completely redesigned the interface from a simple page into a multi-pane **Security Command Center**:
- **Glassmorphism Design**: Using blurred backdrop filters and glowing accents for a modern, high-end feel.
- **Sidebar Architecture**: Organized navigation for Overview, Analysis, and System Compliance.
- **Dynamic Incident Feed**: Color-coded transaction logs with descriptive anomaly reasoning.
- **System Health Monitoring**: Integrated pulse animations for live scan status.

---

### 🚀 Usage Instructions
1. **Unify & Analyze**: Run `python scripts/full_pipeline.py` to execute all 5 steps in one command.
2. **Dashboard**: Run `python app.py` and visit `http://127.0.0.1:5001`.
