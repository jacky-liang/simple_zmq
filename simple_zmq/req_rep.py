import zmq
from pickle import dumps, loads

from .utils import msg_to_data, data_to_msg


class SimpleZMQClient:

    def __init__(self, ip, port):
        self._socket = zmq.Context().socket(zmq.REQ)
        self._socket.connect('tcp://{}:{}'.format(ip, port))

    def send(self, data):
        self._socket.send_string(data_to_msg(data))
        rep_msg = self._socket.recv_string()
        return msg_to_data(rep_msg)


class SimpleZMQServer:

    def __init__(self, ip, port):
        self._socket = zmq.Context().socket(zmq.REP)
        self._socket.bind('tcp://{}:{}'.format(ip, port))

        self._sent_rep = True

    def recv(self):
        if not self._sent_rep:
            raise ValueError('Cannot recv before replying to previous req!')

        msg = self._socket.recv_string()
        self._sent_rep = False
        return msg_to_data(msg)

    def rep(self, data):
        self._socket.send_string(data_to_msg(data))
        self._sent_rep = True
