#bash info

module load iq-tree


iqtree2 -s alignment_matrix_all.fasta -nt AUTO -bb 1000 -m TEST 
