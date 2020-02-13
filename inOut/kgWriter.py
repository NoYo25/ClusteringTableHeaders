# http://jmvidal.cse.sc.edu/talks/xmlrdfdaml/rdfschemaex.html
# rdflib documentation: https://rdflib.readthedocs.io/en/stable/
# Validator: https://www.w3.org/RDF/Validator/
import os
import uuid

from config import kg_schema_xml_template, GT_KG_Schema_XML, results_dir, GT_KG_Full_XML
from rdflib import URIRef, BNode, Literal, Namespace, Graph, plugin
from rdflib.namespace import DC, FOAF, RDFS
from rdflib.serializer import Serializer
import rdflib
from rdflib.namespace import RDF, XSD
from parser import *


class KGWriter(object):
    def __init__(self):
        # Manually created clusters ...
        self.GT_named_clusters = {
            'SoilProperties': ['PET SD', 'Aridity', 'elevation', 'ESA', 'PETyr', 'sand silt clay mean', 'C.N ratio', 'Soil Organic Matter  percent', 'Organic Carbon  percent'],
            'Study': [' Name', 'file'],
            'PH': [' value', ' Collection Method', ' mean', 'ph new'],
            'mean': ['OC ', 'CN ', 'OCFinal'],
            'percent': ['Sand  ', 'Silt  ', 'Clay  ', 'SandFinal'],
            'Final': ['Clay', 'Silt', 'ph', 'Sand'],
            'SnowMonths': [' value', ' cat'],
            'SpeciesRichness': ['value', 'Unit'],
            'SiteWetBiomass': ['Site WetBiomass', 'Site WetBiomassUnits'],
            'Site': [' BiomassM2', 'logBiomass', ' AbundanceUnits', 's AbundanceM2', ' Name'],
            'Abundance': ['Site ', 'log']}


        # Manually create original clusters, it must map the columns in the CSV file
        self.GT_original_clusters = {
            'SoilProperties': ['PET_SD', 'Aridity', 'elevation', 'ESA', 'PETyr', 'sand_silt_clay_mean', 'C.N_ratio', 'Soil_Organic_Matter__percent', 'Organic_Carbon__percent'],
            'Study': ['Study_Name', 'file'],
            'PH': ['PH_value', 'PH_Collection_Method', 'PH_mean', 'ph_new'],
            'mean': ['OC_mean', 'CN_mean', 'OCFinal'],
            'percent': ['Sand__percent', 'Silt__percent', 'Clay__percent', 'SandFinal'],
            'Final': ['ClayFinal', 'SiltFinal', 'phFinal', 'SandFinal'],
            'SnowMonths': ['SnowMonths_value', 'SnowMonths_cat'],
            'SpeciesRichness': ['SpeciesRichness_value', 'SpeciesRichnessUnit'],
            'SiteWetBiomass': ['Site_WetBiomass', 'Site_WetBiomassUnits'],
            'Site': ['Site_BiomassM2', 'logBiomass', 'Site_AbundanceUnits', 'Sites_AbundanceM2' , 'Site_Name'],
            'Abundance': ['Site_Abundance', 'logAbundance']}



        self.ex_uri = Namespace('http://www.loda.example#')


        self.g = Graph()

    #TODO: Create GroundTruth by hand and make the use of exiting vocabularies in schema.org and others to map it to real properties
    def writeGroundTruthSchema(self):
        self.writeSchema(self.GT_named_clusters, to_file_path=GT_KG_Schema_XML)

    def writeGroundTruthFullGraph(self):
        self.writeFullGraph(self.GT_named_clusters, self.GT_original_clusters, to_file_path=GT_KG_Full_XML)

    def __getID(self, name):
        return unifyWord(name.strip()) + str(uuid.uuid1())

    def __getLabel(self, name):
        return getWords(name.strip())

    def __getValue(self, name):
        return unifyWord(name.strip())

    def writeSchema(self, named_clusters,  to_file_path):

        for c, members in named_clusters.items():

            classNode = URIRef(self.__getID(c))
            self.g.add((classNode, RDF.type, RDFS.Class))
            self.g.add((classNode, RDFS.label, Literal(self.__getLabel(c))))

            # Properties follow the class node
            for property_member in members:
                predicate = URIRef(self.ex_uri[self.__getValue(property_member)])
                propertyNode = URIRef(self.__getID(property_member))
                self.g.add((propertyNode, RDF.type, predicate))
                self.g.add((propertyNode, RDFS.domain, classNode))
                self.g.add((propertyNode, RDFS.range, Literal(self.__getValue(property_member))))
                self.g.add((propertyNode, RDFS.label, Literal(self.__getLabel(c))))

        self.g.serialize(os.path.join(os.path.realpath('.'), to_file_path), format='xml')

    def writeFullGraph(self, named_clusters, original_clusters, to_file_path):
        for c, members in named_clusters.items():

            classNode = URIRef(self.__getID(c))
            self.g.add((classNode, RDF.type, RDFS.Class))
            self.g.add((classNode, RDFS.label, Literal(self.__getLabel(c))))

            # Properties follow the class node
            for property_member in zip(members):
                predicate = URIRef(self.ex_uri[self.__getValue(property_member)])
                propertyNode = URIRef(self.__getID(property_member))
                self.g.add((propertyNode, RDF.type, predicate))
                self.g.add((propertyNode, RDFS.domain, classNode))
                self.g.add((propertyNode, RDFS.range, Literal(self.__getValue(property_member))))
                self.g.add((propertyNode, RDFS.label, Literal(self.__getLabel(c))))

                # add dummy article
                value = "Learning of Data Annotations"
                instanceNode = URIRef(self.__getID(value))
                self.g.add((instanceNode, RDF.type, classNode))
                self.g.add((instanceNode, predicate, Literal(self.__getLabel(value))))


                break

            break

        self.g.serialize(os.path.join(os.path.realpath('..'), to_file_path), format='xml')

    def readGraph(self):
        g = rdflib.Graph()
        g.load(os.path.join(os.path.realpath('..'), GT_KG_Schema_XML))
        for s, p, o in g:
            print (s, p, o)
        print(len(g))

    def visualizeGraph(self):
        pass
        # Online Service: http://www.ldf.fi/service/rdf-grapher
        # Software Package: https://www.w3.org/2018/09/rdf-data-viz/

if __name__ == '__main__':
    w = KGWriter()
    w.writeGroundTruthSchema()
    #w.writeGroundTruthFullGraph()
    #w.readGraph()
