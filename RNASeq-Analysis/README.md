# Author
Vishnu Priya Nuthanapati

# Date created 
11/14/2022

# Methods 
## Aliging RNASeq reads to reference genome with multiple scripting 
### input data 
The input data for this experiment is a subset of an RNA-Seq experiment of Aiptasia pallida. Here there are four treatment groups with six replicates in total 24 anemones. As there is more data in the raw reads of anemones, before considering the data to RNA alignment QC sequencing is done, where it does quality check and produces relatively small reads with potential length and quality for RNA sequencing. 
### GMAP database
`gmap_build` uses to build an index of the reference genome. The GMAP database has been indexed and improved to enable significantly quicker alignment than would be achievable if the alignment were performed directly against the FASTA file.
### with multiple scripting 
To write sam,bam and bai files at a time for all 24 fastq files we use for loop inside the bash script. Firstly we find the samples by writing a script `findSampleNames.sh` and then list the samples using `listSamples.sh`. 
### Created shell scripts 
- trimAll.sh - trims all the fastq files
- alignAll.sh - aligns the fastq files 
- sortall.sh - sorts all the align reads
- indexAll.sh - indexes the align reads
### Trimming
For quality trimming we use trimmomatic which is java based quality trimmers. The input to the trim function is raw fastq files of Aiptasia pallida.The files are in data/rawreads/. We trim[[1]](http://www.usadellab.org/cms/?page=trimmomatic) the rawread directory which consists of fastq files and direct the trimmed output files to data/trimmed/. We produce log files which are written to results/logs/ directory when `trimAll.sh` is runned. 
### Aligning the reads
We create `alignAll.sh` file for soting the alignments. We use gsnap command. `gsnap` stands for Genomic Short-read Nucleotide Alignment Program. The GSNAP[[2]](https://bioinformaticshome.com/tools/rna-seq/descriptions/GSNAP.html#gsc.tab=0) technique, which is based on the seed-and-extend approach, operates on reads as short as 14 nucleotides and computes SNP-tolerant alignments of diverse combinations of major and minor alleles. Here for aliging it takes the trimmed file paths as input files and gives **.sam** format files as output files. 
### sorting of the alignments 
Created `sortAll.sh` scriptfile to sort the aligned reads.`samtools` a collection of tools is used for manipulating alignment formats. Here for sorting we use `samtools sort`[[3]](https://rnnh.github.io/bioinfo-notebook/docs/samtools.html). The input files are .sam which is taken from /results/sam/ and it provides **.sorted.bam** files as output files. 
### indexing for bam files
Created `indexAll.sh` to index all the sorted bam files. Here we get **.bai** files. .bai files are index files for BAM. Here we use `samsort index`[[3]](https://rnnh.github.io/bioinfo-notebook/docs/samtools.html).You'll need an index file to contain the BAM file offsets of genome positions if you want to seek to a certain genome position from a sorted bam file.

## satch_alignRNAseq.sh
Combined all the multi shell scripts in one batch script and run it with `sbatch` command. **.output** file is produced as output.

# Reference citations 
1. (USADELLAB.org - Trimmomatic: A Flexible Read Trimming Tool for Illumina NGS Data, n.d.). [[1]](http://www.usadellab.org/cms/?page=trimmomatic)
2. (Tammi, n.d.). [[2]](https://bioinformaticshome.com/tools/rna-seq/descriptions/GSNAP.html#gsc.tab=0)
3. (SAMtools, n.d.). [[3]](https://rnnh.github.io/bioinfo-notebook/docs/samtools.html)


