import logging
import argparse
from time import sleep

from zmq_pub_sub import SimpleZMQSubscriber

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', '-ip', type=str, default='127.0.0.1')
    parser.add_argument('--port', '-port', type=str, default='5555')
    parser.add_argument('--topic', '-t', type=str, default='topic')
    args = parser.parse_args()

    sub = SimpleZMQSubscriber(args.ip, args.port, args.topic)

    logging.info('Running subscriber...')
    while True:
        data = sub.get()
        logging.info(data)
        sleep(1e-3)
