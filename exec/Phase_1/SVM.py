# SVM model 
import numpy as np
from scipy.sparse import hstack
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score

def get_accuracy(train, test):
    tweets = pd.concat([train, test], ignore_index = True, levels = None, keys = None)
    count_vectorizer = CountVectorizer(ngram_range=(1,3))
    vectorized_data = count_vectorizer.fit_transform(tweets.text)
    indexed_data = hstack((np.array(range(0,vectorized_data.shape[0]))[:,None], vectorized_data))
    print(tweets.head(5))
    targets = []
    for index, row in tweets.iterrows():
        if row['is_sarcasm'] == True: targets.append(1)
        else: targets.append(0)

    data_train, data_test, targets_train, targets_test = train_test_split(indexed_data, targets, test_size=0.3, random_state=0)
    data_train_index = data_train[:,0]
    data_train = data_train[:,1:]
    data_test_index = data_test[:,0]
    data_test = data_test[:,1:]

    clf = OneVsRestClassifier(svm.SVC(gamma=0.01, C=100., probability=True, class_weight='balanced', kernel='linear'))
    #cross validation
    #cross_val_scores = []
    #svm_sc = cross_val_score(clf, indexed_data, targets, cv=5)
    #cross_val_scores.append((svm_sc.mean(), svm_sc.std() * 2))

    clf_output = clf.fit(data_train, targets_train)

    nb = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    #nb_sc = cross_val_score(nb, indexed_data, targets, cv=5)
    #cross_val_scores.append((nb_sc.mean(), nb_sc.std() * 2))

    nb.fit(data_train, targets_train)

    
    

    return (clf.score(data_test, targets_test), nb.score(data_test, targets_test))
    #return cross_val_scores 




