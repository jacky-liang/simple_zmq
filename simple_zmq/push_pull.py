import zmq

from .utils import msg_to_data, data_to_msg


class SimpleZMQProducer:

    def __init__(self, ip, port):
        self._socket = zmq.Context().socket(zmq.PUSH)
        self._socket.bind('tcp://{}:{}'.format(ip, port))

    def push(self, data, raw=False):
        if raw:
            msg = data
        else:
            msg = data_to_msg(data)
        self._socket.send_string(msg)


class SimpleZMQCollector:

    def __init__(self, ip, port, buffer_len=1):
        self._socket = zmq.Context().socket(zmq.PULL)
        self._socket.setsockopt(zmq.CONFLATE, buffer_len)
        self._socket.connect('tcp://{}:{}'.format(ip, port))

    def get(self, raw=False):
        msg = self._socket.recv_string()

        if raw:
            return msg
        return msg_to_data(msg)
