#!/usr/bin/python
#-*- coding: utf-8 -*-

from .Annotation import Annotation

class SpanAnnotation(Annotation):

    def __init__(self,pStartToken:int, pFinalToken:int, pLabel:str="", pSpan:str=None):
        self._type = "span"
        self._span = pSpan
        self._start_token = pStartToken
        self._final_token = pFinalToken
        self._label = pLabel

    def getStartToken(self):
        return self._start_token

    def getFinalToken(self):
        return self._final_token

    def getLabel(self):
        return self._label

    def getSpan(self):
        return self._span

    def TAS(self):
        d = {}
        d["type"] = self._type
        if self._span is not None and type(self._span) is str:
            d["span"] = self._span
        d["label"] = self._label
        d["start_token"] = self._start_token
        d["final_token"] = self._final_token
        return d
