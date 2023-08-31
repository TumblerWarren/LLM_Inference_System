import requests

url = 'http://localhost:5000/generate_response'
data = {'user_send_input': 'oh,lets get ready its already evening'}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Response Text:", response.text)
    '''
    response_text = response.json()['response']
    print("Generated Response:", response_text)'''
else:
    print("Error:", response.json()['error'])
