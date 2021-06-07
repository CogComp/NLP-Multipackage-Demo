#!/usr/bin/python
#-*- coding: utf-8 -*-

from .CharView import CharView
from texas.annotations.CharAnnotation import CharAnnotation

class Tokens(CharView):

    def __init__(self):
        # automatically name "TOKENS" and set type as "CharView" 
        super(Tokens, self).__init__(pName = "TOKENS")

    def add(self,pStartChar:int, pEndChar:int, pLabel:str = "", pIndex = None):
        self.getAnnSet().add ( CharAnnotation(pStartChar, pEndChar, pLabel, pIndex) )
        