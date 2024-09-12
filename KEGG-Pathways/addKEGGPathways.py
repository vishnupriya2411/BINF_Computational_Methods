#!/usr/bin/env python 

import argparse
import requests

def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Your script description (often top line of script's DocString; eg. Duplicate word n times)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Create a sequential argument (eg. it has to come in the order defined)
    parser.add_argument('blast_file', # name of the argument, we will later use args.word to get this user input
                        metavar='.txt', # shorthand to represent the input value
                        help='Blast file as an input', # message to the user, it goes into the help menu
                        type=str, # type of input expected, could also be int or float
                        default=None, # default option if no input is given by the user
                        # required=True # whether this input must be given by the user, could also be True
                        )
    # Create a flagged argument (eg. input comes after a short "-i" or long "--input" form flag)
    parser.add_argument("output_filename", # name of the argument, we will later use args.number to get this user input
                        metavar='.txt', # shorthand to represent the input value
                        help='Processed BLAST file, with added details', # message to the user, it goes into the help menu
                        type=str, # type of input expected, could also be int or float
                        default=1, # default option if no input is given by the user
                        # required=False # whether this input must be given by the user, could also be True
                        )

    return(parser.parse_args())

def getUniProtFromBlast(blast_line, threshold):
    """Return UniProt ID from the BLAST line if the evalue is below the threshold.

    Returns False if evalue is above threshold.
    """
    cleaned_line = blast_line.strip()
    blast_fields = cleaned_line.split("\t")
    if float(blast_fields[7]) < float(threshold):
        return(blast_fields[1])
    else:
        return(False)

def getKeggOrthology(kegg_organism_IDs):
    ko_data = list()
    for kegg_organism_ID in kegg_organism_IDs:
        # print("ORGANISM ID", kegg_organism_ID)
        result = requests.get(f'https://rest.kegg.jp/link/ko/{kegg_organism_ID}')
        try:
            for entry in result.iter_lines():
                str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
                fields = str_entry.split("\t")
                ko_data.append(fields[1])
        except IndexError:
            return False
    
    return ko_data

def getKeggPathIDs(kegg_path_IDs):
    keggGenes = []
    for kegg_path_ID in kegg_path_IDs:
        print(kegg_path_ID)
        result = requests.get(f'https://rest.kegg.jp/link/pathway/{kegg_path_ID}')
        print("PATHIDS", kegg_path_ID)
        try:
            for entry in result.iter_lines():
                str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
                fields = str_entry.split("\t")
                print("PATH_OUTPUT", fields)
                keggGenes.append(fields[1])  # second field is the keggGene value
        except IndexError:
            return False
    return(keggGenes)

def getKeggGenes(uniprotID):
    """Return a list of KEGG organism:gene pairs for a provided UniProtID."""
    keggGenes = []
    result = requests.get(f'https://rest.kegg.jp/conv/genes/uniprot:{uniprotID}')
    # print(result.content)
    try:
        for entry in result.iter_lines():
            str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
            fields = str_entry.split("\t")
            keggGenes.append(fields[1])  # second field is the keggGene value
    except IndexError:
        return False
    return(keggGenes)

def loadKeggPathways(): 
    """Return dictionary of key=pathID, value=pathway name from http://rest.kegg.jp/list/pathway/ko 

    Example: keggPathways["path:ko00564"] = "Glycerophospholipid metabolism"
    """
    keggPathways = {}
    result = requests.get('https://rest.kegg.jp/list/pathway/ko')
    for entry in result.iter_lines():
        str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
        # print(str_entry)
        fields = str_entry.split("\t")
        keggPathways[fields[0]] = fields[1]
    return(keggPathways)

def addKEGGPathways(args):
    
    threshold = 1e-50
    
    pathways = loadKeggPathways()
    print("LOADED KEGG PATHWAYS", pathways)

    with open(args.output_filename, "w") as output_file:
        with open(args.blast_file, "r") as blast_file:
            for blast_line in blast_file.readlines():
                uniprotID = getUniProtFromBlast(blast_line, threshold)
                if not isinstance(uniprotID, bool):
                    uniprotID = uniprotID.split(".")[0]
                else:
                    continue
                print(uniprotID)
                if uniprotID != False:
                    keggGenes = getKeggGenes(uniprotID)
                    if keggGenes != False:
                        # print("KEGGGENES", keggGenes)
                        orthology = getKeggOrthology(keggGenes)
                        # print("ORTHOLOGY", orthology)
                        if orthology != False:
                            path_ids = getKeggPathIDs(orthology)
                            print("PATH_IDS", path_ids)
                            if path_ids != False:
                                for path_no, path_id in enumerate(path_ids):
                                    
                                    try:
                                        path_desc = pathways[path_id]
                                    except KeyError:
                                        continue
                                        
                                    else:
                                        print(orthology, path_ids)
                                        new_line = blast_line.strip()+f"\t{orthology[0]}\t{path_desc}\n"
                                        print(new_line)
                                        output_file.write(new_line)
                            else:
                                continue


                    else:
                        continue

                else:
                    continue

                # print(hsa)

    return 0

if __name__ == "__main__":
    args = get_args()

    result = addKEGGPathways(args)
    print(result)
