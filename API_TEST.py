import requests

url = 'http://localhost:5000/generate_response'
data = {'user_send_input': 'Lets go to tonights summer festival'}
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
