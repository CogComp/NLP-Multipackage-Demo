#!/usr/bin/python
#-*- coding: utf-8 -*-

from texas.anns.AnnotationSet import AnnotationSet
from texas.core.Metadata import Metadata

class AnnotationView:

    def __init__(self, pName : str, pType : str = None):
        if not (pName is None or type(pName) is str):
            raise Exception("AnnotationView 'pName' parameter type is required to be 'str'");
        pName = pName.strip()
        if len(pName) == 0:
            raise Exception("AnnotationView 'pName' parameter is empty");
        self._name = pName
        self.setType( pType )
        self._meta = Metadata()
        self._anns = AnnotationSet()
        self.setTexasClass("tx.view.AnnotationView")

    def getTexasClass(self) -> str:
        return self._txClass
    def txClass(self) -> str:
        return self._txClass
    def setTexasClass(self,pClass) -> str:
        if not (type(pClass) is str):
            raise Exception("AnnotationView 'pClass' parameter type is required to be 'str'");
        self._txClass = pClass

    def getName(self):
        return self._name
    def name(self):
        return self._name

    def setType(self,pType : str):
        if not (pType is None or type(pType) is str):
            raise Exception("AnnotationView 'pType' parameter type is required to be 'str'");
        if not pType is None: 
            pType = pType.strip()
        if not pType is None and len(pType) == 0:
            raise Exception("AnnotationView 'pType' parameter is empty");
        self._type = pType
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
        d = {"name": self.getName()}
        if not self.getType() is None:
            d = {"type": self.getType()}
        if self.getMeta() is not None and self.getMeta().size() > 0:
            d["meta"] = self.getMeta().TAS()
        d["anns"] = self.getAnnSet().TAS()
        d["texas.class"] = self._txClass
        return d

    def reverse(self, jss:dict):
        #print(">>>>>",jss)
        if jss is None:
            return
        if not type(jss) is dict:
            raise Exception("AnnotationView reverse JSON-Serializable-Schema 'jss' parameter is required to be 'dict'");
        if "type" in jss:
            self.setType(jss["type"])
        if "meta" in jss:
            self.getMeta().reverse(jss["meta"])
        if "anns" in jss:
            #print(">>>>>",jss["anns"])
            self.getAnnSet().reverse(jss["anns"])
        if "texas.class" in jss:
            self.setTexasClass(jss["texas.class"])
        