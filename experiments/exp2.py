from clusteringAlgorithms.kMeans import MyKMeans
from clustersBuilder import ClustersBuilder
from featuresExtractor.syntacticFeatureExtractor import SyntacticFeatureExtractor


class Experiment2(object):
    def __init__(self, headers_lst):
        self.lst = headers_lst

    def run(self):
        print("Experiment 2: ")
        clustering_algo2 = MyKMeans(params={"k": 6, "featureExtractor": SyntacticFeatureExtractor()})
        builder = ClustersBuilder(featureExtractor=SyntacticFeatureExtractor(), clusterAlgorithm=clustering_algo2
                                  , words=self.lst, plot=True)
        clusters = builder.build_clusters()
        print(clusters)
        return clusters
