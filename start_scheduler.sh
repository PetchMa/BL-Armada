singularity instance start ../peterma-ml scheduler
screen -d -m singularity exec instance://scheduler python scheduler.py