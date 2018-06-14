from os import listdir
from os.path import isfile, join
import sklearn.datasets as datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import KFold
import re
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.model_selection import KFold
class NaiveBayesBernoulli:

    def __init__(self):
        self.binaryVector = [0, 0, 0, 0, 0, 0, 0, 0]
        self.dictionaryWords = ['awful', 'bad', 'boring', 'dull',
                                 'effective', 'enjoyable', 'great', 'hilarious']
        self.dicWordCounts = {'awful':0, 'bad':0, 'boring':0, 'dull':0,
                                 'effective':0, 'enjoyable':0, 'great':0, 'hilarious':0}
        self.wordCount = 0
        self.conditionalProbabiltiesPostive = {'awful':0.0, 'bad':0.0, 'boring':0.0, 'dull':0.0,
                                 'effective':0.0, 'enjoyable':0.0, 'great':0.0, 'hilarious':0.0}
        self.conditionalProbabiltiesNegative = {'awful':0.0, 'bad':0.0, 'boring':0.0, 'dull':0.0,
                                 'effective':0.0, 'enjoyable':0.0, 'great':0.0, 'hilarious':0.0}

    def parseInputFileMultinomial(self):
        foldFolders = ['foldOne', 'foldTwo', 'foldThree', 'foldFour', 'foldFive', 'foldSix', 'foldSeven',
                       'foldEight', 'foldNine', 'foldTen']
        sumTotalCorrectPreds = 0
        for folder in foldFolders:
            trainDirectory = "C:\\Users\\herna\\PycharmProjects\\A3\\10Fold\\" + folder + "\\train\\"
            movie_reviews_dataset = datasets.load_files(trainDirectory)
            count_vect = CountVectorizer()
            X_train_counts = count_vect.fit_transform(movie_reviews_dataset.data)
            tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
            X_train_tf = tf_transformer.transform(X_train_counts)
            tfidf_transformer = TfidfTransformer()
            X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
            clf = MultinomialNB().fit(X_train_tfidf, movie_reviews_dataset.target)


            testDirectory = "C:\\Users\\herna\\PycharmProjects\\A3\\10Fold\\" + folder + "\\test\\"
            movie_reviews_dataset_test = datasets.load_files(testDirectory)
            X_new_counts = count_vect.transform(movie_reviews_dataset_test.data)
            X_new_tfidf = tfidf_transformer.transform(X_new_counts)
            predicted = clf.predict(X_new_tfidf)
            correctPred = 0
            for review, category in zip(movie_reviews_dataset_test.target, predicted):
                if movie_reviews_dataset.target_names[review]  == movie_reviews_dataset.target_names[category]:
                    correctPred +=1
                # print('%r => %s' % (movie_reviews_dataset.target_names[review] ,movie_reviews_dataset.target_names[category]))
            print('Correct: ', correctPred)
            print('Accuracy: ', correctPred / 200)
            sumTotalCorrectPreds += correctPred
        print('Total Correct: ', sumTotalCorrectPreds)
        print('Total Accuracy: ', sumTotalCorrectPreds / 2000)


    def parseInputFileBernoulli(self):
        foldFolders = ['foldOne', 'foldTwo', 'foldThree', 'foldFour', 'foldFive', 'foldSix', 'foldSeven',
                       'foldEight', 'foldNine', 'foldTen']
        sumTotalCorrectPreds = 0
        for folder in foldFolders:
            trainDirectory = "C:\\Users\\herna\\PycharmProjects\\A3\\10Fold\\" + folder + "\\train\\"
            movie_reviews_dataset = datasets.load_files(trainDirectory)
            count_vect = CountVectorizer()
            X_train_counts = count_vect.fit_transform(movie_reviews_dataset.data)
            tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
            X_train_tf = tf_transformer.transform(X_train_counts)
            tfidf_transformer = TfidfTransformer()
            X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
            clf = BernoulliNB().fit(X_train_tfidf, movie_reviews_dataset.target)


            testDirectory = "C:\\Users\\herna\\PycharmProjects\\A3\\10Fold\\" + folder + "\\test\\"
            movie_reviews_dataset_test = datasets.load_files(testDirectory)
            X_new_counts = count_vect.transform(movie_reviews_dataset_test.data)
            X_new_tfidf = tfidf_transformer.transform(X_new_counts)
            predicted = clf.predict(X_new_tfidf)
            correctPred = 0
            for review, category in zip(movie_reviews_dataset_test.target, predicted):
                if movie_reviews_dataset.target_names[review]  == movie_reviews_dataset.target_names[category]:
                    correctPred +=1
                # print('%r => %s' % (movie_reviews_dataset.target_names[review] ,movie_reviews_dataset.target_names[category]))
            print('Correct: ', correctPred)
            print('Accuracy: ', correctPred / 200)
            sumTotalCorrectPreds += correctPred
        print('Total Correct: ', sumTotalCorrectPreds)
        print('Total Accuracy: ', sumTotalCorrectPreds / 2000)

naiveBayesPython = NaiveBayesBernoulli()
# naiveBayesPython.parseInputFileMultinomial()
naiveBayesPython.parseInputFileBernoulli()