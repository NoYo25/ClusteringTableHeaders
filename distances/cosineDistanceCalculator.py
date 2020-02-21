import abc

import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine
from distances.distanceCalculator import DistanceCalculator


class CosineDistanceCalculator(DistanceCalculator, metaclass=abc.ABCMeta):

    def calculate_distances(self, X):
        dist_Mat = np.zeros(shape=(X.shape[0], X.shape[0]))
        for i in range(X.shape[0]):
            for j in range(X.shape[0]):
                dist = cosine(X[i], X[j])
                dist_Mat[i][j] = dist
        return dist_Mat

    def calculate_distances_full_view(self, X,  index, columns, distance_file_path, plot=True):
        dist_matrix = self.calculate_distances(X)
        df = pd.DataFrame(dist_matrix, index=self.words, columns=self.words)
        if plot:
            self.plot_distances_heatmap(df, distance_file_path)
        return df




