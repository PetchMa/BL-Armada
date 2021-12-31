#!/bin/bash
#SBATCH --job-name=vasptest
#SBATCH --output=vasp.out
#SBATCH --error=vasp.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=peterxy.ma@gmail.com
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-node=8
#SBATCH --distribution=cyclic:cyclic
#SBATCH --mem-per-cpu=7000mb
#SBATCH --partition=gpu
#SBATCH --gpus:tesla:4
#SBATCH --time=00:30:00

module purge
module load cuda/10.0.130  intel/2018  openmpi/4.0.0 vasp/5.4.4

srun --mpi=pmix_v3 vasp_gpu
