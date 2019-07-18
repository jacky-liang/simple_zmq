import logging
import argparse
from time import time, sleep

from zmq_pub_sub import SimpleZMQPublisher

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', '-ip', type=str, default='127.0.0.1')
    parser.add_argument('--port', '-port', type=str, default='5555')
    parser.add_argument('--topic', '-t', type=str, default='topic')
    args = parser.parse_args()

    pub = SimpleZMQPublisher(args.ip, args.port, args.topic)

    logging.info('Running publisher...')
    while True:
        data = {'time': time()}
        pub.push(data)
        sleep(1e-3)
        