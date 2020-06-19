import zmq

from .utils import msg_to_data, data_to_msg


class SimpleZMQClient:

    def __init__(self, ip, port):
        self._socket = zmq.Context().socket(zmq.REQ)
        self._socket.connect('tcp://{}:{}'.format(ip, port))

    def send(self, data, raw=False):
        if raw:
            msg = data
        else:
            msg = data_to_msg(data)

        self._socket.send_string(msg)
        rep_msg = self._socket.recv_string()
        if raw:
            return rep_msg
        return msg_to_data(rep_msg)
        

class SimpleZMQServer:

    def __init__(self, ip, port):
        self._socket = zmq.Context().socket(zmq.REP)
        self._socket.bind('tcp://{}:{}'.format(ip, port))

        self._sent_rep = True

    def recv(self, raw=False):
        if not self._sent_rep:
            raise ValueError('Cannot recv before replying to previous req!')

        msg = self._socket.recv_string()
        self._sent_rep = False

        if raw:
            return msg
        return msg_to_data(msg)

    def rep(self, data, raw=False):
        if raw:
            msg = data
        else:
            msg = data_to_msg(data)
        
        self._socket.send_string(msg)
        self._sent_rep = True
