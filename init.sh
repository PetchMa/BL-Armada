echo "Starting Scheduler"
bash start_scheduler.sh
echo "Starting 3 Workers"
bash start_workers.sh -u 1
