#!/usr/bin/python
#-*- coding: utf-8 -*-

from texas.annotations.AnnotationSet import AnnotationSet
from texas.views.AnnotationView import AnnotationView
from texas.views.CharView import CharView
from texas.views.TokenView import TokenView
from texas.views.SpanView import SpanView
from texas.views.RelationView import RelationView

class AnnotationViewSet:
    def __init__(self):
        self._anns = {}

    def add(self, pView:AnnotationView):
        if not isinstance(pView, AnnotationView):
           raise Exception("AnnotationViewSet 'pView' parameter class is required to be 'AnnotationView'");
        pViewName = pView.getName()
        if pViewName in self._anns:
            raise Exception("AnnotationViewSet already has an AnnotationView named '"+pViewName+"'");
        self._anns[pViewName] = pView
        
    def get(self, pViewName:str):
        if pViewName not in self._anns:
            raise Exception("AnnotationView '"+pViewName+"' does NOT exist");
        return self._anns[pViewName]

    def size(self):
        return len(self._anns)
        
    def exists(self, pViewName:str):
        if pViewName in self._anns:
            return True
        else:
            return False
        
    def TAS(self):
        d = {}
        for annViewName in self._anns:
            d[annViewName] = self._anns[annViewName].TAS()
        return d
        
    def reverse(self, jss: dict):
        self._anns = {}
        if jss is None:
            return
        if not type(jss) is dict:
            raise Exception("AnnotationViewSet reverse JSON-Serializable-Schema 'jss' parameter is required to be 'dict'");
        for annViewName in jss:
            annView = jss[annViewName]
            if not "type" in annView:
                raise Exception("Missing 'type' attribute in AnnotationView '"+annViewName+"' during reverse");
            if annView["type"].endswith("AnnotationView.CharView"):
                self._anns[annViewName] = CharView(annViewName)
            elif annView["type"].endswith("AnnotationView.TokenView"):
                self._anns[annViewName] = TokenView(annViewName)
            elif annView["type"].endswith("AnnotationView.SpanView"):
                self._anns[annViewName] = SpanView(annViewName)
            elif annView["type"].endswith("AnnotationView.RelationView"):
                self._anns[annViewName] = RelationView(annViewName)
            else:
                self._anns[annViewName] = AnnotationView(annViewName,annView["type"])
            self._anns[annViewName].reverse( annView )
