#!/usr/bin/python
#-*- coding: utf-8 -*-

from .Annotation import Annotation

class TokenAnnotation(Annotation):

    def __init__(self,pTokenIndex:int,pLabel:str=""):
        self._type = "token"
        self._token = pTokenIndex
        self._label = pLabel

    def getTokenIndex(self):
        return self._token

    def getLabel(self):
        return self._label

    def TAS(self):
        d = {}
        d["type"] = self._type
        d["label"] = self._label
        d["token_index"] = self._token
        return d
