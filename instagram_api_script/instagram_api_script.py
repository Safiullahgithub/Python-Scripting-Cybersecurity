import requests

# Instagram API credentials
app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'
access_token = 'YOUR_ACCESS_TOKEN'

# User ID of the Instagram account
user_id = 'YOUR_USER_ID'

# Endpoint for user profile
url = f'https://graph.instagram.com/{user_id}?fields=id,username&access_token={access_token}'

# Send GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    user_data = response.json()
    print(f"User ID: {user_data['id']}")
    print(f"Username: {user_data['username']}")
else:
    print("Failed to retrieve user data")
