#!/usr/bin/python
#-*- coding: utf-8 -*-

import json

class Metadata:
    def __init__(self):
        self._meta = None

    def set(self, pAttribute, pValue):
        d = {pAttribute : pValue}
        s = json.dumps(d)
        if self._meta is None:
            self._meta = {}
        self._meta[pAttribute] = pValue

    def get(self, pAttribute):
        if self._meta is None:
            return None
        if pAttribute in self._meta:
            return self._meta[pAttribute]
        else:
            return None

    def has(self, pAttribute):
        if self._meta is None:
            return False
        if pAttribute in self._meta:
            return True
        else:
            return False

    def size(self):
        if self._meta is None:
            return 0
        else:
            return len(self._meta)

    def TAS(self):
        d = {}
        if not self._meta is None:
            for attr in self._meta:
                # there is a space here to validate serializable objects
                d[attr] = self._meta[attr]
        return d

    def reverse(self, jss: dict):
        self._meta = {}
        if jss is None:
            return
        if not type(jss) is dict:
            raise Exception("Metadata reverse 'jss' parameter is required to be 'dict'");
        for attr in jss:
            self._meta[attr] = jss[attr]
