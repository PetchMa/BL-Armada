while getopts u:a:f: flag
do
    case "${flag}" in
        u) instance_num=${OPTARG};;
    esac
done
# python3 BL-Armada/SLURM/write.py
python3 BL-Armada/worker.py $instance_num