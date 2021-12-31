for VARIABLE in 0 1 2
do
    ssh blpc$VARIABLE bash BL-Armada/singularity_full.sh
done