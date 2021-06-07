#!/usr/bin/python
#-*- coding: utf-8 -*-

from .AnnotationView import AnnotationView

class RelationView(AnnotationView):

    def __init__(self, pName:str):
        # automatically set type as "RelationView"
        super(RelationView, self).__init__(pName = pName, pType = "AnnotationView"+"."+"RelationView")
