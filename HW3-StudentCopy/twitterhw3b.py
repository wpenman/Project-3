# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob 

access_token = "163323944-IhIvobqT95HKnqbvKhRW6YuLtCYeq9JkCSjpJy4E"
access_token_secret = "jD7xEJ5hIZKCoANtuhsaqyRtX1vPK2G0eGmSzwWr159oQ"
consumer_key = "DQfU2Y1xBCBbGXgRXHWGnrXDa"
consumer_secret = "YwHUOxkaWUfffhuSt8eUfdZkAeNzEYVnOsuCJDy7yg9l1TzHIe"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

polar_sum = 0
polar_count = 0
sub_sum = 0
sub_count = 0

public_tweets = api.search('#happy')
for tweet in public_tweets:
	blob = TextBlob(tweet.text)
	print(blob)
	sent = blob.sentiment
	polarity = sent.polarity
	subjectivity = sent.subjectivity
	polar_sum += polarity
	polar_count += 1
	sub_sum += subjectivity
	sub_count += 1


print("Average subjectivity is", (sub_sum/sub_count))
print("Average polarity is", (polar_sum/polar_count))
