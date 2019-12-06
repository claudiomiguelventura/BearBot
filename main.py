import tweepy

from time import strftime
import keychain

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

auth = tweepy.OAuthHandler(keychain.api_key, keychain.api_secret_key)
auth.set_access_token(keychain.access_token, keychain.access_token_secret)

api = tweepy.API(auth)
#Mostrar ao Bagagem
auth_ok = False

try:
    api.verify_credentials()
    print("Authentication OK")
    auth_ok = True
except:
    print("Error during authentication")
    auth_ok = False

if auth_ok:
  current_time = strftime("%d/%m/%Y, %H:%M:%S")
  #api.update_status("Crontab ran. " + current_time)
  api.update_status(str(sys.argv[1]))

