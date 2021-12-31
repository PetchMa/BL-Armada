import sys
import zmq
import logging
import time


compute_node = sys.argv[1]




logger = logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('BL-Armada/logs/worker_'+str(compute_node)+'.log')
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


for i in range(10):
    # string = socket.recv()
    # topic, messagedata = string.split()
    # total_value += int(messagedata)
    time.sleep(1)
    logger.info("taking")