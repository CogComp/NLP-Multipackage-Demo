#!/usr/bin/python
#-*- coding: utf-8 -*-

class Bits:
    def __init__(self):
        self._bits = None

    def add(self, pBit):
        if self._bits is None:
            self._bits = []
        # How to check 'TextAnnotationSchema' class (?)
        # if not isinstance(pBit, TextAnnotationSchema):
        #    raise Exception("TexAS 'bit' is required to be an instance from class 'TextAnnotationSchema'");
        self._bits.append(pBit)

    def size(self):
        if self._bits is None:
            self._bits = []
        return len(self._bits)

    def getList(self):
        if self._bits is None:
            self._bits = []
        return self._bits
    def list(self):
        return self.getList()

    def filterByType(self, pType:str):
        if self._bits is None:
            self._bits = []
        l = []
        for bit in self._bits:
            if bit.getType == pType:
                l.append(bit)
        return l

    def TAS(self):
        if self._bits is None:
            self._bits = []
        d = []
        for bit in self._bits:
            d.append(bit.TAS())
        return d

