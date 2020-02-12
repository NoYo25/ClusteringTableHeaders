from clusteringAlgorithms.GDB import GDB
from clustersBuilder import ClustersBuilder
from config import syntatic_distance_threshold
from featuresExtractor.syntacticFeatureExtractor import SyntacticFeatureExtractor



class Experiment1(object):
    def __init__(self, headers_lst):
        self.lst = headers_lst

    def run(self):
        print("Experiment 1 - Syntatic Representation: ")
        clustering_algo1 = GDB(params={"distance_threshold": syntatic_distance_threshold, "words": self.lst, "distance_file_path": "syntatic_distances.png"})
        builder = ClustersBuilder(featureExtractor=SyntacticFeatureExtractor(), clusterAlgorithm=clustering_algo1
                                  , words=self.lst, plot=True)
        clusters = builder.build_clusters()
        print("Initial clusters using syntatic ASCII representation")
        print(clusters)

        clusters = builder.suggest_clusters_names(clusters)
        print(clusters)

        clusters = builder.shorten_cluster_items(clusters)
        print(clusters)
        return clusters
