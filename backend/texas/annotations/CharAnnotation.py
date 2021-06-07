#!/usr/bin/python
#-*- coding: utf-8 -*-

from .Annotation import Annotation

class CharAnnotation(Annotation):

    def __init__(self,pStartChar:int, pFinalChar:int, pLabel:str = None, pIndex:int = None):
        self._type = "char"
        if pIndex and not (type(pIndex) is int):
            raise Exception("CharAnnotation 'pIndex' parameter type is required to be 'int'");
        if not (type(pStartChar) is int):
            raise Exception("CharAnnotation 'pStartChar' parameter type is required to be 'int'");
        if not (type(pFinalChar) is int):
            raise Exception("CharAnnotation 'pEndChar' parameter type is required to be 'int'");
        if not (pLabel is None or type(pLabel) is str):
            raise Exception("CharAnnotation 'pLabel' parameter type is required to be 'str'");
        self._index = pIndex
        self._start_char = pStartChar
        self._final_char = pFinalChar
        self._label = pLabel

    def getStartChar(self):
        return self._start_char

    def getFinalChar(self):
        return self._final_char

    def getLabel(self):
        return self._label

    def getIndex(self):
        return self._index
        
    def TAS(self):
        d = {}
        d["type"] = self._type
        if self._index is not None:
            d["index"] = self._index
        d["label"] = self._label
        d["start_char"] = self._start_char
        d["final_char"] = self._final_char
        return d
