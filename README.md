# BL-Armada
Breakthrough Listen Armada - on premise distributed computing workload manager. Collection of scripts to spawn a fleet of workloads on demand

### Spawn Containers
In a series of scripts spawning containers has been made possible to initalize the enviroments. The way in which the containers are spwaned follows a simple series of threaded commands. 
1. First Head node specifies how many nodes and how many instances on each node
2. Second for each node we split resources evenly and start up instances
3. With resources spawned we can then go on waking up scheduler.
```
bash 
```
