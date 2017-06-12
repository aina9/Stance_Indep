import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

X, y, c = [], [], [] 
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2),
                                    token_pattern=r'\b\w+\b',
                                    stop_words=['URL'])
encoder = LabelEncoder()
clf = MultinomialNB()

with open("../data/full_for_cat.txt") as f:
    for line in f:
        cols = line.split("\t")
        # tweet, class, lang
        X.append(cols[1]) ; y.append(cols[4]) ; c.append(cols[5].rstrip("\n"))
        
X = bigram_vectorizer.fit_transform(X).toarray()
print(y[:10])
y = encoder.fit_transform(y)
print(y[:10])

X_train, X_mid, y_train, y_mid, c_train, c_test = train_test_split(X, y, c)
X_test, y_test = [], []

for X, y, c in zip(X_mid, y_mid, c_test):
    if c == 'cat':
        X_test.append(X)
        y_test.append(y)

clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print(classification_report(y_test, predictions))
