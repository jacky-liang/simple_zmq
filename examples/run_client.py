from __future__ import print_function
from time import time
from simple_zmq import SimpleZMQClient

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = '5555'

    client = SimpleZMQClient(ip, port)

    print('Running client...')
    while True:
        data = {'time': time()}
        rep = client.send(data)
        print(rep)        