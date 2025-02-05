#Process subreads from PacBio using ccs https://anaconda.org/bioconda/pbccs

/home/amaciasm/miniconda3/bin/ccs …/m54284U_220502_104309.subreads.bam Boug1_cell1_ccs.bam

/home/amaciasm/miniconda3/bin/ccs …/m54284U_220503_165459.subreads.bam Boug1_cell2_ccs.bam

#bash job 2 bam2fastq output is a fastq file

/home/amaciasm/miniconda3/bin/bam2fastq -o Boug_HiFi Boug1_cell1_ccs.bam Boug1_cell2_ccs.bam

#bash job 3 adapter filter

source activate /home/amaciasm/miniconda3

/home/amaciasm/Bougainvillia/HiFiAdapterFilt-master/pbadapterfilt.sh -p Boug_HiFi -o Boug_HiFi_adap_filt

#bash job 4 hifiasm to assemble the genome https://github.com/chhylp123/hifiasm 

/home/amaciasm/Bougainvillia/hifiasm/hifiasm -o Boug_het.asm -t32 /home/amaciasm/Bougainvillia/Boug_HiFi_adap_filt/Boug_HiFi.filt.fastq.gz
