import tweepy
import time

import requests
import os

consumer_key = '2APBd6vkznDiVoo0k161LRhhb'
consumer_secret = '1hkrqZmGQlVvgyLUs2kuATqEmrGm0llJiKUwb58cMrPWe1cKwC'

access_token = '1036225992979824641-gLHNhDn82vWyNlsVBrccyeF1qruFnV'
access_token_secret = 'skVcLkZ8p6vlAcrf7moy0u9Wo84OGXs3FAgjnE2s7qKwL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print (user.name + " | " + str(user.id))


# Sigue a todos los que te siguen
def follow_who_follow():
        for followers in tweepy.Cursor(api.followers).items():
            followers.follow()
            print ("Followed everyone that is following " + user.name)

# Rtea y dale fav a tweets por palabras clave
def rt_fav_keyword():
    numberOfTweets = 3
    search = "Alain De Botton"

    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet()
            tweet.favorite()
            print ('Retweeted the tweet')

        except tweepy.TweepError as e:
            print (e.reason)

        except StopIteration:
            break
    
def reply_to_keyword():
    tweetId = "289429998"
    username = "DaniHeatCrazy"
      
    phrase = "Máquina"
      
    for tweet in tweepy.Cursor(api.search,   search).items(numberOfTweets):
        try:
            #tweetId = tweet.user.id
            #username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
            print ("Replied with " + phrase)
              
        except tweepy.TweepError as e:
            print (e.reason)
              
        except StopIteration:
            break
            
def get_home_timeline():
    public_tweets = api.home_timeline()
    count = 1
    for tweet in public_tweets:
        print("Tweet " + str(count))
        count += 1
        print(tweet.text + "\n")
        
def tweet_image(url, message):
    print ("principio de tweet_image    ")
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        print("entra en el if")
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        print("antes del update")
        api.update_with_media(filename, status=message)
        print("despues del update")
        os.remove(filename)
        print("IMAGEN TWITTEADA")
    else:
        print (request.status_code)
        print("Unable to download image")
                                
#followers =  api.followers(user)
#direct_messages = api.direct_messages()
# post a tweet --> api.update_status('prueba1')
        
def main():
    print ("main Function started \n-----\n")
    count = 0
    while True:
        time.sleep(3)
        for direct_message in api.direct_messages():
            count += 1
            print ("\nIteration: " + str(count))
            try:

                api.update_status(direct_message.text)
                #api.update_status(direct_message.entities["urls"][0]["expanded_url"])
                #api.update_with_media(direct_message.entities["urls"][0]["expanded_url"], direct_message.text)

                """
                if direct_message.entities["urls"]:
                    print ("tiene imagen\n")
                    #print (direct_message.entities["urls"])
                    tweet_image(direct_message.entities["urls"][0]["expanded_url"], direct_message.text)
                else:

                """

            except tweepy.TweepError as e:
                print (direct_message.text)
                """
                if direct_message.entities["urls"]:
                    print ("tiene imagen")
                    print (direct_message.entities["urls"])
                """

                print (e.reason)
                #print (direct_message)
                #print ("Tweet duplicado: no tweeteado.")

main()