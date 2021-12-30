#!/bin/bash
#SBATCH --job-name=array_job_test   # Job name
#SBATCH --mail-type=FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=peterxy.ma@gmail.com   # Where to send mail	
#SBATCH --ntasks=1                  # Run a single task
#SBATCH --mem=1                     # Job Memory
#SBATCH --time=00:05:00             # Time limit hrs:min:sec
#SBATCH --output=array_%A-%a.log    # Standard output and error log
#SBATCH --array=1-5                 # Array range

echo This is task $SLURM_ARRAY_TASK_ID
