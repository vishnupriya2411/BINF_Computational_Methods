#!/usr/bin/env python

from Bio import SeqIO

# Define input and output file paths
input_file = "APOE_refseq_transcript.fasta"
output_file = "apoe_aa.fasta"

# Open the input and output files
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    # Iterate over each record in the input file
    for record in SeqIO.parse(f_in, "fasta"):
        # Trim the sequence to a multiple of three
        trimmed_seq = record.seq[:len(record.seq) - (len(record.seq) % 3)]

        # Translate the DNA sequence to amino acid sequence
        amino_acid_seq = trimmed_seq.translate()

        # Create a new SeqRecord object with the translated sequence and the original header
        new_record = record
        new_record.seq = amino_acid_seq

        # Write the new record to the output file
        SeqIO.write(new_record, f_out, "fasta")

