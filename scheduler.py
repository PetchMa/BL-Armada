#
#   Hello World client in Python
import zmq
import random
import sys
import time
import logging


logger = logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('logs/schedule.log')
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


logger.info("scheduler")
# port = "5556"
# if len(sys.argv) > 1:
#     port =  sys.argv[1]
#     int(port)

# context = zmq.Context()
# socket = context.socket(zmq.PUB)
# socket.bind("tcp://*:%s" % port)


# while True:
#     topic = random.randrange(9999,10005)
#     messagedata = random.randrange(1,215) - 80
#     print "%d %d" % (topic, messagedata)
#     socket.send("%d %d" % (topic, messagedata))
#     time.sleep(1)