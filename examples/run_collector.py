from __future__ import print_function
from time import time
from simple_zmq import SimpleZMQCollector

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = '5555'

    col = SimpleZMQCollector(ip, port)

    print('Running collector...')
    while True:
        data = col.get()
        print(data)
        