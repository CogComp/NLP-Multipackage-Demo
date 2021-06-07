#!/usr/bin/python
#-*- coding: utf-8 -*-

from .core.TextAnnotationSchema import TextAnnotationSchema

class Corpus(TextAnnotationSchema):

    def __init__(self, pLang : str = None):
        """ Set TEXAS type as 'corpus' and text = '' """
        super(Corpus, self).__init__(pText = None, pLang = pLang, pType = "corpus")
        self.setTexasClass("tx.Corpus")
