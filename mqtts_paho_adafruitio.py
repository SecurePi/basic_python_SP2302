# Example of using the MQTT client class to publish feed values.
# Based on m3y54m paho mqtt adafruit IO codes
#Github Link: https://github.com/m3y54m/paho-mqtt-client

# Import standard python modules.
import random
import sys
import time

import ssl
import paho.mqtt.client as mqtt

TLS_CA = "./certs/ca-certificates.crt"
TLS_V  = ssl.PROTOCOL_TLSv1_2

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'bbbbbbbbbbbbbbbbbbbbbbbbbbb'

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'test'


# Connected callback functions and it calls after the SP2302 has connected.
def connected(client, userdata, flags_dict, result):
    print('Connected to Adafruit IO!')

# Disconnected callback function when SP2302 has been disconnected with Adafruit IO.
def disconnected(client, userdata, rc):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)


# Create an MQTT client.
client = mqtt.Client()
# Enable TLS and use port 8883
# Disable TLS and use port 1883
client.tls_set(ca_certs=TLS_CA, tls_version=TLS_V)
#client.tls_set_context()
# Enter Adafruit IO from getting the username and IO key
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected

# Connect to the Adafruit IO server.
client.connect('io.adafruit.com', 8883, 60)

#Starts the loop and works in the background.
client.loop_start()
# Now send new values every 10 seconds.
print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
while True:
    value = random.randint(0, 100)
    print('Publishing {0} to DemoFeed.'.format(value))
    client.publish('{0}/feeds/{1}'.format(ADAFRUIT_IO_USERNAME, FEED_ID), value)
    time.sleep(10)
