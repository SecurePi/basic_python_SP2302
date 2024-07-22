import requests

def https_get_request(url):
    try:
        # Send HTTPS GET request
        response = requests.get(url)
        
        # Print the response status code and content
        print(f"Response Status Code: {response.status_code}")
        print("Response Content:")
        print(response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
url = "https://google.com"
https_get_request(url)
