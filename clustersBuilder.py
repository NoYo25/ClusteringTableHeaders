# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:06:39 2019

@author: Nora
"""
from XBuilder import XBuilder
from clusteringAlgorithms.GDB import GDB
from clusteringAlgorithms.clusterAlgorithm import ClusterAlgorithm
from clusteringAlgorithms.kMeans import MyKMeans
from featuresExtractor.featureExtractor import FeatureExtractor
from featuresExtractor.semanticFeatureExtractor import SemanticFeatureExtractor
from featuresExtractor.syntacticFeatureExtractor import SyntacticFeatureExtractor
from inOut.kgWriter import KGWriter
from stringUtil import *



from config import min_cluster_name_len, Unknown_cluster_name


class ClustersBuilder:
    def __init__(self, featureExtractor, clusterAlgorithm, words, plot=False):

        self.plot = plot

        assert isinstance(featureExtractor, FeatureExtractor)
        self.featureExtractor = featureExtractor

        assert isinstance(clusterAlgorithm, ClusterAlgorithm)
        self.clusterAlgorithm = clusterAlgorithm

        self.words = words
        self.clusters = None

    def __suggest_cluster_name(self, cluster_word_lst):
        length = len(cluster_word_lst)

        lcs_dict = {}
        for i in range(length):
            for j in range(length):
                if i != j:
                    lcs = find_longest_substring(cluster_word_lst[i], cluster_word_lst[j])
                    if len(lcs) < min_cluster_name_len:
                        continue

                    if lcs in lcs_dict:
                        lcs_dict[lcs] = lcs_dict[lcs] + 1
                    else:
                        lcs_dict[lcs] = 1

        if bool(lcs_dict):
            # print(lcs_dict)
            key = max(lcs_dict, key=lcs_dict.get)
        else:
            key = Unknown_cluster_name
        return key

    def suggest_clusters_names(self, clusters):
        clusters_n = len(clusters)
        named_clusters = {}
        for i in range(clusters_n):
            name = self.__suggest_cluster_name(clusters[i])
            named_clusters.update({name: clusters[i]})

        self.clusters = named_clusters
        return named_clusters


    def display_clusters(self, clusters):
        for key in clusters.keys():
            print("{0}:".format(key))
            for word in clusters[key]:
                print("\t" + word)
            print("\n")

    def move_item(self, clusters, word, to_cluster):
        new_dict = {c: [x for x in vals if x != word] for c, vals in clusters.items()}
        if to_cluster in clusters:
            new_dict.update({to_cluster: new_dict[to_cluster] + [word]})
        else:
            new_dict.update({to_cluster: [word]})
        return new_dict

    def move_items(self, clusters, word_lst, to_cluster_lst):
        assert len(word_lst) == len(to_cluster_lst)

        new_dict = clusters
        for word, to_cluster in zip(word_lst, to_cluster_lst):
            new_dict = self.move_item(new_dict, word, to_cluster)

        self.clusters = new_dict
        return new_dict

    def rename_cluster(self, clusters, old_name, new_name):
        if old_name in clusters:
            # clusters.update({new_name, clusters.pop(old_name)})
            clusters[new_name] = clusters.pop(old_name)
        else:
            print("The name doesn't exists.")
        return clusters

    def rename_clusters(self, clusters, old_names, new_names):
        assert len(old_names) == len(new_names)
        for old, new in zip(old_names, new_names):
            clusters = self.rename_cluster(clusters, old, new)
        return clusters

    def merge_clusters(self, clusters_key_lst):
        #it would merge it automatically to the first cluster key mentioned in the list:
        dest_cluster = clusters_key_lst[0]
        for key in clusters_key_lst[1:]:
            self.clusters.update({dest_cluster: self.clusters[dest_cluster] + self.clusters[key]})
            del self.clusters[key]
        return self.clusters


    def shorten_cluster_items(self, clusters):
        new_dict = {c: [x.replace(c, '').replace('_', ' ') for x in vals] for c, vals in clusters.items()}
        return new_dict

    def build_clusters(self):
        feature_builder = XBuilder(self.featureExtractor)
        X = feature_builder.get_X(self.words)

        self.clusterAlgorithm.add_to_params("X", X)
        clusters = self.clusterAlgorithm.run(plot=self.plot)
        self.clusters = clusters
        return clusters

