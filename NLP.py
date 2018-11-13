import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
import gensim
from gensim import corpora
import re
import string as st



class NLP_Functions:
    def sentiment(self, tweets):
        # input: list of strings
        # output: list of ints
        sentiments = []
        for tweet in tweets:
            tweet = clean(tweet)
            sid = SentimentIntensityAnalyzer()
            score = sid.polarity_scores(tweet)
            sentiments.append(score['compound'])
        return sentiments

    def topics(self, tweets, ldamodel, num_words):
        # input:
        #     tweets: strings
        #     ldamodel: Lda model from trainLDA
        #     topics: integer number of topics to return per tweet
        #     num_words: integer number of words per topic
        # output:
        #     list of lists, each list within the list contains a tuple (topic, percentage)
        #     each list within the greater list is for each tweet
        to_return = []
        for tweet in tweets:
            topics_w_percents = ldamodel.print_topics(num_topics=1, num_words=num_words)
            percents = topics_w_percents[0][1].split()
            for_topics = [i for i in percents if i != "+"]
            percents = [float(i[:5]) for i in for_topics]
            for_topics = " ".join(word for word in for_topics)
            topics = re.findall('"([^"]*)"', for_topics)
            topics_percents_tuples = zip(topics, percents)
            topics_percents_tuples = list(topics_percents_tuples)
            to_return.append(topics_percents_tuples)
        return to_return

    def trainLDA(self, tweets):
        # input: list of strings
        # output: lda model trained on strings
        tweets_clean = [clean(tweet).split() for tweet in tweets]
        dictionary = corpora.Dictionary(tweets_clean)
        tweet_term_matrix = [dictionary.doc2bow(tweet) for tweet in tweets_clean]
        Lda = gensim.models.ldamodel.LdaModel
        ldamodel = Lda(tweet_term_matrix, num_topics=3, id2word=dictionary, passes=50)
        return ldamodel

    def clean(self, doc):
        # input: string
        # output: string
        lemma = WordNetLemmatizer()
        stop = set(stopwords.words('english'))
        exclude = set(string.punctuation)
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude or ch == "!")
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split()).split()
        link_free = [word for word in normalized if 'http' not in word]
        cleaned = " ".join(word for word in link_free)
        return cleaned