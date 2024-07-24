import requests
import json

# Adafruit IO credentials and API endpoint
username = 'aaaaaaaaaaaa'
key = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbb'
feed_key = 'test'
base_url = f'https://io.adafruit.com/api/v2/{username}/feeds/{feed_key}'

def publish_to_adafruit_io(value):
    try:
        # Create headers with API key
        headers = {
            'X-AIO-Key': key,
            'Content-Type': 'application/json'
        }
        
        # Create payload
        payload = {
            'value': value
        }

        # Send POST request to publish data
        response = requests.post(base_url + '/data', headers=headers, json=payload)

        # Check if request was successful
        if response.status_code == 201:
            print(f"Published value '{value}' to Adafruit IO")
        else:
            print(f"Failed to publish to Adafruit IO. Status code: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_latest_from_adafruit_io():
    try:
        # Create headers with API key
        headers = {
            'X-AIO-Key': key,
            'Accept': 'application/json'
        }

        # Send GET request to fetch latest feed data
        response = requests.get(base_url + '/data/last', headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            value = data['value']
            created_at = data['created_at']
            print(f"Latest value: {value} (created at {created_at})")
        else:
            print(f"Failed to fetch data from Adafruit IO. Status code: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
value_to_publish = 'Hello, Adafruit IO!'
publish_to_adafruit_io(value_to_publish)

print("Fetching latest data from Adafruit IO:")
fetch_latest_from_adafruit_io()
