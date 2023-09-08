





from pyyoutube import Api
api = Api(client_id="AIzaSyCO487FSltOzZTdqmoY3sc1KcPAMqZXGV8", client_secret="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")
# Get authorization url
AU = api.get_authorization_url()
print(AU)
# ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=id&redirect_uri=https%3A%2F%2Flocalhost%2F&scope=scope&state=PyYouTube&access_type=offline&prompt=select_account', 'PyYouTube')
# user to do
# copy the response url
# AT = api.generate_access_token(authorization_response="link for response")
# print(AT)
# AccessToken(access_token='token', expires_in=3599, token_type='Bearer')
channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items)

