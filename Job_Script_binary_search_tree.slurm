#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=05:00:00

module load Python/3.12.3-GCCcore-13.3.0
module load matplotlib/3.9.2-gfbf-2024a

time python Binary_Tree.py
