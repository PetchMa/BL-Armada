#!/bin/bash
#SBATCH --mail-user=peterxy.ma@gmail.com
#SBATCH --mail-type=BEGIN,END
#SBATCH --cpus-per-task=16
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=4g
#SBATCH --time=2:00:00
#SBATCH --account=blpc0
#SBATCH --partition=standard
#SBATCH --output=%x.o%A_%a

echo "Running plot script on a single CPU core"

python multicore_test.py

