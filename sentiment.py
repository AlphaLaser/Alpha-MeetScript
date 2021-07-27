import text_extract

sentiments = []

for my_sentiment in text_extract.conversation.messages :
    sentiments.append(my_sentiment.sentiment)


