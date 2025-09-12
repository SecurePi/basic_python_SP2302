# sp2302_modbus_to_adafruitio_mqtt.py

import time
import paho.mqtt.client as mqtt
from pymodbus.client import ModbusTcpClient

# --- Modbus TCP Configuration ---
MODBUS_DEVICE_IP = '127.0.0.1'
MODBUS_PORT = 502
MODBUS_UNIT_ID = 1
MODBUS_REGISTER_ADDR = 0
REGISTER_COUNT = 1

# --- Adafruit IO MQTT Config ---
ADAFRUIT_IO_USERNAME = 'bbbbbbbb'
ADAFRUIT_IO_KEY = 'aaaaaaa'
ADAFRUIT_IO_FEED = 'sensor2'

MQTT_BROKER = 'io.adafruit.com'
MQTT_PORT = 1883
MQTT_TOPIC = f"{ADAFRUIT_IO_USERNAME}/feeds/{ADAFRUIT_IO_FEED}"
POLL_INTERVAL = 10  # seconds

# --- MQTT Setup ---
client = mqtt.Client()
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

def read_modbus_register():
    modbus_client = ModbusTcpClient(MODBUS_DEVICE_IP, port=MODBUS_PORT)
    if not modbus_client.connect():
        print("[X] Modbus connection failed.")
        return None
    try:
        result = modbus_client.read_holding_registers(MODBUS_REGISTER_ADDR, REGISTER_COUNT, unit= MODBUS_UNIT_ID)
        if result.isError():
            print("[!] Modbus read error")
            return None
        return result.registers[0]
    except Exception as e:
        print(f"[!] Modbus exception: {e}")
        return None
    finally:
        modbus_client.close()

def main():
    print("[✓] Starting Modbus to Adafruit IO MQTT bridge")
    while True:
        value = read_modbus_register()
        if value is not None:
            client.publish(MQTT_TOPIC, str(value))
            print(f"[>] Published to {MQTT_TOPIC}: {value}")
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
