from flask import Flask, render_template, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# Load the final analysis data
DATA_PATH = 'data/final_anomaly_analysis.csv'

def load_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        return df
    return None

@app.route('/')
def index():
    df = load_data()
    if df is None:
        return "Data not found. Please run the analysis scripts first."
    
    # Calculate Summary Stats
    total_transactions = len(df)
    total_anomalies = df['is_anomaly_combined'].sum()
    anomaly_rate = (total_anomalies / total_transactions) * 100
    
    # Get top 20 anomalies for display
    anomalies_list = df[df['is_anomaly_combined'] == 1].sort_values(by='Timestamp', ascending=False).head(50)
    anomalies_data = anomalies_list.to_dict('records')
    
    # Prepare chart data: Anomalies over time (hourly)
    df_sorted = df.sort_values('Timestamp')
    chart_data = df_sorted.resample('h', on='Timestamp')['is_anomaly_combined'].sum().reset_index()
    chart_labels = chart_data['Timestamp'].dt.strftime('%H:%M').tolist()
    chart_values = chart_data['is_anomaly_combined'].tolist()
    
    return render_template('index.html', 
                           total=total_transactions, 
                           anomalies=total_anomalies, 
                           rate=f"{anomaly_rate:.2f}%",
                           transactions=anomalies_data,
                           chart_labels=chart_labels,
                           chart_values=chart_values)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
