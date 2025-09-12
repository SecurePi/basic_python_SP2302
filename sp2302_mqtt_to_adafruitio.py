# sp2302_mqtt_to_adafruitio.py

import time
import paho.mqtt.client as mqtt
import random

# --- Adafruit IO MQTT Configuration ---
ADAFRUIT_IO_USERNAME = 'bbbbbbb'
ADAFRUIT_IO_KEY = 'aaaaaaa'
ADAFRUIT_IO_FEED = 'sensor1'

MQTT_BROKER = 'io.adafruit.com'
MQTT_PORT = 1883
MQTT_TOPIC = f"{ADAFRUIT_IO_USERNAME}/feeds/{ADAFRUIT_IO_FEED}"

# --- Bind MQTT client to eth0 explicitly (optional) ---
MQTT_LOCAL_BIND_IP = '10.0.1.69'  # eth0 IP (Internet-facing)

client = mqtt.Client()
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Optional: bind to eth0 to ensure traffic doesn't go through eth1
client.bind_address = MQTT_LOCAL_BIND_IP

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

def main():
    print(f"[✓] Publishing data to Adafruit IO topic: {MQTT_TOPIC}")
    while True:
        simulated_value = random.randint(0, 100)
        client.publish(MQTT_TOPIC, simulated_value)
        print(f"[>] Sent: {simulated_value}")
        time.sleep(5)

if __name__ == "__main__":
    main()