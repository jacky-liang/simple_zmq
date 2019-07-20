import zmq
from pickle import dumps, loads

from .utils import msg_to_data, data_to_msg

class SimpleZMQProducer:

    def __init__(self, ip, port):
        self._socket = zmq.Context().socket(zmq.PUSH)
        self._socket.bind('tcp://{}:{}'.format(ip, port))

    def push(self, data):
        self.push_raw(data_to_msg(data))

    def push_raw(self, raw_msg):
        self._socket.send_string(raw_msg)


class SimpleZMQCollector:

    def __init__(self, ip, port, buffer_len=1):
        self._socket = zmq.Context().socket(zmq.PULL)
        self._socket.setsockopt(zmq.CONFLATE, buffer_len)
        self._socket.connect('tcp://{}:{}'.format(ip, port))

    def get(self):
        msg = self._socket.recv_string()
        return msg_to_data(msg)
