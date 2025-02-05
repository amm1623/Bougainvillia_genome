from Bio import SeqIO

# Paths to your files
updated_fasta = "Bougainvillia_aa_cdhit.pep"  # FASTA file with duplicates removed
original_chrom = "Boug_all.chrom"  # Original chromosome file with 5 columns
output_chrom = "Boug_u.chrom"  # Output chromosome file to be created

# Step 1: Extract IDs and lengths from the updated FASTA
unique_sequences = {record.id: len(record.seq) for record in SeqIO.parse(updated_fasta, "fasta")}

# Step 2: Read the original chromosome file and update lengths based on unique sequences
with open(original_chrom, "r") as chrom_in, open(output_chrom, "w") as chrom_out:
    for line in chrom_in:
        # Strip leading/trailing whitespace and split by whitespace
        parts = line.strip().split()
        
        # Ensure there are exactly 5 parts
        if len(parts) == 5:
            chrom_name = parts[0]
            start_pos = parts[3]
            end_pos = parts[4]
            
            try:
                # Convert positions to integers and calculate length
                start_pos_int = int(start_pos)
                end_pos_int = int(end_pos)
                chrom_length = end_pos_int - start_pos_int + 1
            except ValueError:
                continue  # Skip lines where positions are not valid integers

            # Check if the chromosome name is in the unique_sequences
            if chrom_name in unique_sequences:
                # Write the original columns with updated length
                chrom_out.write(f"{chrom_name}\t{parts[1]}\t{parts[2]}\t{start_pos}\t{unique_sequences[chrom_name]}\n")

print(f"Updated chromosome file saved to {output_chrom}")
