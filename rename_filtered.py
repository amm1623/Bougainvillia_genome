import os
from Bio import SeqIO

def rename_gene_ids(file_path, new_id):
    # Read sequences from the filtered FASTA file and rename IDs
    with open(file_path, 'r') as file:
        records = list(SeqIO.parse(file, 'fasta'))

    # Update the ID of each sequence
    for record in records:
        record.id = new_id
        record.description = ''  # Optionally clear the description

    # Write the modified sequences to a new file
    output_file = f'renamed_{os.path.basename(file_path)}'
    with open(output_file, 'w') as out_file:
        SeqIO.write(records, out_file, 'fasta')
    print(f'Saved renamed sequences to {output_file}')

# Process all filtered FASTA files in the current directory
for filename in os.listdir('.'):
    if filename.startswith('filtered_') and filename.endswith('.fa'):
        rename_gene_ids(filename, 'Bmus')
