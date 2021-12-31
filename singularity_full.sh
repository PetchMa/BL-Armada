while getopts u:a:f: flag
do
    case "${flag}" in
        u) instance_num=${OPTARG};;
        a) compute_num=${OPTARG};;
    esac
done

singularity instance start --nv -B /mnt_blpd7,/mnt_blpd1,/mnt_blpd10,/mnt_blpd11,/mnt_blpd12,/mnt_blpd13,/mnt_blpd14,/mnt_blpd15,/mnt_blpd16,/mnt_blpd17,/mnt_blpd18,/mnt_blpd19,/mnt_blpd2,/mnt_blpd3,/mnt_blpd4,/mnt_blpd5,/mnt_blpd6,/mnt_blpd8,/mnt_blpd9,/datax/scratch/pma  peterma-ml worker_$((instance_num))
screen -d -m singularity exec instance://worker_$((instance_num)) bash BL-Armada/run_worker.sh -u $((compute_num))
# singularity exec instance://instance_$((instance_num)) bash BL-Armada/run_worker.sh -u $((compute_num))


