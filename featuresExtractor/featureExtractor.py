import abc


class FeatureExtractor(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_features_from_word(self, input_str):
        raise NotImplementedError('get_features_from_word must be implemented!')

    @abc.abstractmethod
    def get_word_from_features(self, features):
        raise NotImplementedError('get_word_from_features must be implemented!')
