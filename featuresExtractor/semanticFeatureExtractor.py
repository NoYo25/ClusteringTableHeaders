from featuresExtractor.featureExtractor import FeatureExtractor
from parser import *
from gensim.models import KeyedVectors
from config import pretrained_word2vec_path
from stringUtil import *
import os

class SemanticFeatureExtractor(FeatureExtractor):
    def __init__(self):
        self.parser = Parser()
        self.model = self.__load_model()

    def get_features_from_word(self, input_str):
        compound_word = to_snake_case(input_str)
        return self.__get_word_vec(self.model, compound_word)

    def get_word_from_features(self, features):
        raise NotImplementedError("This method is not implemented")

    def __load_model(self):
        print("Loading model...")
        model = KeyedVectors.load_word2vec_format(os.path.join(os.path.realpath('.'), pretrained_word2vec_path), binary=True)
        return model

    def __preprocess_words(self, lst):
        print("Preprocess words in lst")
        new_lst = []
        for word in lst:
            new_lst = new_lst + [to_snake_case(word)]
        return new_lst

    def __get_word_vecs(self, model, compound_words):
        print("Getting vectors...")
        vecs = []
        for compound_word in compound_words:
            vec = self.__get_word_vec(model, compound_word)
            vecs = vecs + [vec]
        return vecs

    def __get_word_vec(self, model, compound_word):
        compound_vec = []

        words = compound_word.split("_")
        for word in words:
            try:
                vec = list(model.wv[word])
                compound_vec = compound_vec + [vec]
            except:
                print(word + " doesn't exist in Vocab!")

        faltted_vec = [val for sublist in compound_vec for val in sublist]

        return faltted_vec

    def run(self, lst):
        new_lst = self.__preprocess_words(lst)
        print(new_lst)
        model = self.__load_model()
        vecs = self.__get_word_vecs(model, new_lst)
        return vecs


if __name__ == '__main__':
    #obj = SemanticFeatureExtractor()
    #word = "Article_Title"
    #print(obj.get_features_from_word(word))

    lst = ["Study_site","file.x","Study_ID","Site_Name.x","SpeciesBinomial","MorphospeciesID","Genus","Family","LifeStage","Native.Nonnative","Functional_Type","Abundance","Abundance_Unit","WetBiomass","WetBiomassUnits","file.y","Study_Name","Site_Name.y","Observational","Latitude__decimal_degrees","Longitude__Decimal_Degrees","Altitude__m","Country","Sample_StartDate_Month","Sample_StartDate_Year","Sample_EndDate_Month","Sample_EndDate_Year","ExtractionMethod","Sampled_Area","Sampled_Area_Unit","Sample_Effort","PH","PH_Collection_Method","PH_mean","CEC","CEC_unit","CEC_mean","Base_Saturation_percent","BaseSaturation_mean","Organic_Carbon__percent","OC_mean","Soil_Organic_Matter__percent","SOM_mean","C.N_ratio","CN_mean","Sand__percent","Silt__percent","Clay__percent","sand_silt_clay_mean","USDA_SoilTexture","Soil_Moisture_percent","WRB_FAO_SoilType","LandUse","HabitatCover","IPBES_Habitat_Units","Management_System","Tillage","Pesticide","Fertilizer","Selectively_harvested","Clear_cut","Fire","Stocking_rate","Grazing_all_year","Rotation","Monoculture","Planted","Habitat_as_described","SpeciesRichness","SpeciesRichnessUnit","Site_WetBiomass","Site_WetBiomassUnits","Site_Abundance","Site_AbundanceUnits","NumberofSpecies","Individuals_fromspecies","Individuals_fromspeciesUnits","Biomass_fromspecies","Biomass_fromspeciesUnits"]

    obj = SemanticFeatureExtractor()
    vectors = obj.run(lst)
    print(type(vectors))
