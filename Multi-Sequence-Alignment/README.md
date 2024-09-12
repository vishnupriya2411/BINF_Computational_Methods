# Author
- Vishnu Priya Nuthanapati

# Date created 
- 03/03/2023

# Multi Alignment Sequencing(MSA)
Multiple sequence alignment (MSA) is a process of aligning three or more biological sequences (DNA, RNA or protein) to identify similarities and differences among them. It is a widely used technique in bioinformatics and computational biology, and plays an important role in understanding the evolutionary relationships among different organisms and the functional implications of sequence variations.

The goal of multiple sequence alignment is to identify the conserved regions (sequence motifs) and variable regions (insertions, deletions and substitutions) among the sequences being aligned. MSA can reveal patterns of conservation, such as highly conserved amino acids in protein sequences, which can help identify functional domains and motifs. MSAs can also be used to infer phylogenetic relationships among different species or to identify structural features in RNA sequences.

There are several algorithms and software tools available for performing multiple sequence alignment, such as ClustalW, MUSCLE, T-Coffee, and MAFFT. These methods use various algorithms to calculate the optimal alignment of the sequences and produce a score that reflects the degree of similarity among the sequences being aligned.

Overall, multiple sequence alignment is an important tool for understanding the evolutionary relationships among different organisms and for identifying conserved and variable regions in biological sequences that may have functional or structural significance.

## APOE orthologs 

APOE (Apolipoprotein E) orthologs are genes found in different species that are homologous to the human APOE gene. APOE is a protein that plays an important role in lipid metabolism and transport in humans, and is associated with several diseases, including Alzheimer's disease and cardiovascular disease.

APOE orthologs are found in a wide range of organisms, from mammals to fish and insects, and share a high degree of sequence similarity with the human APOE gene.

# pipeline 
## translate_APOE.py 
The task requires the creation of a Python3 program named translate_APOE.py that converts APOE orthologs obtained from the NCBI protein search into amino acid sequences and saves them into a new fasta file named apoe_aa.fasta. The header line of each sequence in the new fasta file should be similar to the original fasta file, i.e., APOE_refseq_transcript.fasta. 

## Clustal Omega
`Clustal Omega` is a widely used multiple sequence alignment software that aligns three or more biological sequences to identify conserved regions and to infer evolutionary relationships between them. It uses a progressive alignment approach, which first generates pairwise alignments of sequences and then builds a guide tree to align them iteratively. Clustal Omega can align DNA and protein sequences, and it is particularly useful for analyzing large datasets, as it can handle hundreds of thousands of sequences in a single alignment. It is available as a web server and as a standalone command-line in discovery as `clustalo`

## clustalAlign.sh
This Bash script loads the Anaconda 3 package manager module, activates a virtual environment called "BINF-12-2021", and performs a sequence alignment using the `clustalo` program with an input file named "apoe_aa.fasta" and an output file named "apoe_alignment.fasta". After the alignment is complete, the script prints the message "Alignment complete." to the console.

## sbatch_clustalAlign.sh
This is a Bash script that runs a sequence alignment using the clustalo program. The script is designed to be submitted as a job to a Slurm job scheduler. The script requests resources from the scheduler, including the partition to run the job in, the maximum time to run, the number of nodes and tasks, and where to direct standard output.

After the resource requests, the script provides usage instructions and copies an input file named "apoe_aa.fasta" to the current directory. Then, the script loads required modules, including Anaconda3 and the BINF6309 Environment, which includes clustalo. The script then runs clustalo with the clustalAlign.sh script and copies the output file to the specified output directory. Finally, the script cleans up input and output files, and copies the log files to the output directory.

# reference 
1. Dineen, D. (n.d.). Clustal Omega, ClustalW and ClustalX Multiple Sequence Alignment. http://www.clustal.org/
2. APOE - Protein - NCBI. (n.d.). https://www.ncbi.nlm.nih.gov/protein/?term=APOE
3. L. (2022, December 24). 7.13C: Homologs, Orthologs, and Paralogs. Biology LibreTexts. https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_(Boundless)/07%3A_Microbial_Genetics/7.13%3A_Bioinformatics/7.13C%3A_Homologs_Orthologs_and_Paralogs

