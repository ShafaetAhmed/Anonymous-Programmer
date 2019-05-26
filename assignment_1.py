#sentiment analysis

try:
    import tweepy
    from textblob import TextBlob as tb
    import matplotlib.pyplot as plt

    consumer_key = 'e0JVkNMi4RX7E9qY662KRcrQg'
    consumer_secret = 'qiaFiwdlhpYQeZEaHEOF02nvWobIVW4NFca11mXEucdolMFJK4'

    access_token = '984039827443105793-Z6yLisl2W2vTbb9hHv5GU3Tx8CAOIhB'
    access_token_secret = 'wZYjXnvAG7ZKjNzN5uKf1WxnAFHyosYupkZ5MEQxkHw4E'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    search_term = input("enter a keyword:")
    no_of_tweets = int(input('enter number of tweets:'))

    tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(no_of_tweets)

    positive = 0
    negative = 0
    neutral = 0

    for tweet in tweets:
        analysis = tb(tweet.text)
        analysis_2 = analysis.sentiment.polarity
        if analysis_2 > 0:
            positive += 1
        elif analysis_2 < 0:
            negative += 1
        elif analysis_2 == 0:
            neutral += 1

    #printing out data
    print(str(positive) + ' positive')
    print(str(neutral) + ' neutral')
    print(str(negative) + ' negative')

    sentiments = [positive, neutral, negative]
    name = ['positive', 'neutral', 'negative']
    colour = ['lightgreen', 'gold', 'red']
    plt.title('People\'s reaction about' + ' ' + search_term + ' after analyzing' + ' ' + str(no_of_tweets) + ' tweets')
    plt.pie(sentiments, labels=name, autopct='%0.1f%%', shadow=True)
    plt.show()
except Exception as e: #handling exception
    print(e)
