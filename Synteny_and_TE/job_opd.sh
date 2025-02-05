# Set locale environment variables

module load miniconda3
module load blast
module load snakemake

#Activate the specific Conda environment with matplotlib installed 
conda activate …/miniconda3

snakemake -p --snakefile /hb/home/amacia16/odp/scripts/odp --configfile /hb/home/amacia16/Boug_project/analysis_odp/config.yaml --cores 16 --
directory /hb/home/amacia16/Boug_project/analysis_odp
