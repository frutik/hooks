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
        routes = yaml.load(
            open(
                '/etc/asterisk/call_hooks/routes.yml',
                'r'))
        requests.post(
            routes[message['type']],
            data=message
        )
