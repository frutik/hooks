#import zmq
import json
import logging
import requests


class Sender(object):
    pass


class AsyncSender(Sender):
    @staticmethod
    def send(route, message):
        context = zmq.Context()
        sock = context.socket(zmq.PUSH)
        sock.connect("tcp://127.0.0.1:5555")
        sock.send(
            json.dumps(message))


class SyncSender(Sender):
    @staticmethod
    def send(route, message):
        logger = logging.getLogger(message.get('type'))
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler('/tmp/hooks.log')
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        logger.addHandler(fh)

        message['result'] = {
            'route': route
        }

        try:
            # TODO request timeout
            result = requests.post(
                route,
                data=message,
                verify=False
            )
            message['result']['code'] = result.status_code
            if result.status_code != 200:
                message['result']['message'] = result.text
        except Exception, e:
            logger.exception(str(e))
            message['result']['exception'] = e.message

        logger.debug(json.dumps(message))

