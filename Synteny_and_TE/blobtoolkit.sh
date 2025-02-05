conda activate /home/amaciasm/miniconda3/envs/btk

blobtools create -fasta Bougainvillia_het_assembly.fa -cov Boug_het_assembly.reads.bam -hits genome_blast.out -o Boug_het_blob_filter
