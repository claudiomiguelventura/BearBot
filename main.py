import tweepy

from time import strftime

# Authenticate to Twitter
auth = tweepy.OAuthHandler("YMEJuRcmNnUQ06vROKnzmaryg", 
    "7JVktW2cZS9IkOJf03iOu6M14rMEb99EPLtt1UmE0sZOQFEKQg")
auth.set_access_token("1202246952257236992-WDDQ64H4RyGBb16imbPxgfHfVHuKVc", 
    "8mRczHPtEm1gVGuqgppOK0UCzla9uhHFNrF84PWVhgbwr")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

current_time = strftime("%d/%m/%Y, %H:%M:%S")

api.update_status("Crontab ran. " + current_time)


