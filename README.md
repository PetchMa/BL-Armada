# BL-Armada 🛳
Breakthrough Listen Armada - internal premise distributed computing "custom orchestration" technique. Used to spawn a fleet of workloads to process data. Facilitates some basic networking infrastructure to monitor and distribute workload in a round robin fashion. 

### Spawn Containers
In a series of scripts spawning containers has been made possible to initalize the enviroments. The way in which the containers are spwaned follows a simple series of threaded commands. 
1. First Head node specifies how many nodes and how many instances on each node
2. Second for each node we split resources evenly and start up instances
3. With resources spawned we can then go on waking up scheduler.
recall some basic singularity commands 
```
singularity instance list
singularity instance stop -a
```
The command to spawn instances is:
```
bash spawn_containers.sh -u 1
```