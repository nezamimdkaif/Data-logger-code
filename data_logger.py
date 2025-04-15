# 📦 Import Libraries
import random
import csv
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import time

# 📌 Function to Simulate Sensor Data
def get_sensor_data():
    temperature = round(random.uniform(20.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 80.0), 2)
    return temperature, humidity

# 📌 Initialize CSV File with Header (if not exists)
def init_csv():
    with open("sensor_log.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)"])

# 📌 Function to Log Data to CSV
def log_data_to_csv():
    temp, hum = get_sensor_data()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sensor_log.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temp, hum])

# 📌 Function to Plot Data using Matplotlib
def plot_data():
    data = pd.read_csv("sensor_log.csv")
    plt.plot(data["Timestamp"], data["Temperature (°C)"], label='Temperature (°C)', marker='o')
    plt.plot(data["Timestamp"], data["Humidity (%)"], label='Humidity (%)', marker='x')
    plt.xticks(rotation=45)
    plt.xlabel("Timestamp")
    plt.ylabel("Values")
    plt.legend()
    plt.tight_layout()
    plt.show()

# 📌 Main Function
if __name__ == "__main__":
    init_csv()  # run once to initialize CSV

    # Simulate and log data 10 times (you can increase this)
    for _ in range(10):
        log_data_to_csv()
        time.sleep(1)  # 1-second delay between readings

    # Plot the logged data
    plot_data()
