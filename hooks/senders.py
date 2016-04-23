import zmq
import json
import logging
import requests


class Sender(object):
    pass


class AsyncSender(Sender):
    @staticmethod
    def send(message):
        context = zmq.Context()
        sock = context.socket(zmq.PUSH)
        sock.connect("tcp://127.0.0.1:5555")
        sock.send(
            json.dumps(message))


class SyncSender(Sender):
    @staticmethod
    def send(event_type, message):
        logger = logging.getLogger(event_type)
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler('/tmp/hooks.log')
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        logger.addHandler(fh)

        logger.debug(json.dumps(message))

        route = message.pop('route')
        try:
            for r in list(route):
                requests.post(
                    r,
                    data=message,
                    verify=False
                )

        except Exception, e:
            logger.debug(str(e))

