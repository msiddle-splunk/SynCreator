import requests
import json
import time


def send2splunk(data, hec_url, hec_token):
    headers = {
        "Authorization": f"Splunk {hec_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "event": data,
        "index": "main",
        "sourcetype": "syncreator_event",
        "time": int(time.time()),
    }
    try:
        response = requests.post(hec_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error sending data to Splunk: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
