import requests

headers = {
    'X-Auth-Token': '<GENERIERTER ZUGANGS TOKEN>',
    'X-User-Id': '<GENERIERTE USER ID>',
    'Content-type': 'application/json',
}

data = '{ "channel": "mi-android-ss-2020", "text": "This is a test! [REST-API]" }'

response = requests.post('https://chat.ur.de/api/v1/chat.postMessage', headers=headers, data=data)

print('Status-Code: ' + response.status_code)