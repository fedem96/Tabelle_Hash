import numpy as np
import math


class Hash:

    def isPrime(self, m):
        for i in range(2, int(math.sqrt(m)) + 1):
            if m % i == 0:
                return False
        return True

    def hash(self, key):
        return key % len(self.table)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Tabella hash: m = " + str(len(self.table)) + ", contenuto = " + str(self.table)


class HashIA(Hash):
    def __init__(self, m):
        self.table = []
        while not self.isPrime(m):
            m += 1
        # adesso mi creo la tabella
        for i in range(m):
            self.table.append(None)

    def insert(self, key):
        i = 0
        h = self.hash(key)
        while i < len(self.table) and self.table[h] is not None and self.table[h] is not False:
            i += 1
            h = (h + 1) % len(self.table)
        if i == len(self.table):
            return False
        self.table[h] = key
        return True

    def search(self, key):
        i = 0
        h = self.hash(key)
        while i < len(self.table) and self.table[h] is not None:
            if self.table[h] == key:
                return h
            i += 1
            h = (h + 1) % len(self.table)
        return -1

    def delete(self, key):
        i = self.search(key)
        if i == -1:
            return False
        self.table[i] = False
        return True

    def countCollisions(self):
        count = 0
        t = self.table
        l = len(t)
        for i in range(l):
            element = t[i]
            if element is not None and element is not False and self.hash(element) != i:
                elementCollisions = i - (element % l)
                if elementCollisions < 0:
                    elementCollisions += l
                count += elementCollisions
        return count

    def countSequences(self):
        medio = 0.0
        massimo = 0
        t = self.table
        l = len(t)
        for i in range(l):
            sequenceLength = 0
            # while t[(i+sequenceLength) % l] is not None and t[(i+sequenceLength) % l] is not False and sequenceLength < l:
            while t[(i + sequenceLength) % l] is not None and sequenceLength < l:
                sequenceLength += 1
            if sequenceLength > massimo:
                if sequenceLength == l - 1:
                    return (l - 1) / 2, l - 1
                elif sequenceLength == l:
                    return l, l
                massimo = sequenceLength
            medio += sequenceLength
        medio = medio / len(t)
        return medio, massimo


class HashC(Hash):
    def __init__(self, m):
        # Hash.__init__(self)
        self.table = []
        while not self.isPrime(m):
            m -= 1
        for i in range(m):
            self.table.append([])

    def insert(self, key):
        h = self.hash(key)
        self.table[h].append(key)
        return True

    def search(self, key):
        h = self.hash(key)
        return h, self.table[h].index(key)

    def delete(self, key):
        h = self.hash(key)
        for i in range(len(self.table[h])):
            if self.table[h][i] == key:
                del self.table[h][i]
                return True
        return False

    def countTotalCollisions(self):
        count = 0
        for lista in self.table:
            if len(lista) > 1:
                count += len(lista) - 1
        return count
