import sys
from random import randint
import pickle

import hash


def test(filename):

    pickleInput = pickle.load(open(filename, "rb"))

    m = pickleInput[0]
    percentuali = pickleInput[1]

    risultati = {}

    for percentuale in percentuali:

        # inizializzo contatori per questa percentuale
        minCollisionsIA = sys.maxint
        medCollisionsIA = 0.0
        maxCollisionsIA = 0
        medSequencesLengthIA = 0.0
        maxSequencesLengthIA = 0

        minCollisionsC = sys.maxint
        medCollisionsC = 0.0
        maxCollisionsC = 0

        for i in range(20):
            # creo due tabelle hash, una per tabelle ad indirizzamento aperto e l'altra con concatenamento
            hashTableIA = hash.HashIA(m)
            hashTableC = hash.HashC(m)
            # riempio le due tabelle
            l = len(hashTableIA.table)
            maxN = l*100
            for j in range(l * percentuale/100):
                hashTableIA.insert(randint(0, maxN))
            l = len(hashTableC.table)
            maxN = l*100
            for j in range(l * percentuale/100):
                hashTableC.insert(randint(0, maxN))

            # conto lunghezza sequenze nelle hash ad indirizzamento aperto
            seqMedia, seqMassima = hashTableIA.countSequences()
            numCollisionsIA = hashTableIA.countCollisions()

            medCollisionsIA += numCollisionsIA
            if numCollisionsIA > maxCollisionsIA:
                maxCollisionsIA = numCollisionsIA
            elif numCollisionsIA < minCollisionsIA:
                minCollisionsIA = numCollisionsIA

            medSequencesLengthIA += seqMedia
            if seqMassima > maxSequencesLengthIA:
                maxSequencesLengthIA = seqMassima
            
            # conto le collisioni nella tabella hash con concatenamento
            numCollisionsC = hashTableC.countTotalCollisions()

            medCollisionsC += numCollisionsC
            if numCollisionsC > maxCollisionsC:
                maxCollisionsC = numCollisionsC
            elif numCollisionsC < minCollisionsC:
                minCollisionsC = numCollisionsC

        medCollisionsIA /= 20
        medSequencesLengthIA /= 20
        medCollisionsC /= 20

        medCollisionsIA = round(medCollisionsIA, 1)
        medSequencesLengthIA = round(medSequencesLengthIA, 1)
        medCollisionsC = round(medCollisionsC, 1)

        risultati[percentuale] = [minCollisionsIA, medCollisionsIA, maxCollisionsIA, medSequencesLengthIA, maxSequencesLengthIA, minCollisionsC, medCollisionsC, maxCollisionsC]

    # adesso salvo l'esito degli esperimenti
    filename = "testOutput.p"
    pickle.dump(risultati, open(filename, "wb"))
    return filename
