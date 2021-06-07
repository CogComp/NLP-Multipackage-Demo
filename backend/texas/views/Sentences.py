#!/usr/bin/python
#-*- coding: utf-8 -*-

from .SpanView import SpanView

class Sentences(SpanView):
    def __init__(self):
        # automatically name "SENTENCES" and set type as "SpanView" 
        super(Sentences, self).__init__(pName = "SENTENCES")

