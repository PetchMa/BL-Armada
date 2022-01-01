import sys
import zmq

def sub_collect(port):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect ("tcp://localhost:"+str(port))
    topicfilter = ""
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

    # string = socket.recv_pyobj()
    result = socket.recv()
    return result

data = sub_collect(2000)
print(data)