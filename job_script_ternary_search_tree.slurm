#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:10:00

module load Python/3.12.3-GCCcore-13.3.0
module load matplotlib/3.9.2-gfbf-2024a

time python ternary_search_tree.py
