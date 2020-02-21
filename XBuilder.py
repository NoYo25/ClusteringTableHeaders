# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:17:07 2019

@author: Nora
"""
import tensorflow as tf
from featuresExtractor.featureExtractor import FeatureExtractor
from featuresExtractor.syntacticFeatureExtractor import SyntacticFeatureExtractor

class XBuilder:
    def __init__(self, featureExtractor):
        assert isinstance(featureExtractor, FeatureExtractor)
        self.featureExtractor = featureExtractor

    def get_max_length(se, X):
        max_len = 0
        for i in range(len(X)):
            if len(X[i]) > max_len:
                max_len = len(X[i])
        return max_len


    def get_X(self, input_str_lst):
        X = [self.featureExtractor.get_features_from_word(s) for s in input_str_lst]
        #max_len = max([sublist[-1] for sublist in X])
        max_len = self.get_max_length(X)
        X = tf.keras.preprocessing.sequence.pad_sequences(maxlen=max_len, sequences=X, padding="post", value=0.0, dtype='float32')

        print(X.shape)
        return X


if __name__ == '__main__':
    lst = ["Article_Title", "Article_Year", "Article_FirstAuthorSurname", "PaperContact_Surname", "PaperContact_Email",
           "Article_Journal", "Article_DOI", "Data_DOI", "DataProvider_Title", "DataProvider_Surname",
           "DataProvider_FirstName", "DataProvider_MiddleInitials", "DataProvider_Email", "DataProvider_Institute",
           "DataProvider_Department", "Additional_Authors", "Number_of_Studies", "Total_Number_ofSites",
           "Total_Number_ofSpecies", "Entire Community", "Notes", "BibKey", "Data From Paper",
           "Other soil organisms sampled", "file"]
    builder = XBuilder(SyntacticFeatureExtractor())
    X = builder.get_X(lst)
    print(X.shape)
