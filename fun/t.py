import requests

def send_get_request_with_bearer_token(url, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Request succeeded
        print('GET request successful')
        print('Response:', response.json())
    else:
        # Request failed
        print('GET request failed')
        print('Response:', response.text)

# Example usage
url = 'http://localhost:8000/api/V1/users/1/'
token = 'your_bearer_token'

send_get_request_with_bearer_token(url, token)