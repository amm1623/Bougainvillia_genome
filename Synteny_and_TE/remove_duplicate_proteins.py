from Bio import SeqIO

input_file = "Bougainvillia_aa.pep"  # Replace with your input FASTA file
output_file = "Bougainvillia_aa_u.pep"  # Replace with your desired output file

# Create a dictionary to store unique sequences
unique_sequences = {}

# Read the FASTA file
for record in SeqIO.parse(input_file, "fasta"):
    sequence = str(record.seq)
    if sequence not in unique_sequences:
        unique_sequences[sequence] = record

# Write the unique sequences to the output file
with open(output_file, "w") as output_handle:
    SeqIO.write(unique_sequences.values(), output_handle, "fasta")

print(f"Unique sequences have been written to {output_file}")
