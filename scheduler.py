#
#   Hello World client in Python
import zmq
import random
import sys
import time
import logging
import time

def publish(port, data, ticks=2):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s" % 2000)
    count =0
    while count <ticks:
        socket.send_pyobj(data)
        time.sleep(1)
        count+=1

logger = logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('logs/scheduler.log')
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
logger.info("Starting Scheduler")


def result_collector():
    collection_status = {}
    while True:
        context = zmq.Context()
        results_receiver = context.socket(zmq.PULL)
        results_receiver.bind("tcp://127.0.0.1:9000")
        result = results_receiver.recv_pyobj()
        print(result)
        node = result['node']
        collection_status[str(node)] = result
        # print(collection_status)

        for key in collection_status.keys():
            if collection_status[key]['status'] =="idle":
                task = {}
                task['node'] = collection_status[key]['node'] 
                task['job'] = " compute this stuff here"
                publish(2000, task)
                print("Delivered Task")
                result = results_receiver.recv_pyobj()
                print(result)

result_collector()