#!/bin/bash
#SBATCH --job-name=parallel_job_test # Job name
#SBATCH --mail-user=petermaxy.ma@gmail.com
#SBATCH --mail-type=BEGIN,END
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=1
#SBATCH --time=2:00:00
#SBATCH --account=pma
#SBATCH --partition=allnodes
#SBATCH --output=serial_test_%j.log   # Standard output and error log
/home/pma; blpc0; date

module load python/3

python multicore_test.py

date