import atexit
import concurrent
import concurrent.futures as futures
import grpc
import logging
import os

import server_pb2
import server_pb2_grpc


port: str = None


def init_env() -> None:
    global port
    port = os.environ['CONF_PORT']

    logging.info('Found CONF_PORT at %s', port)


def init_atexit() -> None:
    def end():
        logging.info('bye')

    atexit.register(end)


def init_logging() -> None:
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('hi')


def init() -> None:
    init_logging()
    init_atexit()
    init_env()


def main() -> None:
    init()


if __name__ == '__main__':
    main()
