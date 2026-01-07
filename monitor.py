import json
import paho.mqtt.client as mqtt
from pydantic import BaseModel


class TemperatureData(BaseModel):
    sensor_name  : str 
    temperature: float


def on_connect(client, userdata, flags, rc, properties):
    print("connected with result code", rc)

    client.subscribe ("temp")
    client.subscribe ("hum")


def on_message(client, userdata, msg ):

    # having in mind that the payload is in bytes so here it's converted to string

    text =msg.payload.decode("utf-8")

    if msg.topic == "temp":
        try: 
            # converts from json string to dictionary 
            data_dict= json.loads(text)

            #dict to validates obj
            data = TemperatureData(
                sensor_name=data_dict["sensor_name"],
                temperature=data_dict["temperature"]
            )

            print(data.sensor_name, "temperature:", round(data.temperature, 2))

        except Exception as e:
            print(f"Bad temp message: {text}")
            print(f"Error: {e}")
    else:
        print(f"Received on {msg.topic}: {text}")


if __name__ == "__main__":
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect ("localhost", 1883, 60)

    try:
        while client.loop() == 0:
            pass

    except KeyboardInterrupt:
        print("Monitor stopped.")
        client.disconnect()