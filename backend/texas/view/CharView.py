#!/usr/bin/python
#-*- coding: utf-8 -*-

from .AnnotationView import AnnotationView

class CharView(AnnotationView):

    def __init__(self, pName : str, pType : str = None):
        # automatically set type as "CharView"
        super(CharView, self).__init__(pName = pName, pType = pType) # pType = "AnnotationView"+"."+"CharView")
        self.setTexasClass("tx.view.CharView")

