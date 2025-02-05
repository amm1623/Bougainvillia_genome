#bash info

conda minimap2 -ax map-pb \
-t16 Boug_het_asm.p_ctg.fa \
Boug_HiFi.fastq.gz \
| samtools sort -@16 -O BAM -o Boug_het_assembly.reads.bam -
