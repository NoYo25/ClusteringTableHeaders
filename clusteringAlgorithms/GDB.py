import numpy as np
import pandas as pd

from XBuilder import XBuilder
from config import *
from clusteringAlgorithms.clusterAlgorithm import ClusterAlgorithm
from distances.cosineDistanceCalculator import CosineDistanceCalculator
from featuresExtractor.syntacticFeatureExtractor import SyntacticFeatureExtractor


class GDB(ClusterAlgorithm, CosineDistanceCalculator):
    def __init__(self, params):
        ClusterAlgorithm.__init__(self, params)
        assert "distance_threshold" in params, "distance_threshold must be in the params dict!"
        self.distance_threshold = params["distance_threshold"]

        assert "words" in params and isinstance(params["words"], list), \
            "list of words(strings) must be in params dictionary!"
        self.words = params["words"]

        assert "distance_file_path" in params and isinstance(params["distance_file_path"], str), \
            "distance_file_path must be in params dictionary!"
        self.distance_file_path = params["distance_file_path"]


    def __get_clusters(self, df2, words):
        # words are sorted as in X features matrix
        taken = []

        clusters = {}

        clusters_n = 0

        for word1 in words:
            cluster_words = []

            if word1 in taken:
                continue

            cluster_words = cluster_words + [word1]
            taken = taken + [word1]

            for word2 in words:
                if word1 == word2:
                    continue

                if df2[word1][word2] and word2 not in taken:
                    cluster_words = cluster_words + [word2]
                    taken = taken + [word2]

            clusters.update({clusters_n: cluster_words})
            clusters_n = clusters_n + 1

        assert len(taken) == len(words)
        return clusters, clusters_n

    def run(self, plot=False):
        X = self.params["X"]
        assert X.shape[0] == len(self.words), \
            "X features matrix must have the first dimension = length of words list!"

        dist_matrix = self.calculate_distances(X)
        temp_bool = dist_matrix < self.distance_threshold
        df2 = pd.DataFrame(temp_bool, index=self.words, columns=self.words)
        clusters, clusters_n = self.__get_clusters(df2, self.words)

        if plot:
            self.calculate_distances_full_view(X=X, index=self.words, columns=self.words, distance_file_path=self.distance_file_path)

        return clusters


if __name__ == '__main__':

    lst = ["Article_Title", "Article_Year", "Article_FirstAuthorSurname", "PaperContact_Surname", "PaperContact_Email",
           "Article_Journal", "Article_DOI", "Data_DOI", "DataProvider_Title", "DataProvider_Surname",
           "DataProvider_FirstName", "DataProvider_MiddleInitials", "DataProvider_Email", "DataProvider_Institute",
           "DataProvider_Department", "Additional_Authors", "Number_of_Studies", "Total_Number_ofSites",
           "Total_Number_ofSpecies", "Entire Community", "Notes", "BibKey", "Data From Paper",
           "Other soil organisms sampled", "file"]
    builder = XBuilder(SyntacticFeatureExtractor())
    X = builder.get_X(lst)

    obj = GDB(params={"distance_threshold" : Distance_threshold }, X=X, words=lst)
    clusters = obj.run()
    print(clusters)
