module load miniconda3

# Loop through all FASTA files starting with 'concatenated'
for i in concatenated*_aligned.fa; do
    # Check if the file exists
    if [[ ! -f "$i" ]]; then
        echo "No files starting with 'concatenated' found."
        exit 1
    fi

    echo "Processing $i..."

    # Run Gblocks with the desired parameters
    Gblocks "$i" -b2=10 -b3=10 -b4=5 -b5=a

    echo "Finished processing $i."
done

echo "Gblocks processing completed."
