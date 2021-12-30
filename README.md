# BL-Armada
Breakthrough Listen Armada - on premise distributed computing workload manager. Collection of scripts to spawn a fleet of workloads on demand

### SLURM Commands 
To operate some of these scripts we need to know some basic commands. 
- squeue -u < username >
gives you the queue and status of the jobs being ran
- scancel < number >
Lets you cancel runs in the queue 
 - sbatch < file name> 
Lets you run batches of jobs that yuou want to get done
- sinfo
shows you all the parition information 
- scontrol
shows you commands to control slurm, use scontrol ping to check if the slurm is up and running
- scontrol show node blpc0
in case you want to check the resources for that compute node.
- htop -u < username >
helps you look at if your job is indeed running


Useful links to documentations (samples)[https://help.rc.ufl.edu/doc/Sample_SLURM_Scripts#Sample_SLURM_Scripts] and (docs)[https://slurm.schedmd.com/documentation.html] and other (links)[https://riffomonas.org/code_club/2021-07-21-slurm]