module load anaconda3/2021.11
source activate BINF-12-2021

input_file="apoe_aa.fasta"
output_file="apoe_alignment.fasta"

clustalo -i $input_file -o $output_file

echo "Alignment complete."

