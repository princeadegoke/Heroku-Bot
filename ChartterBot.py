# Dependencies
import tweepy
import time

# Twitter API Keys
consumer_key = "md27jI2cdRGQ5QJrC9GrZnjfj"
consumer_secret = "dp2ujQmPbGKDJO1UTx3S3kMdApXWz91XDMaLL1Ti92HygMrJVg"
access_token = "943270787640852485-AMbIDMXo65N5tVrEPs5TJvVlU9c2faJ"
access_token_secret = "lFoISe9o4VujzhvqWosuzWCS1uK2Ax7AeinI5r5mDsYG9"

# Create quotes to tweet
quote_list = []


# Create function for tweeting
def QuoteItUp(quote_num):

counter = 0


    
    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
    # Tweet a random quote
    api.update_status(random.choice(happy_quotes))
    
    # Print success message
    print("Tweeted successfully, sir!") 
    
    # Set timer to run every minute

while(counter < 15):
    HappyItUp()
    counter = counter + 1
    time.sleep(60)