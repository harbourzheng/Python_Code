import twitter 

twitter_search = twitter.Twitter(domain=“search.twitter.com”)
trends = twitter_search.trends()
[trends['name'] for trend in trends['trends']]

