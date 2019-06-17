#import zmq
import json
import logging
import requests


class Sender(object):
    pass


class Response(object):
    def __init__(self, response=None):
        pass

    def time(self):
        return None

    def status(self):
        return None

    def message(self):
        return None


class RequestsResponse(object):
    def __init__(self, response=None):
        self.response = response

    def time(self):
        return self.response.elapsed

    def status(self):
        return self.response.status_code

    def message(self):
        return self.response.text


class AsyncSender(Sender):
    @staticmethod
    def send(route, message, timeout=10):
        context = zmq.Context()
        sock = context.socket(zmq.PUSH)
        sock.connect("tcp://127.0.0.1:5555")
        sock.send(
            json.dumps(message))

        return Response()


class SyncSender(Sender):
    @staticmethod
    def send(route, message, timeout=10):
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
            result = requests.post(
                route,
                data=message,
                verify=False,
                timeout=timeout
            )
            message['result']['code'] = result.status_code
            if result.status_code != 200:
                message['result']['message'] = result.text
        except Exception, e:
            logger.exception(str(e))
            message['result']['exception'] = e.message

        logger.debug(json.dumps(message))

        return RequestsResponse(result)

