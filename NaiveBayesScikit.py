from os import listdir
from os.path import isfile, join
import sklearn.datasets as datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
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

    def parseInputFile(self):
        self.positiveFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive')
                     if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\positive', f))]
        self.negativeFiles = [f for f in listdir('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative')
                     if isfile(join('C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles\\negative', f))]
        featureVectorsNegative = []

        negativeMovieDirectory = "C:\\Users\\herna\\PycharmProjects\\A2\\reviewFiles"
        movie_reviews_dataset = datasets.load_files(negativeMovieDirectory)
        # print(movie_reviews_negative)
        # print(movie_reviews_dataset.target_names)
        # print(len(movie_reviews_dataset.data))
        # print(movie_reviews_dataset.data[0])
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(movie_reviews_dataset.data)
        tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
        X_train_tf = tf_transformer.transform(X_train_counts)
        print(X_train_tf.shape)
       


naiveBayesPython = NaiveBayesBernoulli()
naiveBayesPython.parseInputFile()