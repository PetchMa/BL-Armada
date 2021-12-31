while getopts u:a:f: flag
do
    case "${flag}" in
        u) num_instances=${OPTARG};;
    esac
done

for VARIABLE in 0 1 2
do
    ssh blpc$VARIABLE bash BL-Armada/spawn_subcontainers.sh -u $num_instances
done