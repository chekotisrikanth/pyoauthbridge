
1. cd pyoauthbridge/pyoauthbridge


2. install dependencies by running:
pip  install -r requirements.txt

3. create .env file with below contents. login details are needed only if we auto_login true. in this case code uses selenium to automatically login and get the token.
In this case token gets stored in token.json file with date time. for next run it will check if token is expired or not.

APP_ID=SAS-CLIENT1
APP_SECRET=
REDIRECT_URL=http://127.0.0.1/
BASE_URL=https://api.stocko.in
AUTO_LOGIN=True
LOGIN_ID=
LOGIN_PASSWORD=
TOTP_SECRET=

4. if you face any issues while using  selenium, you can use auto_login=false and once the server starts. hit url http://127.0.0.1/getcode
5. if you want to use this token for next time. store token in token.json file and update date_created. code will automatically use this token and check if it is expired within 24 hour.




