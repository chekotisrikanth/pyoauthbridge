from connect2 import Connect
from flask import Flask, request, redirect
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
app_id = os.getenv('APP_ID')
app_secret = os.getenv('APP_SECRET')
redirect_url = os.getenv('REDIRECT_URL')
base_url = os.getenv('BASE_URL')
login_id = os.getenv('LOGIN_ID')
login_pwd = os.getenv('LOGIN_PASSWORD')
totp_secret = os.getenv('TOTP_SECRET')
auto_login = os.getenv('AUTO_LOGIN').lower() == 'true'


conn = Connect(app_id, app_secret, redirect_url, base_url,login_id,login_pwd,totp_secret)

access_token = conn.get_access_token(auto_login)

print('access_token ',access_token)


if access_token:
    conn.set_access_token(access_token)

payload = {
    'client_id': login_id  # Example payload
}
profile_res = conn.fetch_profile(payload)
print(profile_res)

script_searchResp = conn.search_scrip({'key': 'NIFTY 50'})
print(script_searchResp)