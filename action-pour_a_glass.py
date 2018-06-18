#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import json
import os
from time import sleep
from RPi import GPIO

POURING_TIME = 10

def subscribe_intent_callback(hermes, intentMessage):
    action_wrapper(hermes, intentMessage)

def action_wrapper(hermes, intentMessage):
    current_session_id = intentMessage.session_id
    say("c'est parti.")
    GPIO.output(14, GPIO.HIGH)
    sleep(POURING_TIME)
    GPIO.output(14, GPIO.LOW)
    result_sentence = "Voici votre boisson."
    hermes.publish_end_session(current_session_id, result_sentence)

def say(text):
    os.system('mosquitto_pub -p 1883 -t hermes/tts/say -m "{"text":"'+text+'","siteId":"default"}"')

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.output(14, GPIO.LOW)
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("jumahe:pour_a_glass", subscribe_intent_callback).start()
