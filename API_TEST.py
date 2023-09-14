import requests

url = 'http://localhost:5000/generate_response'
#url = 'http://127.0.0.1:5000/generate_response'
#url = 'http://172.28.0.12:5000/generate_response'
#url = 'https://68fc-34-75-7-187.ngrok-free.app/generate_response'

data = {'user_send_input': 'Lets go on a date then'}
response = requests.post(url, json=data)

print("Request Status Code:", response.status_code)
print("Response Text:", response.text)

try:
    if response.status_code == 200:
        response_json = response.json()
        if 'response' in response_json:
            response_text = response_json['response']
            print("Generated Response:", response_text)
        else:
            print("Response JSON doesn't contain 'response' key:", response_json)
    else:
        print("Error Response")
except Exception as e:
    print("Exception during response handling:", e)
