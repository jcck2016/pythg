user_input = input("Enter your tweet: ")
max_tweets = 140
user_tweet_count = len(user_input)


if user_tweet_count <= max_tweets:
    print("***************************************************")
    print(f"Your {user_tweet_count} character(s) tweet will work !!!!! .... still have {max_tweets-user_tweet_count} character(s) left !")

if user_tweet_count > max_tweets:
    print("***************************************************")
    print(f"Your {user_tweet_count} character(s) tweet is too long !!!!! ... over by {user_tweet_count-max_tweets} character(s)")


'''
commenters()
'''
