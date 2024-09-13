# Author
- Vishnu Priya Nuthanapati

# Date created 
- 11/21/2022

# Methods 
## Running transcriptome assembly for mutliple fastq files 
### input data 
- The input data is the data which is being retrieved from RNASeq Module. It's been retrieved by generating `symbolic links` to access data from module7. Now the input data is trimmed fastq files, sam and bam files. The data files are imported from previous module.
- Using BAM files to assemble a reference-guided transcriptome. 
- Using quality-trimmed reads to assemble a de-novo transcriptome. 
### Created shell scripts
- mergeAll.sh
- runTrinity.sh
- analyzeTrinity.sh
- trinityDeNovo.sh
- analyzeTrinityDeNovo.sh
- sbatch_trinity.sh
### Denovo transcriptome assembly
- De novo transcriptome assembly is frequently used to investigate non-model organisms since it is less expensive and easier than creating a genome, and reference-based approaches cannot be used without an existing genome.
### Samtools
- Samtools sort and align: Assemblers require SAM files to be sorted and in BAM format - the binary version of SAM. We utilize samtools to convert a SAM file into a sorted BAM file. Samtools may be used to do a variety of tasks on sam files, such as viewing, sorting, indexing, and so on. The shell script will convert Aip02.sam to a sorted BAM version here.
### Samtools index
- Samtools index:
Here is the samtools index command. Write this as a shell script named indexSam.sh and run it. Monitor with top. Here we Notice that the Capture STDOUT (1>) as Aip02.index.log and and STDERR (2>) as Aip02.index.err.
### Trinity
- Trinity is a tool that comprises of three modules for de novo transcriptome assembly using RNA-seq data: Inchworm, Chrysalis, and Butterfly. The technique employs de Bruijn graphs and the dynamic programming approach, and it is capable of detecting isoforms, handling paired-end reads, different insert sizes, and strandedness. The time it takes to execute is proportional to the number of graph branches.
- We utilize this assembly to determine the N50 value and so continue our sequencing analysis. After sorting the contigs in descending order of length, N50 is the minimum length of contigs for 50% of the assembly. The N50 value for all contigs in genome guided assembly is 570, but the equivalent parameter for de novo assembly is 605. The N50 for the longest genome-guided isoform contig is 514, whereas the same metric for de novo is 512.

# Citations 
1. Jain, P., Krishnan, N. M., & Panda, B. (2013). Augmenting transcriptome assembly by combining de novo and genome-guided tools. PeerJ (San Francisco, CA), 1, e133–e133. https://doi.org/10.7717/peerj.133 Wu, T. D., Reeder, J., Lawrence, M., Becker, G., & Brauer, M. J. (2016)
2. GMAP and GSNAP for Genomic Sequence Alignment: Enhancements to Speed, Accuracy, and Functionality. Statistical Genomics, 283–334. https://doi.org/10. 1007/978-1-4939-3578-9_15 Bolger, A. M., Lohse, M., & Usadel, B. (2014).
3. Trimmomatic: a flexible trimmer for Illumina sequence data. Bioinformatics, 30(15), 2114–2120. https://doi.org/10.1093/bioinformatics/btu170 Wu, T. D., & Watanabe, C. K. (2005). 
4. GMAP: a genomic mapping and alignment program for mRNA and EST sequences. Bioinformatics, 21(9), 1859–1875. https://doi.org/10.1093/bioinformatics/bti310 
5. Li, H., Handsaker, B., Wysoker, A., Fennell, T., Ruan, J., Homer, N., Marth, G., Abecasis, G., & Durbin, R. (2009). The Sequence Alignment/Map format and SAMtools. Bioinformatics, 25(16), 2078–2079. https://doi.org/10.1093/bioinformatics/btp352 


