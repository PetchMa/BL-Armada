for VARIABLE in 0 1 2
do
    ssh blpc$VARIABLE singularity instance stop -a
done
singularity instance stop -a