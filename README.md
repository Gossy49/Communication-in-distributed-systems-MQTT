# MQTT Sensor Network 

This project simulates a network of MQTT sensors:
- Temperature sensors: T1, T2 publish to topic `temp` (0–30)
- Humidity sensors: H1, H2 publish to topic `hum` (20–100)

A monitoring unit subscribes to both topics, validates incoming JSON using Pydantic,
and prints values with the sensor name.

## Requirements
- Mosquitto MQTT broker
- Python 3
- Packages from `requirements.txt`

## Setup
Start Mosquitto (if not already running):
```bash
sudo systemctl start mosquitto

## Run
Monitor : python monitor.py
sensors: python temp1.py
         python temp2.py
         python hum1.py
         python hum2.py