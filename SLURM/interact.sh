#!/bin/bash

srun --account=pma --partition=standard --time=02:00:00 --ntasks=1 --cpus-per-task=1 --nodes=1 --mem=6GB --pty /bin/bash