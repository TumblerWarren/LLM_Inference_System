import requests

url = 'http://localhost:5000/generate_response'
data = {'user_input': 'I wanna do that after this, will it be okay'}
response = requests.post(url, json=data)

if response.status_code == 200:
    response_text = response.json()['response']
    print("Generated Response:", response_text)
else:
    print("Error:", response.json()['error'])
