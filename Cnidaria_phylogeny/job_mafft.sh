module load mafft

# Loop through all FASTA files starting with 'concatenated'
for i in concatenated*.fa; do
    # Check if the file exists
    if [[ ! -f "$i" ]]; then
        echo "No files starting with 'concatenated' found."
        exit 1
    fi

    # Create an output filename by adding "_aligned.fast" to the original name
    output_file="${i%.fa}_aligned.fa"

    # Check if the output file already exists
    if [[ -f "$output_file" ]]; then
        echo "$output_file already exists. Skipping."
        continue
    fi

    echo "Processing $i..."
    
    # Run MAFFT with the --auto option
    if mafft.bat --auto "$i" > "$output_file" 2> "${i%.fa}_error.log"; then
        echo "Finished processing $i. Output saved to $output_file."
    else
        echo "MAFFT failed on $i. Check ${i%.fa}_error.log for details."
    fi
done

echo "MAFFT processing completed."
