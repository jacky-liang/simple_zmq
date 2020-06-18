import zmq

from .utils import data_to_msg, msg_to_data


class SimpleZMQPublisher:

    def __init__(self, ip, port, topic):
        self._socket = zmq.Context().socket(zmq.PUB)
        self._socket.bind('tcp://{}:{}'.format(ip, port))

        self._topic = topic

    def push(self, data, raw=False):
        if raw:
            msg = data
        else:
            msg = data_to_msg(data)

        self._socket.send_string('{} {}'.format(self._topic, msg))


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

    def get(self, raw=False, block=True):
        if block:
            raw_msg = self._socket.recv_string()
        else:
            try:
                raw_msg = self._socket.recv_string(zmq.NOBLOCK)
            except zmq.ZMQError as e:
                if e.errno == zmq.EAGAIN:
                    return None
                else:
                    raise(e)
        
        msg = raw_msg[len(self._topic) + 1:]
        if raw:
            return msg
        return msg_to_data(msg)