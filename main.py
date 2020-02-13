from config import kg_Schema_embeddings_XML, kg_Schema_ascii_XML
from experiments.exp1 import Experiment1
from experiments.exp3 import Experiment3
from experiments.expGT import ExperimentGroundTruth
from inOut.kgWriter import KGWriter

if __name__ == '__main__':
        #lst = ["Article_Title", "Article_Year", "Article_FirstAuthorSurname", "PaperContact_Surname", "PaperContact_Email",
        #   "Article_Journal", "Article_DOI", "Data_DOI", "DataProvider_Title", "DataProvider_Surname",
        #   "DataProvider_FirstName", "DataProvider_MiddleInitials", "DataProvider_Email", "DataProvider_Institute",
        #   "DataProvider_Department", "Additional_Authors", "Number_of_Studies", "Total_Number_ofSites",
        #   "Total_Number_ofSpecies", "Entire Community", "Notes", "BibKey", "Data From Paper",
        #   "Other soil organisms sampled", "file"]
        
    lst = ["file",
"Study_Name",
"Site_Name",
"PH_value",
"PH_Collection_Method",
"PH_mean",
"Organic_Carbon__percent",
"OC_mean",
"Soil_Organic_Matter__percent",
"C.N_ratio",
"CN_mean",
"Sand__percent",
"Silt__percent",
"Clay__percent",
"sand_silt_clay_mean",
"ph_new",
"phFinal",
"ClayFinal",
"SandFinal",
"SiltFinal",
"OCFinal",
"ESA",
"elevation",
"SnowMonths_value",
"SnowMonths_cat",
"Aridity",
"PETyr",
"PET_SD",
"SpeciesRichness_value",
"SpeciesRichnessUnit",
"Site_WetBiomass",
"Site_WetBiomassUnits",
"Site_BiomassM2",
"logBiomass",
"Site_Abundance",
"Site_AbundanceUnits",
"Sites_AbundanceM2",
"logAbundance"
]

    # lst = ["Article_Title", "Article_Year"] #for debugging

    #Ground Truth
    #exp = ExperimentGroundTruth(lst)
    #clusters = exp.run()
    #writer = KGWriter()
    #writer.writeGroundTruthSchema()


    #Experiment 1 ...
    exp1 = Experiment1(lst)
    clusters = exp1.run()

    writer = KGWriter()
    writer.writeSchema(clusters, kg_Schema_ascii_XML)

    #Experiment 3 ...
    exp3 = Experiment3(lst)
    clusters = exp3.run()

    writer = KGWriter()
    writer.writeSchema(clusters, kg_Schema_embeddings_XML)
