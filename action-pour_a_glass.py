#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import json
from time import sleep
from RPi import GPIO

POURING_TIME = 10

def subscribe_intent_callback(hermes, intentMessage):
    action_wrapper(hermes, intentMessage)

def action_wrapper(hermes, intentMessage):
    say(hermes,"Préparez votre verre, je vous sers dans 3 secondes...")
    sleep(1)
    say(hermes,"2 secondes")
    sleep(1)
    say(hermes,"1 seconde. Attention...")
    sleep(1)
    GPIO.output(14, GPIO.HIGH)
    sleep(POURING_TIME)
    GPIO.output(14, GPIO.LOW)
    current_session_id = intentMessage.session_id
    result_sentence = "Votre boisson est prête."
    hermes.publish_end_session(current_session_id, result_sentence)

def say(hermes, text):
    hermes.publish('hermes/tts/say', json.dumps({'text': text}))

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.output(14, GPIO.LOW)
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("jumahe:pour_a_glass", subscribe_intent_callback).start()
