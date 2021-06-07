#!/usr/bin/python
#-*- coding: utf-8 -*-

from .Annotation import Annotation
from .SpanAnnotation import SpanAnnotation

class RelationAnnotation(Annotation):

    def __init__(self,pRelationName:str, pRootType:str, pRootStartToken:int, pRootFinalToken:int, pRootLabel:str="", pRootSpan:str=None):
        self._type = "relation"
        self._name = pRelationName
        self._root = SpanAnnotation(pStartToken = pRootStartToken, pFinalToken = pRootFinalToken, pLabel = pRootLabel, pSpan = pRootSpan)
        self._root._type = pRootType
        #self._span = pSpan
        #self._start_token = pStartToken
        #self._final_token = pFinalToken
        #self._label = pLabel
        
    def getName(self):
        return self._name

    def getRoot(self):
        return self._root

    '''
    def getStartToken(self):
        return self._start_token

    def getFinalToken(self):
        return self._final_token

    def getLabel(self):
        return self._label

    def getSpan(self):
        return self._span
    '''
    
    def TAS(self):
        d = {}
        d["type"] = self._type
        d["name"] = self._name
        d["root"] = self._root.TAS()
        #if self._span is not None and type(self._span) is str:
        #    d["span"] = self._span
        #d["label"] = self._label
        #d["start_token"] = self._start_token
        #d["final_token"] = self._final_token
        return d
