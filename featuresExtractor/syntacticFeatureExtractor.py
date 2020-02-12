from featuresExtractor.featureExtractor import FeatureExtractor
from parser import *

class SyntacticFeatureExtractor(FeatureExtractor):
    def __init__(self):
        self.parser = Parser()

    def __get_ASCII_From_Chars(self, input_str):
        return [ord(c) for c in input_str]

    def __get_Chars_From_ASCII(self, input_ascii):
        return ''.join([chr(int(c)) for c in input_ascii])

    def get_features_from_word(self, input_str):
        input_segments = self.parser.parse(input_str)
        features = [input_segments[0]]
        for segment in input_segments[1:]:
            features = features + self.__get_ASCII_From_Chars(segment)
        return features

    def get_word_from_features(self, features):
        length = int(features[0])
        ascii_arr = features[1:length + 1]
        return self.__get_Chars_From_ASCII(ascii_arr)


if __name__ == '__main__':
    obj = SyntacticFeatureExtractor()
    word = "Article_Title"
    features = obj.get_features_from_word(word)
    print(features)
