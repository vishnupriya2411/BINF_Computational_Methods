# Author
- Nuthanapati Vishnu Priya 
# Date created 
- 11/30/2022
# Methods 
## Running BLAST 
### input data
The input data is the data which is being retrieved from module-08 results. It's been retrieved by generating symbolic links to access data from module8. Now the data file is .fasta files. The data files are imported from previous module. 
### BLAST 
- `BLAST` Basic Local Alignment Search Tool performs speed-optimized local alignment searches between a query and a sequence database. These begin with a "word" of size "W" that scores higher than a cutoff "T." The alignment is then extended in every direction, looking for one with a score of "S" or above.`makeblastdb` uses to convert .fasta file into BLAST database and creates `Trinity.fasta`. Trinity.fasta has mRNA sequences, to align it with Swissport which is protein database. `blastx` is used to align input query to the database. 
### Transcoder
- Transcoder assists in the identification of potential coding regions within reconstructed transcripts and recognizes likely coding sequences based on the following criterias: minimum length ORFs, log-likelihood score, PSSM
- TransDecoder to locate potential coding areas in transcript sequences. It locates lengthy open reading frames (ORFs) inside transcripts and rates them based on the sequences they contain.
-finding longest ORFs and then align them with swissport using `blastp` and the alignments are found. 
### HMM scan 
- The development of observable events that depend on internal, indirectly visible causes can be modeled statistically using a hidden Markov model (HMM).
- `hmmscan` is used to search protein sequences against collections of protein profiles because HMMER aims to be significantly more accurate and more able to detect remote homologs, because of the strength of its underlying probability models.
### Protein prediction 
The `TransDecoder.Predict` program predicts the likely coding regions from the ORFs identified by Transdecoder.LongOrfs and included results from homology searches (blast/hmmer results) as ORF retention criterion, and aligned with query sequences which are predicted protien sequences to Swissport. 

# References 
1. Kent, W. J. (2002). BLAT--the BLAST-like alignment tool. Genome Research, 12(4), 656–664. https://doi.org/10.1101/gr.229202
2. Haneef, J. (2014, February 2). Difference between PAM and BLOSUM Matrix. Major Differences. https://www.majordifferences.com/2014/02/difference-between-pam-and-blosum-matrix_1.html)
3. Alweshah, M., Alkhalaileh, S., Albashish, D., Mafarja, M., Bsoul, Q., & Dorgham, O. (2021). A hybrid mine blast algorithm for feature selection problems. Soft Computing (Berlin, Germany), 25(1), 517–534. https://doi.org/10.1007/s00500-020-05164-4


