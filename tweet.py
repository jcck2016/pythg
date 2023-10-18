user_input = input("Enter your tweet: ")
max_tweets = 140
user_tweet_count = len(user_input)


if user_tweet_count <= max_tweets:
    print("***************************************************")
    print(f"Your {user_tweet_count} character(s) tweet will work !!!!! .... still have {140-user_tweet_count} character(s)")

if user_tweet_count > max_tweets:
    print("***************************************************")
    print(f"Your {user_tweet_count} character(s) tweet is too long !!!!! ... more by {user_tweet_count-140} character(s)")
