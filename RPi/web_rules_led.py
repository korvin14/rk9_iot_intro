import time

import RPi.GPIO as GPIO
from pubnub import Pubnub

GPIO.setmode(GPIO.BCM)
LED_PIN = 4
GPIO.setup(LED_PIN, GPIO.OUT)


pubnub = Pubnub(publish_key='pub-c-7f7941c8-87c0-4f99-b2b9-44a9040b5dbd',
                subscribe_key='sub-c-76755bf8-43f7-11e7-b66e-0619f8945a4f')


def sub_callback(message, channel):
  print 'received from web message: {}'.format(message)
  if message['led'] == 1:
    for i in range(3):
      GPIO.output(LED_PIN, True)
      time.sleep(0.5)
      GPIO.output(LED_PIN, False)
      time.sleep(0.5)

pubnub.subscribe(channels='blink_rpi_led', callback=sub_callback)
  while True:
    pass
