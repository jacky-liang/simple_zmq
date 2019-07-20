import zmq
from pickle import dumps, loads

from .utils import data_to_msg, msg_to_data


class SimpleZMQPublisher:

    def __init__(self, ip, port, topic):
        self._socket = zmq.Context().socket(zmq.PUB)
        self._socket.bind('tcp://{}:{}'.format(ip, port))

        self._topic = topic

    def push(self, data):
        msg = data_to_msg(data)
        self.push_raw(msg)

    def push_raw(self, raw_msg):
        self._socket.send_string('{} {}'.format(self._topic, raw_msg))


class SimpleZMQSubscriber:

    def __init__(self, ip, port, topic, buffer_len=1):
        self._socket = zmq.Context().socket(zmq.SUB)
        self._socket.setsockopt(zmq.CONFLATE, 1)

        try:
            self._socket.setsockopt_string(zmq.SUBSCRIBE, topic)
        except:
            self._socket.setsockopt(zmq.SUBSCRIBE, b'{}'.format(topic))

        self._socket.connect('tcp://{}:{}'.format(ip, port))

        self._topic = topic

    def get(self):
        msg = self._socket.recv_string()[len(self._topic) + 1:]
        return msg_to_data(msg)