#!/bin/bash

#SBATCH info

module load mafft
module load iq-tree

mafft.bat --thread 4 --auto --amino vision_gene_seq.fasta > vision_gene_aligned.fasta

iqtree2 -s vision_gene_aligned.fasta -m MFP -B 1000 -alrt 1000 -T 8
