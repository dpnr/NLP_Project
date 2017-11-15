import glob
import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline


def model():
    count_vect = CountVectorizer()
    # from sklearn.datasets import fetch_20newsgroups
    # twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
    # print(twenty_train.target_names)
    dict={}
    dict["arson"]=1
    dict["attack"]=2
    dict["bombing"]=3
    dict["kidnapping"]=4
    dict["robbery"]=5


    trainX=[]
    trainY=[]
    testX=[]
    testY=[]


    for filename in os.listdir('texts/'):
        try:
            with open('texts/'+ filename) as file:
                trainX.append(file.read())
        except:
            pass
            # print(filename)
    for filename in os.listdir('answers/'):
        with open('answers/' + filename) as file:
            data=file.readlines()
            inc=data[1].split()[1].lower()
            trainY.append(dict[inc])


    # testX=trainX[-50:]
    # testY=trainY[-50:]
    # trainX=trainX
    # trainY=trainY
    # testX = map(lambda x: float(x), testX)
    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                          ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                               alpha=1e-3, random_state=42,
                                             max_iter=5, tol=None))])
    text_clf.fit(trainX, trainY)
    X_train_counts = count_vect.fit_transform(trainX)
    X_train_counts.shape
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    X_train_tfidf.shape
    # clf = MultinomialNB().fit(X_train_tfidf, trainY)
    # X_test_counts = count_vect.transform(testX)
    # X_test_tfidf = tfidf_transformer.transform(X_test_counts)
    # predicted = text_clf.predict(testX)
    return text_clf
    # for category in  predicted:
    #     print(category)
    # print(np.mean(predicted == testY))
# print(np.mean)


# model()
