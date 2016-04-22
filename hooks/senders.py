import zmq
import json
import yaml
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
    def send(message):
        route = message.pop('route')
        try:
            requests.post(
                route,
                data=message
            )
            logger.debug(json.dumps(message))
        except Exception, e:
            logger.debug(str(e))


logger = logging.getLogger('hooks')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('/tmp/hooks.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)




