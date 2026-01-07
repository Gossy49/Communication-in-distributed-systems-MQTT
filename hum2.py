import time
import random 
import json
import paho.mqtt.client as mqtt
from pydantic import BaseModel

class HumidityData(BaseModel):
    sensor_name: str
    humidity: float

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print(f" Connected sucessfully to the broker")
    else:
        print (f"Connection failed with code {rc}")


if __name__ == "__main__":
    sensor_name = "H2"

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect

    client.connect("localhost",1883, 60)
    client.loop_start()

    try:
        while True:
            
            #produce random humudity values between 20to 100
            hum_value = round(random.uniform(20,100),2)

            #to validate with pydantic
            data = HumidityData(sensor_name=sensor_name,humidity= hum_value)

            #convert to Json string
            payload = json.dumps(data.model_dump())


            #publish to "hum" topic 
            client.publish("hum",payload)
            print(f"Published: {payload}")

            time.sleep(2)

    except KeyboardInterrupt:
            print("Humudity2 stopped.")

    # Stop the loop and disconnect
    client.loop_stop()
    client.disconnect()


