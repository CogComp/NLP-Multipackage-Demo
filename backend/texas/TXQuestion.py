#!/usr/bin/python
#-*- coding: utf-8 -*-

from .core.TextAnnotationSchema import TextAnnotationSchema

class Question(TextAnnotationSchema):

    def __init__(self, pText : str, pLang : str = None):
        """ Set TEXAS type as 'question' """
        super(Question, self).__init__(pText = pText, pLang = pLang, pType = "question")

