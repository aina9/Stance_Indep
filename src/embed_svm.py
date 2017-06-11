import word2vec
import numpy as np
from nltk.tokenize import TweetTokenizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

X = [] ; y = []

es = word2vec.load("../embeddings/es.vec", kind='txt')
ca = word2vec.load("../embeddings/ca.vec", kind='txt')

tok = TweetTokenizer()
encoder = LabelEncoder()
lr = LogisticRegression()
mlp = MLPClassifier(activation='tanh', hidden_layer_sizes=(100))

def build_vector(tweet, lang):
    model = es if lang == 'spa' else ca
    out = []
    for i in tok.tokenize(tweet):
        try:
            out.append(model[i])
        except KeyError:
            out.append(model['OOV'])

    arr = [sum(x) for x in zip(*out)]
    if len(arr) == 0:
        return np.zeros(50)

    return arr


with open("../data/full.txt") as f:
    for line in f:
        cols = line.split("\t")
        # vector, class
        X.append(build_vector(cols[1], cols[5])) ; y.append(cols[4])

y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)
lr.fit(X_train, y_train)
predictions = lr.predict(X_test)

print(classification_report(y_test, predictions))
