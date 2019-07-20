from __future__ import print_function
from time import time
from simple_zmq import SimpleZMQProducer

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = '5555'

    prod = SimpleZMQProducer(ip, port)

    print('Running producer...')
    while True:
        data = {'time': time()}
        print('sent')
        prod.push(data)
        