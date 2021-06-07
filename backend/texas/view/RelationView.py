#!/usr/bin/python
#-*- coding: utf-8 -*-

from .AnnotationView import AnnotationView
from texas.anns.RelationAnnotation import RelationAnnotation

class RelationView(AnnotationView):

    def __init__(self, pName : str, pType : str = None):
        # automatically set type as "RelationView"
        super(RelationView, self).__init__(pName = pName, pType = pType) # pType = "AnnotationView"+"."+"RelationView")
        self.setTexasClass("tx.view.RelationView")

    def add(self,pRelationName:str, pRootType:str, pRootStartToken:int, pRootFinalToken:int, pRootLabel:str = "", pRootSpan:str = None):
        # MISSING: validate duplicated relation names
        print("adding...")
        self.getAnnSet().add ( RelationAnnotation(pRelationName, pRootType, pRootStartToken, pRootFinalToken, pRootLabel, pRootSpan) )
