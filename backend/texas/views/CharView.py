#!/usr/bin/python
#-*- coding: utf-8 -*-

from .AnnotationView import AnnotationView

class CharView(AnnotationView):

    def __init__(self, pName:str):
        # automatically set type as "CharView"
        super(CharView, self).__init__(pName = pName, pType = "AnnotationView"+"."+"CharView")

