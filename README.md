# Author
- Vishnu Priya Nuthanapati
  
# Multi Alignment Sequencing and Functional Annotation Project
## Overview
This project focuses on the bioinformatics analysis of biological sequences (DNA, RNA, and proteins) to explore evolutionary relationships, identify functional motifs, and annotate protein-coding regions. The pipeline integrates multiple tools and scripting workflows to automate sequence alignment, RNA-Seq data processing, transcriptome assembly, and functional annotation.

## Key Steps

1.  Multiple Sequence Alignment (MSA):

Using Clustal Omega to align APOE orthologs across species, highlighting conserved regions and sequence variations.

2.  RNA-Seq Data Processing:

Quality trimming, alignment, and sorting of Aiptasia pallida RNA-Seq data using tools like Trimmomatic, GSNAP, and Samtools to generate sorted BAM files.

3.  Transcriptome Assembly:

De novo and reference-guided transcriptome assembly using Trinity to reconstruct gene expression from RNA-Seq data and calculate N50 values.

4.  Protein Prediction and Functional Annotation:

Prediction of coding regions with TransDecoder and local alignment with BLAST.
Functional annotation using KEGG API to map predicted proteins to known biological pathways.

## Tools and Scripts:

- Clustal Omega for sequence alignment
- Trimmomatic, GSNAP, and Samtools for RNA-Seq data processing
- Trinity for transcriptome assembly
- BLAST and HMMER for protein prediction
- KEGG API for pathway annotation

This project leverages automated scripting and job scheduling (Slurm) to streamline high-throughput bioinformatics analysis, enabling the exploration of evolutionary insights and functional annotations from large-scale sequence data.






