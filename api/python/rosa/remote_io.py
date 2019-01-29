import json
import websocket as ws

from threading import Thread


class RemoteIO(object):
    def __init__(self, host):
        url = 'ws://{}:1234'.format(host)
        self.ws = ws.create_connection(url)

        self.setup(
            AIN1=18, AIN2=17, PWMA=4,
            BIN1=24, BIN2=27, PWMB=22,
            STBY=23
        )

        self.last_state = {}

        self._poll_t = Thread(target=self._update_state)
        self._poll_t.daemon = True
        self._poll_t.start()

    def set_speed(self, motor, speed):
        self.ws.send(json.dumps({
            'wheels': {
                motor: speed
            }
        }))

    def buzz(self, duration):
        self.ws.send(json.dumps({'buzz': duration}))

    def setup(self,
              AIN1, AIN2, PWMA,
              BIN1, BIN2, PWMB,
              STBY):
        self.ws.send(json.dumps({
            'setup': {
                'AIN1': AIN1, 'AIN2': AIN2, 'PWMA': PWMA,
                'BIN1': BIN1, 'BIN2': BIN2, 'PWMB': PWMB,
                'STBY': STBY
            }
        }))

    def _update_state(self):
        while True:
            self.last_state.update(json.loads(self.ws.recv()))
