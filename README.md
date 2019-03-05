# Tabelle Hash
L’obbiettivo è verificare come si comportano le tabelle hash al crescere del numero di dati inseriti all’interno di esse. Le due tecniche di gestione delle collisioni considerate sono indirizzamento aperto e concatenamento.

## Esperimento

Per ciascuna delle tecniche di gestione delle collisioni, verrà creato un grafico in cui si riportano il numero di collisioni (minime, medie e massime in 20 tentativi diversi) al variare della percentuale di carico della tabella hash (composta da 1000 bucket). Per il metodo indirizzamento aperto, verrà creato un ulteriore grafico in cui si riportano le lunghezze delle sequenze contigue di elementi.


Per eseguire l'esperimento:

`python2 exp.py`