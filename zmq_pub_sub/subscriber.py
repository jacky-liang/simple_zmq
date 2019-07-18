import zmq
from pickle import loads


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
        msg = eval(self._socket.recv_string()[len(self._topic) + 1:])

        try:
            data = loads(msg)
        except:
            data = loads(msg.encode('latin1'), encoding='latin1')
        return data
