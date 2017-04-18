import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

X = [] ; y = []
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2),
                                    token_pattern=r'\b\w+\b',
                                    stop_words=['URL'])
encoder = LabelEncoder()
clf = MultinomialNB()

with open("../data/full.txt") as f:
    for line in f:
        cols = line.split("\t")
        # tweet, class
        X.append(cols[1]) ; y.append(cols[4])
        
X = bigram_vectorizer.fit_transform(X).toarray()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print(classification_report(y_test, predictions))
