import logging

import server_pb2
import server_pb2_grpc


def init_logging() -> None:
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('hello')


def init() -> None:
    init_logging()


def main() -> None:
    init()


if __name__ == '__main__':
    main()
