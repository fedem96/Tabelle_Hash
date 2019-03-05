import pickle
import matplotlib.pyplot as plt

import test

pickleTestInput = [1000, [10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90, 91, 92, 93, 94, 95, 95, 97, 98, 99, 100]]
testFileInput = "testInput.p"
pickle.dump(pickleTestInput, open(testFileInput, "wb"))
testFileOutput = test.test(testFileInput)

risultati = pickle.load(open(testFileOutput, "rb"))

print "{percentuale: [minCollisionsIA, medCollisionsIA, maxCollisionsIA, medSequencesLengthIA, maxSequencesLengthIA, minCollisionsC, medCollisionsC, maxCollisionsC], ...}"
print risultati

x = []
y = []

for i in range(8):
    y.append([])

percentuali = risultati.keys()
percentuali.sort()
for percentuale in percentuali:
    x.append(percentuale)
    for i in range(8):
        y[i].append(risultati[percentuale][i])

# grafico collisioni in indirizzamento aperto
plt.plot(x, y[0], label='Collisioni minime')
plt.plot(x, y[1], label="Collisioni medie")
plt.plot(x, y[2], label="Collisioni massime")
plt.title("Tabella Hash con indirizzamento aperto")
plt.xlabel("Percentuale di carico")
plt.ylabel("Numero di collisioni")
plt.legend(loc='upper left')
plt.show()

# grafico lunghezza sequenze in indirizzamento aperto
plt.plot(x, y[3], label="Lunghezza media")
plt.plot(x, y[4], label="Lunghezza massima")
plt.title("Tabella Hash con indirizzamento aperto")
plt.xlabel("Percentuale di carico")
plt.ylabel("Lunghezza sequenze")
plt.legend(loc='upper left')
plt.show()

# grafico collisioni in concatenamento
plt.plot(x, y[5], label='Collisioni minime')
plt.plot(x, y[6], label="Collisioni medie")
plt.plot(x, y[7], label="Collisioni massime")
plt.title("Tabella Hash con concatenamento")
plt.xlabel("Percentuale di carico")
plt.ylabel("Numero di collisioni")
plt.legend(loc='upper left')
plt.show()
