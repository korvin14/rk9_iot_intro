import sys
from pubnub import Pubnub

pubnub = Pubnub(publish_key='pub-c-7f7941c8-87c0-4f99-b2b9-44a9040b5dbd',
                subscribe_key='sub-c-76755bf8-43f7-11e7-b66e-0619f8945a4f')

channel = 'hello-pi'

data = {
    'username': 'Your name',
    'message': 'Hello World from Pi!'
}


def callback(m):
    print(m)

pubnub.publish(channel, data, callback=callback, error=callback)
