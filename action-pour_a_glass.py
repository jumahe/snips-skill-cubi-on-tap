#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import json
import os
from time import sleep
from RPi import GPIO

POURING_TIME = 5

def subscribe_intent_callback(hermes, intentMessage):
    action_wrapper(hermes, intentMessage)

def action_wrapper(hermes, intentMessage):
    current_session_id = intentMessage.session_id
    say("Voici votre boisson.")
    GPIO.output(14, GPIO.HIGH)
    sleep(POURING_TIME)
    GPIO.output(14, GPIO.LOW)
    say("Votre boisson est prête.")
    hermes.publish_end_session(current_session_id, "A bientôt.")

def say(text):
    payload = json.dumps({"text":text,"siteId":"default","lang":"fr"})
    pub_str = "mosquitto_pub -p 1883 -t hermes/tts/say -m '{0}'".format(payload)
    os.system(pub_str)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.output(14, GPIO.LOW)
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("jumahe:pour_a_glass", subscribe_intent_callback).start()
