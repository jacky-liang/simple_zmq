from __future__ import print_function
from simple_zmq import SimpleZMQSubscriber

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = '5555'
    topic = 'topic'

    sub = SimpleZMQSubscriber(ip, port, topic)

    print('Running subscriber...')
    while True:
        data = sub.get()
        print(data)
