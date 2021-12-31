import sys
import zmq
import logging
import time


compute_node = sys.argv[1]

logger = logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
# fh = logging.FileHandler('BL-Armada/logs/worker_'+str(compute_node)+'.log')
fh = logging.FileHandler('logs/worker_'+str(compute_node)+'.log')

fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)





def consumer():
    context = zmq.Context()
    # recieve work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:9000")
    worker_status = {}
    worker_status['node'] = compute_node
    
    while True:
        worker_status['status'] = 'starting'
        print(worker_status)
        consumer_sender.send_pyobj(worker_status)
        time.sleep(10)
        worker_status['status'] = 'busy'
        print(worker_status)
        consumer_sender.send_pyobj(worker_status)
        time.sleep(10)
        worker_status['status'] = 'idle'
        print(worker_status)
        # take care of getting new task 
        print("Waiting for new tasks....")
        consumer_sender.send_pyobj(worker_status)
        context = zmq.Context()
        SUB_SCRIBER = context.socket(zmq.SUB)
        SUB_SCRIBER.connect("tcp://127.0.0.1:9001")
        task = SUB_SCRIBER.recv()
        print(task)

consumer()
