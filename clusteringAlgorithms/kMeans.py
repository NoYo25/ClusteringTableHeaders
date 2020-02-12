from XBuilder import XBuilder
from clusteringAlgorithms.clusterAlgorithm import ClusterAlgorithm
from sklearn.cluster import KMeans
import numpy as np

from featuresExtractor.featureExtractor import FeatureExtractor
from featuresExtractor.syntacticFeatureExtractor import SyntacticFeatureExtractor


class MyKMeans(ClusterAlgorithm):
    def __init__(self, params):
        ClusterAlgorithm.__init__(self, params)

        assert "k" in params, "k must be in the params dict!"
        self.k = params["k"]

        assert "featureExtractor" in params, "featureExtractor must be in params"
        self.featureExtractor = params["featureExtractor"]

        assert isinstance(self.featureExtractor, FeatureExtractor)

    def __get_clusters_dict(self, X, estimator):
        labels_unique = np.unique(estimator.labels_)
        n_clusters_ = len(labels_unique)
        # print(n_clusters_)
        dict_1 = {i: X[np.where(estimator.labels_ == i)] for i in range(n_clusters_)}

        clustered_dict = {}

        lst = []
        for key, vals in dict_1.items():
            c_lst = []
            for val in vals:
                # print(val)

                word = self.featureExtractor.get_word_from_features(val)
                # print(word)
                c_lst = c_lst + [word]
            lst.append(c_lst)
            # print("\n")

        for key, vals in dict_1.items():
            clustered_dict[key] = lst[key]
            # print(lst[key])
        return clustered_dict

    def run(self, plot=False):

        X = self.params["X"]
        kmeans_estimator = KMeans(n_clusters=self.k)
        k_clusters = kmeans_estimator.fit_predict(X)
        clusters = self.__get_clusters_dict(X, kmeans_estimator)

        if plot:
            pass
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

    obj = MyKMeans(params={"k" : 6 }, X=X, featureExtractor=SyntacticFeatureExtractor())
    clusters = obj.run()
    print(clusters)