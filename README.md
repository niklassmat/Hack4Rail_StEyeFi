# Hack4Rail_StEyeFi
A hackathon project to improve cleanliness and crowd management at railway stations using real-time data analysis.

## 🚀 Project Overview

As part of a hackathon challenge, our team is working on a data-driven solution that utilizes **PAX_Counter** devices—passive sensors that detect nearby devices (e.g., smartphones)—to estimate the number of people in the vicinity of a train station.

Our goal: **detect unusually high crowd activity** near bins or specific station zones to **trigger alerts for service staff** to clean and maintain these areas proactively.

## 🧠 What We’re Building

We are developing a pipeline that:
- Ingests PAX_Counter data (device detection counts with timestamps and locations)
- Analyzes daily and weekly patterns per station and sensor
- Detects **anomalies** where people density exceeds expected thresholds
- Raises **alerts** to prompt cleaning or inspection actions

This allows for:
- Cleaner stations 🧼
- Smarter staff deployment 🚶‍♀️
- Improved passenger experience 🚆

## 📁 Repository structure
> The `process_data` folder contains core transformation logic. The script group_master_data.py is meant to group the master_data file by station_id to get the unique stations. The script process_pax_data.py loads and merges sensor data from multiple CSV files, processes timestamps to extract weekday information, and filters data for a specific station. It then calculates average daily passenger counts per weekday and outputs a summary table including upper and lower bounds for anomaly detection.
> 
