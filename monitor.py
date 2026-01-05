import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties):
    print("connected with result code", rc)

    client.subscribe ("temp")
    client.subscribe ("hum")


def on_message(client, userdata, msg ):
    print(f"Received: {msg.topic} {msg.payload}")

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