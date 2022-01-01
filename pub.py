import zmq
import random
import sys
import time


def publish(port, data, time)
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s" % 2000)
    count =0
    while count <10:
        socket.send("data")
        time.sleep(1)
        count+=1