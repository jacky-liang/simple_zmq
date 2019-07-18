import zmq
from pickle import dumps

class SimpleZMQPublisher:

    def __init__(self, ip, port, topic):
        self._socket = zmq.Context().socket(zmq.PUB)
        self._socket.bind('tcp://{}:{}'.format(ip, port))

        self._topic = topic

    def push(self, data):
        msg = repr(dumps(data, protocol=2))
        self._socket.send_string('{} {}'.format(self._topic, msg))
