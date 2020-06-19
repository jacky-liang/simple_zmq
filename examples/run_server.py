from __future__ import print_function
from time import time
from simple_zmq import SimpleZMQServer

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = '5555'

    server = SimpleZMQServer(ip, port)

    print('Running server...')
    while True:
        req = server.recv()
        print('Got req')
        server.rep(req)