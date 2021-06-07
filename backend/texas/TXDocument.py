#!/usr/bin/python
#-*- coding: utf-8 -*-

from .core.TextAnnotationSchema import TextAnnotationSchema

class Document(TextAnnotationSchema):

    def __init__(self, pText : str, pLang : str = None, pType : str = "document"):
        """ Set TEXAS type as 'document' """
        super(Document, self).__init__(pText = pText, pLang = pLang, pType = pType)
        self.setTexasClass("tx.Document")

