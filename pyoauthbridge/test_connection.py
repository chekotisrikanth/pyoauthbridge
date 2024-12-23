from connect2 import Connect
from flask import Flask, request, redirect


# Replace with your actual credentials
app_id = "SAS-CLIENT1"
app_secret = "your client_secret"
redirect_url = "http://127.0.0.1/"
base_url = "https://api.stocko.in"
client_id = "your client_id"

#access_token = "YOUR_ACCESS_TOKEN"  # Or obtain it using conn.get_access_token()

conn = Connect(app_id, app_secret, redirect_url, base_url)

access_token = conn.get_access_token()

print('access_token ',access_token)

#access_token = "NQOGiY16aFrKqRque8HMg5TVCGilCaiSnWDMITIctQk.VIOU6sRIYAsxdPSJqRkzl4b9x32JAqzpLAJ0_4UDxSw"
if access_token:
    conn.set_access_token(access_token)

payload = {
    'client_id': client_id
}
profile_res = conn.fetch_profile(payload)
print(profile_res)




