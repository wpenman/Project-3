# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

#https://twitter.com/wadepenman-Twitter URL

import tweepy

# Unique code from Twitter
access_token = "163323944-IhIvobqT95HKnqbvKhRW6YuLtCYeq9JkCSjpJy4E"
access_token_secret = "jD7xEJ5hIZKCoANtuhsaqyRtX1vPK2G0eGmSzwWr159oQ"
consumer_key = "DQfU2Y1xBCBbGXgRXHWGnrXDa"
consumer_secret = "YwHUOxkaWUfffhuSt8eUfdZkAeNzEYVnOsuCJDy7yg9l1TzHIe"

# Boilerplate code here
auth = tweepy.OAuthHandler("DQfU2Y1xBCBbGXgRXHWGnrXDa", "YwHUOxkaWUfffhuSt8eUfdZkAeNzEYVnOsuCJDy7yg9l1TzHIe")
auth.set_access_token("163323944-IhIvobqT95HKnqbvKhRW6YuLtCYeq9JkCSjpJy4E", "jD7xEJ5hIZKCoANtuhsaqyRtX1vPK2G0eGmSzwWr159oQ")

api = tweepy.API(auth)
img = "dwight.jpg"
hashtag_txt = "I love the office! #UMSI-206 #Proj3"
api.update_with_media(img, status=hashtag_txt)

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")