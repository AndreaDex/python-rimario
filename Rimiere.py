# In onore del settecentesimo anno dalla morte del Sommo Poeta
# prova anche tu a scrivere la tua Divina Commedia!
# divertiti a scrivere rime con questo semplice programma

import os

from _funzioni import *


def inizia():
    scrivendo = True
    poema = []
    # Inizia a scrivere e chiede conferma sul continuare
    while scrivendo:
        scrivere_poema(poema)
        salva_poema(poema)
        continuare = input('Vuoi continuare a scrivere ? (s/n) : ')
        if continuare.lower() == "s":
            scrivendo = True
        else:
            scrivendo = False
            print('Arrivederci grande poeta :)')


inizia()
