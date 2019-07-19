from __future__ import print_function
from time import time
from simple_zmq import SimpleZMQPublisher

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = '5555'
    topic = 'topic'

    pub = SimpleZMQPublisher(ip, port, topic)

    print('Running publisher...')
    while True:
        data = {'time': time()}
        pub.push(data)
        