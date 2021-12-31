
while getopts u:a:f: flag
do
    case "${flag}" in
        u) num_instances=${OPTARG};;
    esac
done

# Or -----------------------
for VARIABLE in $(seq 1 $num_instances); do
    bash BL-Armada/singularity_full.sh -u $VARIABLE
done