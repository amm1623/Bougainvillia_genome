import os
from Bio import SeqIO

def concatenate_fasta_files(alignment_file, new_sequence_file, output_file):
    # Read sequences from both files
    alignment_seqs = list(SeqIO.parse(alignment_file, 'fasta'))
    new_seqs = list(SeqIO.parse(new_sequence_file, 'fasta'))

    # Append new sequences to the existing alignment
    with open(output_file, 'w') as out_file:
        # Write original alignment sequences
        SeqIO.write(alignment_seqs, out_file, 'fasta')
        # Write new sequences
        SeqIO.write(new_seqs, out_file, 'fasta')
    
    print(f'Concatenated {new_sequence_file} into {alignment_file}, saved to {output_file}')

# Process matching file pairs in the directory
for filename in os.listdir('.'):
    if filename.startswith('renamed_filtered_') and filename.endswith('.h2a.fa'):
        # Get the base part of the renamed file
        base_filename = filename[len('renamed_filtered_'):-len('.h2a.fa')]

        # Search for the corresponding untrimmed file that matches the base
        for untrimmed_file in os.listdir('.'):
            if untrimmed_file.startswith('OG') and untrimmed_file.endswith('.untrimmed.fa.mafft'):
                if base_filename in untrimmed_file:
                    output_filename = f'concatenated_{base_filename}.fa'
                    concatenate_fasta_files(untrimmed_file, filename, output_filename)
                    break
        else:
            print(f"Warning: Corresponding untrimmed file for {filename} not found.")
