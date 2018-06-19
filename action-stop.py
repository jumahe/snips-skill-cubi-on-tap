#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
#from RPi import GPIO

def subscribe_intent_callback(hermes, intentMessage):
    action_wrapper(hermes, intentMessage)

def action_wrapper(hermes, intentMessage):
    result_sentence = "Arrêt de la pompe."
    current_session_id = intentMessage.session_id
    #GPIO.output(14, GPIO.LOW)
    hermes.publish_end_session(current_session_id, result_sentence)

if __name__ == "__main__":
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(14, GPIO.OUT)
    #GPIO.output(14, GPIO.LOW)
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("jumahe:stop", subscribe_intent_callback).start()
