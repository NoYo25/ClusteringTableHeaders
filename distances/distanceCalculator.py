import abc
import os

import seaborn as sns
import matplotlib.pyplot as plt

from config import results_dir





class DistanceCalculator(object):

    @abc.abstractmethod
    def calculate_distances(self, X):
        raise NotImplementedError('calculate_distances must be implemented!')

    @abc.abstractmethod
    def calculate_distances_full_view(self, X,  index, columns, distance_file_path, plot=True):
        raise NotImplementedError('calculate_distances must be implemented!')

    def plot_distances_heatmap(self, df, distance_file_path):
        # plt.rcParams['figure.figsize'] = (20.0, 15.0)
        plt.rcParams['figure.figsize'] = (15.0, 10.0)
        # sns.heatmap(df, cmap='coolwarm', vmin=0, vmax=1)
        svm = sns.heatmap(df, cmap='coolwarm', vmin=0, vmax=1)
        plt.show()

        figure = svm.get_figure()
        print(os.path.join(os.path.realpath('.'), results_dir, distance_file_path))
        figure.savefig(os.path.join(os.path.realpath('.'), results_dir, distance_file_path), bbox_inches='tight', dpi=400)

