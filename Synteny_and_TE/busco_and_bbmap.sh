
source activate /home/amaciasm/miniconda3

#before blobtoolkit
/home/amaciasm/software/busco/bin/busco -i Boug_asm.p_ctg.fa -m genome -o Boug_busco -l metazoa --offline

#on final assembly
/home/amaciasm/software/busco/bin/busco -i Bougainvillia_filtered.fa -m genome -o Boug_busco_filtered -l metazoa --offline

#before blobtoolkit
/home/amaciasm/software/bbmap/stats.sh Boug_het_asm.p_ctg.fa > Boug_het_asm_stats.out

#on final assembly
/home/amaciasm/software/bbmap/stats.sh Bougainvillia_filtered.fa > Boug_filtered_stats.out
