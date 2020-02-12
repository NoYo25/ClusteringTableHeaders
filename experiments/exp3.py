from clusteringAlgorithms.GDB import GDB
from clustersBuilder import ClustersBuilder
from config import semantic_distance_threshold
from featuresExtractor.semanticFeatureExtractor import SemanticFeatureExtractor


class Experiment3(object):
    def __init__(self, headers_lst):
        self.lst = headers_lst

    def run(self):
        print("Experiment 3 - Semantic Representation: ")
        # Here we can say that the semantic embbedings gives an intiution that, it won't relate a couple of words except they are
        # tightly coupled, the threshold needs to be adjusted to capture more words into one cluster
        clustering_algo1 = GDB(params={"distance_threshold": semantic_distance_threshold, "words": self.lst, "distance_file_path": "semantic_distances.png"})

        builder = ClustersBuilder(featureExtractor=SemanticFeatureExtractor(), clusterAlgorithm=clustering_algo1
                                  , words=self.lst, plot=True)
        clusters = builder.build_clusters()
        print(clusters)

        clusters = builder.suggest_clusters_names(clusters)
        print(clusters)

        clusters = builder.shorten_cluster_items(clusters)
        print(clusters)

        return clusters

if __name__ == '__main__':
    lst = ["Article_Title", "Article_Year", "Article_FirstAuthorSurname", "PaperContact_Surname", "PaperContact_Email",
           "Article_Journal", "Article_DOI", "Data_DOI", "DataProvider_Title", "DataProvider_Surname",
           "DataProvider_FirstName", "DataProvider_MiddleInitials", "DataProvider_Email", "DataProvider_Institute",
           "DataProvider_Department", "Additional_Authors", "Number_of_Studies", "Total_Number_ofSites",
           "Total_Number_ofSpecies", "Entire Community", "Notes", "BibKey", "Data From Paper",
           "Other soil organisms sampled", "file"]
    exp = Experiment3(lst)
    exp.run()