#!/bin/bash

#SBATCH -p 128x24   # Partition name
#SBATCH -J orthofinder2        # Job name
#SBATCH -o orthofinder2_peptides.out    # Name of stdout output file

module load orthofinder/orthofinder-2.5.5 

orthofinder -f cnidaria_peptide_seq/
