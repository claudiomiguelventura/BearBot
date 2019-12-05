import tweepy

from time import strftime
import keychain

auth = tweepy.OAuthHandler(keychain.api_key, keychain.api_secret_key)
auth.set_access_token(keychain.access_token, keychain.access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

current_time = strftime("%d/%m/%Y, %H:%M:%S")

api.update_status("Crontab ran. " + current_time)


