import requests

def send_get_request_with_bearer_token(token, entity="terms",user_id=1,prod_id=1):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(
        "http://localhost:8000/recommendations/",
        headers=headers,
        params=dict(entity=entity,user_id=user_id,prod_id=prod_id)
    )

    print('GET request')
    print('Response:', response.status_code)
    print('Response:', response.json())

token = 'widget_api_key'
# token = "acme_api_key" #only users
send_get_request_with_bearer_token(token, "companies" )