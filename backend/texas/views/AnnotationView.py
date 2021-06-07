#!/usr/bin/python
#-*- coding: utf-8 -*-

from texas.annotations.AnnotationSet import AnnotationSet
from texas.core.Metadata import Metadata

class AnnotationView:

    def __init__(self, pName:str, pType:str):
        if not (pName is None or type(pName) is str):
            raise Exception("AnnotationView 'pName' parameter type is required to be 'str'");
        if not (pType is None or type(pType) is str):
            raise Exception("AnnotationView 'pType' parameter type is required to be 'str'");
        pName = pName.strip()
        pType = pType.strip()
        if len(pName) == 0:
            raise Exception("AnnotationView 'pName' parameter is empty");
        if len(pType) == 0:
            raise Exception("AnnotationView 'pType' parameter is empty");
        self._name = pName
        self._type = pType
        self._meta = Metadata()
        self._anns = AnnotationSet()

    def getName(self):
        return self._name
    def name(self):
        return self._name

    def getType(self):
        return self._type
    def type(self):
        return self._type

    def getMeta(self):
        return self._meta
    def meta(self):
        return self._meta

    def getAnnSet(self):
        return self._anns
    def annSet(self):
        return self._anns
   
    def TAS(self):
        d = {"name": self.getName(), "type": self.getType()}
        if self.getMeta() is not None and self.getMeta().size() > 0:
            d["meta"] = self.getMeta().TAS()
        d["anns"] = self.getAnnSet().TAS()
        return d

    def reverse(self, jss:dict):
        #print(">>>>>",jss)
        if jss is None:
            return
        if not type(jss) is dict:
            raise Exception("AnnotationView reverse JSON-Serializable-Schema 'jss' parameter is required to be 'dict'");
        if "meta" in jss:
            self.getMeta().reverse(jss["meta"])
        if "anns" in jss:
            #print(">>>>>",jss["anns"])
            self.getAnnSet().reverse(jss["anns"])
