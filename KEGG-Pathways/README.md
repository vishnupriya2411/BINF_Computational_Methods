# Author 
- Vishnu Priya Nuthanapati

## Date created 
- 07/12/2022

### Aim
- to annotate SWISS port ID hits to a species-independent ortholog ID. We can do this with the KEGG ortholog IDs

### input file
`alignedPredicted.txt`(output of previous module) is used as input file in this module. This .txt file has information of aligned predicted proteins from protein data Swissport. 

### KEGG API
- It provides a programmatic way to access data from a service like KEGG. 
- The below are the scripts used in python script to annotate the input data with KEGG 
- `getOneKegg.sh` - it is used to get the swissport to KEGG conversion for protein 
- `getOneKo.sh` - it is used to get the KEGG orthology for one KEGG protein ID
- `getOnePath.sh` - it is used to get pathways for KEGG orthology 
- `getPathDesc.sh` - it is used to get pathway descriptions for all KOpathways. 
- Thus annotation is done with access the KEGG files with `requests` and using bash scripts in python script by using `subprocess`

# References 
1. KO (KEGG ORTHOLOGY) Database. (n.d.-b). https://www.genome.jp/kegg/ko.html 
2. KEGG PATHWAY Database. (n.d.). https://www.genome.jp/kegg/pathway.html 
3. KEGG: Kyoto Encyclopedia of Genes and Genomes. (n.d.). https://www.genome.jp/kegg/
