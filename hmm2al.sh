#download https://github.com/josephryan/hmm2aln.pl

module load miniconda3
module load perl

# Consolidated locale settings
if locale -a | grep -q "en_US.UTF-8"; then
    export LC_ALL="en_US.UTF-8"
    export LANG="en_US.UTF-8"
    export LANGUAGE="en_US.UTF-8"
else
    export LC_ALL="C"
    export LANG="C"
    export LANGUAGE="C"
fi

# Set PERL5LIB for local Perl module path
export PERL5LIB="$HOME/perl5/lib/perl5:$PERL5LIB"

# Running the Perl script
ls -1 | perl -ne 'chomp; if (/(.*).untrimmed.fa.mafft/) { print "/hb/home/amacia16/cnidarian_trees/cnidaria_phylogeny/from_debiasse/debiasse_
et_al_cnid_partitions_fasta/hmm2aln.pl/hmm2aln.pl --hmm=$1.hmm --name=$1 --fasta=/hb/home/amacia16/Boug_project/Bougainvillia_aa.pep --thread
s=4 > $1.h2a.fa\n"; }' | sh
