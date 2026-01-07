import time 
import random 
import json
import paho.mqtt.client as mqtt
from pydantic import BaseModel


class TemperaturesData(BaseModel):
    sensor_name: str
    temperature: float

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("Connected successfully to the broker.")
    else:
        print(f"Connection failed with code {rc}")

if __name__ == '__main__':
    sensor_name ="T2"


    # Create an MQTT client instance
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    # Set callback for connection
    client.on_connect = on_connect

    # Connect to the broker
    client.connect("localhost", 1883, 60)

    # Start the loop
    client.loop_start()

  

    try:
        while True:
            # Random temperature: 0 to 30
            temp_value = round(random.uniform(0, 30),2)

            #validate with pydantic
            data = TemperaturesData(sensor_name=sensor_name, temperature=temp_value)
           
            # Convert to JSON string (simple way)
            payload = json.dumps(data.model_dump())

            # Publish to "temp" topic
            client.publish("temp", payload)
            print("Published:", payload)

            time.sleep(2)

    except KeyboardInterrupt:
        print("Temperature1 stopped.")

    # Stop the loop and disconnect
    client.loop_stop()
    client.disconnect()