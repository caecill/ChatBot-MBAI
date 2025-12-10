from textblob import TextBlob

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    
    if polarity > 0.3:
        return "positif"
    elif polarity < -0.3:
        return "negatif"
    else:
        return "netral"
