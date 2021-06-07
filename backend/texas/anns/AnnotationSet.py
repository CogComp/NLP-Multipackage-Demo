#!/usr/bin/python
#-*- coding: utf-8 -*-

from .Annotation import Annotation
from .CharAnnotation import CharAnnotation
from .TokenAnnotation import TokenAnnotation
from .SpanAnnotation import SpanAnnotation
from .RelationAnnotation import RelationAnnotation

class AnnotationSet:
    def __init__(self):
        self._anns = []

    def add(self, pAnn:Annotation):
        if not isinstance(pAnn, Annotation):
           raise Exception("AnnotationSet 'pAnn' parameter class is required to be 'Annotation'");
        self._anns.append(pAnn)
        
    def getAnns(self):
        return self._anns
    def anns(self):
        return self._anns

    def size(self):
        return len(self._anns)
        
    def TAS(self):
        d = []
        for annotation in self.getAnns():
            d.append( annotation.TAS() )
        return d
        
    def reverse(self, jss: list):
        if jss is None:
            return
        if not type(jss) is list:
            raise Exception("AnnotationSet reverse 'jss' parameter is required to be 'list'");
        for ann in jss:
            if not type(ann) is dict:
                raise Exception("Annotation in reverse 'anns' list is required to be 'dict'");
            if not "type" in ann:
                raise Exception("Missing 'type' attribute in Annotation during reverse");
            if ann["type"] == "char":
                if not "index" in ann:
                    ann["index"] = None
                if not "label" in ann:
                    raise Exception("Missing 'label' attribute in CharAnnotation during reverse");
                if not "start_char" in ann:
                    raise Exception("Missing 'start_char' attribute in CharAnnotation during reverse");
                if not "final_char" in ann:
                    raise Exception("Missing 'final_char' attribute in CharAnnotation during reverse");
                self.getAnns().append (CharAnnotation(pStartChar = ann["start_char"], pFinalChar = ann["final_char"], pLabel = ann["label"], pIndex = ann["index"]))
            if ann["type"] == "token":
                if not "token_index" in ann:
                    raise Exception("Missing 'token_index' attribute in CharAnnotation during reverse");
                if not "label" in ann:
                    raise Exception("Missing 'label' attribute in CharAnnotation during reverse");
                self.getAnns().append (TokenAnnotation(pTokenIndex = ann["token_index"], pLabel = ann["label"]))
            if ann["type"] == "span":
                if not "start_token" in ann:
                    raise Exception("Missing 'start_token' attribute in CharAnnotation during reverse");
                if not "final_token" in ann:
                    raise Exception("Missing 'final_token' attribute in CharAnnotation during reverse");
                if not "label" in ann:
                    raise Exception("Missing 'label' attribute in CharAnnotation during reverse");
                annSpan = None
                if "span" in ann:
                    annSpan = ann["span"]
                self.getAnns().append (SpanAnnotation(pStartToken = ann["start_token"], pFinalToken = ann["final_token"], pLabel = ann["label"], pSpan=annSpan))

            
        '''
        self._anns = {}
        if jss is None:
            return
        if not type(jss) is dict:
            raise Exception("AnnotationViewSet reverse 'jss' parameter is required to be 'dict'");
        for attr in jss:
            self._anns[attr] = AnnotationView.reverse(jss[attr])
        '''