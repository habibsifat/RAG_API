import requests
import time

url = "http://0.0.0.0:8000/ask"
#data = {"question": "What is the full form of USA?"}

data = {"question": "What were two key legislative achievements of the Civil Rights Movement in the 1960s?"}



start_time = time.time()
response = requests.post(url, json=data)
end_time = time.time()
print("\n\nResponse:")
print(response.json())
print(f"\n\nTime taken: {end_time - start_time} seconds\n\n")