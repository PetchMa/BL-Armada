import sys
import zmq
import logging
import time

def sub_collect(port):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect ("tcp://localhost:"+str(port))
    topicfilter = ""
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

    result = socket.recv_pyobj()
    return result

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
    worker_status['status'] = 'idle'
    worker_status['task']= '' 
    consumer_sender.send_pyobj(worker_status)
    while True:
        # take care of getting new task 
        print("Waiting for new tasks....")
        print(worker_status)
        consumer_sender.send_pyobj(worker_status)
        flag = True
        while flag:
            task = sub_collect(2000)
            if task['node']==compute_node:
                worker_status['task'] = task['job']
                worker_status['status'] = 'busy'
                print(worker_status)
                consumer_sender.send_pyobj(worker_status)
                flag = False
            else:
                print("did not get task for this machine")
        time.sleep(20)
        print("done JOB! Now Idle")
        worker_status['status'] = 'idle'
        worker_status['task']= '' 
        


consumer()
