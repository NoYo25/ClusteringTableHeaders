# Clustering Table Headers

## Project Description 
This project aims at creating an RDF schema given a list of column headers of a tabular dataset. 
It first transforms the given header list into meaningful vectors, then it applies a distance-based Clustering algorithm such that it maximizes the similarity among headers inside one cluster. The user has the facility to move items from one cluster to another and merge among some clusters.
The system can suggest cluster names based on the commonality among its members. If no common word found, it will produce Unknown.
Afterwards, the user can rename the automatically generated names. Finally, it can expose the resultant clusters in an RDF format.   

## Project Features
- Parse manmade column header (e.g., "articleFirst_AuthorSurname" -> "article", "first", "author", "surname").
- Get header vector representation, converts from string column names into a vector space model.
- Distance-based clustering will be applied to the obtained vectors.
- Users can move members from one to another, merge among clusters and rename clusters.
- Cluster names suggestion, the system can do that by finding the commonality string among cluster members
- Export to RDF/XML schema, each cluster name contributes schema node and cluster members contribute relations/predicates.


## Results 
* All are available under [/results](results) local folder.
* Manually created graph is available under [/assets](assets) folder in RDF/XML format.

## Reproducibility of Results 

* Please keep these values in the config.py
    - min_cluster_name_len = 3
    - Unknown_cluster_name = "Unknown"
    - syntatic_distance_threshold = 0.15
    - semantic_distance_threshold = 0.6
    - pretrained_word2vec_path = 'assets/GoogleNews-vectors-negative300.bin'

* Entry point: main.py initially is configured with two experiments 
    - Syntactic representation of the column headers using ASCII code 
    - Semantic representation of the headers using word embeddings 


## System Requirements & Dependencies 

- python 
- tensorflow
- keras
- pandas
- seaborn
- sklearn
- [RDFLib](https://github.com/RDFLib/rdflib)

## Citation


## Credits 
    * Pre-trained word embeddings, [GoogleNews-vectors-negative300.bin](https://code.google.com/archive/p/word2vec/). 
        -  Mikolov, T., Chen, K., Corrado, G., Dean, J.: Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781 (2013)
    * Columns headers in the main.py are from sWorm dataset 
        - Phillips, H.R., Guerra, C.A., Bartz, M.L., Briones, M.J., Brown, G., Crowther, T.W., Ferlian, O., Gongalsky, K.B., Van Den Hoogen, J., Krebs, J., et al.: Global distribution of earthworm diversity. Science 366(6464), 480–485 (2019)
    * The manually created schema and resultant schemas from experiments are validated by the online [RDF Validator](https://www.w3.org/RDF/Validator/)
    
## License
All source code files are distributed under the terms of the GNU LESSER GENERAL PUBLIC LICENSE.
