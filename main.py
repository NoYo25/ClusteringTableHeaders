from config import kg_Schema_embeddings_XML, kg_Schema_ascii_XML
from experiments.exp1 import Experiment1
from experiments.exp3 import Experiment3
from experiments.expGT import ExperimentGroundTruth
from inOut.kgWriter import KGWriter

if __name__ == '__main__':
    lst = ["Article_Title", "Article_Year", "Article_FirstAuthorSurname", "PaperContact_Surname", "PaperContact_Email",
           "Article_Journal", "Article_DOI", "Data_DOI", "DataProvider_Title", "DataProvider_Surname",
           "DataProvider_FirstName", "DataProvider_MiddleInitials", "DataProvider_Email", "DataProvider_Institute",
           "DataProvider_Department", "Additional_Authors", "Number_of_Studies", "Total_Number_ofSites",
           "Total_Number_ofSpecies", "Entire Community", "Notes", "BibKey", "Data From Paper",
           "Other soil organisms sampled", "file"]

    # lst = ["Article_Title", "Article_Year"] #for debugging

    #Ground Truth
    #exp = ExperimentGroundTruth(lst)
    #clusters = exp.run()
    #writer = KGWriter(clusters)
    #writer.writeSchema(kg_Schema_ascii_XML)


    #Experiment 1 ...
    print("Syntatic representation of column headers using ASCII code..."
    exp1 = Experiment1(lst)
    clusters = exp1.run()

    writer = KGWriter(clusters)
    writer.writeSchema(kg_Schema_ascii_XML)

    #Experiment 3 ...
    print("Semantic representation of column headers using word vectors..."
    exp3 = Experiment3(lst)
    clusters = exp3.run()

    writer = KGWriter(clusters)
    writer.writeSchema(kg_Schema_embeddings_XML)
