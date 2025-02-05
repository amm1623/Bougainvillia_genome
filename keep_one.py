import os
from Bio import SeqIO

def process_fasta(file_path):
    sequences = []
    # Read sequences from the FASTA file
    with open(file_path, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            sequences.append(record)

    # Filter sequences based on gaps
    best_sequence = None
    for seq in sequences:
        gap_count = seq.seq.count('-')
        if best_sequence is None:
            best_sequence = seq
        else:
            best_gap_count = best_sequence.seq.count('-')
            # Check for fewer gaps or longer sequence
            if gap_count < best_gap_count or (gap_count == best_gap_count and len(seq) > len(best_sequence)):
                best_sequence = seq

    # Write the best sequence to a new file or print it
    if best_sequence:
        output_file = f'filtered_{os.path.basename(file_path)}'
        with open(output_file, 'w') as out_file:
            SeqIO.write(best_sequence, out_file, 'fasta')
        print(f'Saved filtered sequence to {output_file}')

# Process all FASTA files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.h2a.fa'):
        process_fasta(filename)
