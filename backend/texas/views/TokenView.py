#!/usr/bin/python
#-*- coding: utf-8 -*-

from .AnnotationView import AnnotationView
from texas.annotations.TokenAnnotation import TokenAnnotation

class TokenView(AnnotationView):

    def __init__(self, pName:str):
        # automatically set type as "TokenView"
        super(TokenView, self).__init__(pName = pName, pType = "AnnotationView"+"."+"TokenView")

    def add(self, pTokenIndex:int, pLabel:str = ""):
        self.getAnnSet().add ( TokenAnnotation(pTokenIndex, pLabel) )
