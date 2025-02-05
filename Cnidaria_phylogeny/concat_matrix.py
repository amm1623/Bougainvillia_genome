import os
from Bio import SeqIO
from collections import defaultdict

def read_fasta_to_species_dict(fasta_file):
    """Reads a FASTA file and returns a dictionary mapping species names to sequences."""
    species_dict = defaultdict(list)
    for record in SeqIO.parse(fasta_file, 'fasta'):
        species_dict[record.id].append(str(record.seq))  # Append the sequence for this species
    return species_dict

def create_alignment_matrix(output_file, concatenated_files):
    """Creates a matrix of alignment sequences with species names as headers."""
    alignment_dict = defaultdict(list)  # Dictionary for species and their loci

    # Gather all alignment sequences by species
    for fasta_file in concatenated_files:
        species_dict = read_fasta_to_species_dict(fasta_file)
        for species, sequences in species_dict.items():
            alignment_dict[species].extend(sequences)  # Add the sequences for each locus

    # Write the alignment sequences to the output file with species names as headers
    with open(output_file, 'w') as out_file:
        # Write sequences for each species
        for species in sorted(alignment_dict.keys()):
            out_file.write(f'>{species}\n')  # Write the species name as a header
            sequences = alignment_dict[species]
            out_file.write('\t'.join(sequences) + '\n')  # Write the alignment sequences

    print(f'Matrix saved to {output_file}')

# Gather all concatenated files that start with 'concatenated_' and end with '.fa'
concatenated_files = [f for f in os.listdir('.') if f.startswith('concatenated_') and f.endswith('_aligned.fa')]

# Create the output matrix file
output_matrix_file = 'alignment_matrix_all.txt'
create_alignment_matrix(output_matrix_file, concatenated_files)
