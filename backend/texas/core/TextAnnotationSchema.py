#!/usr/bin/python
#-*- coding: utf-8 -*-

from .Language import Language
from .Timestamp import Timestamp
from .Metadata import Metadata
from .Bits import Bits
from texas.view.AnnotationViewSet import AnnotationViewSet
from texas.view.Tokens import Tokens
from texas.view.TokenView import TokenView
from texas.view.SpanView import SpanView
from texas.view.RelationView import RelationView
from texas.view.Sentences import Sentences

def reverse(jss: dict):
    if not type(jss) is dict:
        raise Exception("TextAnnotationSchema import JSON-Serializable-Schema 'jss' parameter type is required to be 'dict'");
    jssType = None
    jssText = None
    jssLang = None
    if "type" in jss:
        jssType = jss["type"]
    if "text" in jss:
        jssText = jss["text"]
    if "lang" in jss:
        jssLang = jss["lang"]
    newTX = TextAnnotationSchema(pText = jssText, pLang = jssLang, pType = jssType)
    for attr in jss:
        if attr in ["type","lang","type"]:
            None
        elif attr == "info":
            None # ignore INFO on reversing (output only)
        elif attr == "date":
            newTX.getDate().setTimestamp(jss[attr])
        elif attr == "meta":
            newTX.meta().reverse(jss[attr])
        elif attr == "view":
            newTX.getViews().reverse(jss[attr])
        elif attr == "bits":
            # newTX.bits().reverse(jss[attr])
            jss2 = jss[attr]
            if not type(jss2) is list:
                raise Exception("Bits reverse JSON-Serializable-Schema 'jss' parameter type is required to be 'list'");
            newTX.bits()._bits = []
            for bit in jss2:
                if not type(bit) is dict:
                    raise Exception("Bit reverse component type is required to be 'dict'");
                newTX.bits()._bits.append( reverse(bit) )
        elif attr == "texas.class":
            newTX.setTexasClass(jss[attr])
    return newTX
    
class TextAnnotationSchema():
    def __init__(self, pText : str, pLang : str, pType : str):
        if not (pText is None or type(pText) is str):
            raise Exception("TextAnnotationSchema 'pText' parameter type is required to be 'str'");
        if not (pLang is None or type(pLang) is str):
            raise Exception("TextAnnotationSchema 'pLang' parameter type is required to be 'str' when given");
        if not type(pType) is str:
            raise Exception("TextAnnotationSchema 'pType' parameter type is required to be 'str'");
        self._type = pType
        self._text = pText
        self._lang = Language(pLang = pLang)
        self._date = Timestamp()
        self._meta = Metadata()
        self._bits = Bits()
        self._view = AnnotationViewSet()
        self.setTexasClass("tx.core.TextAnnotationSchema")
        
    # def jss__(self, jss, ignore):
    #     pass

    def getTexasClass(self) -> str:
        return self._txClass
    def txClass(self) -> str:
        return self._txClass
    def setTexasClass(self,pClass) -> str:
        if not (type(pClass) is str):
            raise Exception("TextAnnotationSchema 'pClass' parameter type is required to be 'str'");
        self._txClass = pClass

    def getType(self) -> str:
        return self._type
    def type(self) -> str:
        return self._type

    def getText(self) -> str:
        return self._text
    def text(self) -> str:
        return self._text

    def getLang(self):
        return self._lang
    def lang(self):
        return self._lang

    def getDate(self):
        return self._date
    def date(self):
        return self._date

    def getMeta(self):
        return self._meta
    def meta(self):
        return self._meta

    def getAnnViewSet(self):
        return self._view
    def AnnViewSet(self):
        return self._view
    def getViews(self):
        return self._view
    def views(self):
        return self._view

    def getBits(self):
        return self._bits
    def bits(self):
        return self._bits

    #
    # TOKEN specific methods
    #
    def getTokenList(self):
        tokenList = []
        if not self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' does NOT exist");
        tokensView = self.getAnnViewSet().get("TOKENS")
        for ann in tokensView.getAnnSet().getAnns():
            tokenList.append( ann.getLabel() )
        return tokenList

    def getTokenInfo(self):
        tokenList = []
        if not self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' does NOT exist");
        tokensView = self.getAnnViewSet().get("TOKENS")
        for ann in tokensView.getAnnSet().getAnns():
            # tokenList.append( { "label":ann.getLabel(), "start_char": ann.getStartChar(), "final_char": ann.getFinalChar() } )
            tokenList.append( ann.TAS() )
        return tokenList

    def setTokenList(self, pTokenList:list, indexed=False):
        if not type(pTokenList) is list:
            raise Exception("TextAnnotationSchema 'pTokenList' parameter type is required to be 'list'");
        if self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' already exists");
        tokenList = []
        lastEndCharPos = 0
        for tok in pTokenList:
            tokenEntry = {"listToken":None, "textToken":None, "startCharPos": -1, "endCharPos": -1}

            # (a) string only
            # e.g. ["a","b","c", ...]

            if type(tok) is str:
                tokenEntry["listToken"] = tok
                charPos = self._text[lastEndCharPos:].find(tokenEntry["listToken"])
                if charPos > -1:
                    tokenEntry["startCharPos"] = charPos+lastEndCharPos
                    tokenEntry["endCharPos"] = tokenEntry["startCharPos"] + len(tokenEntry["listToken"])
                    tokenEntry["textToken"] = tokenEntry["listToken"]
            
            # (b.1) pair (start,end) char positions only
            # e.g. [ [0,10], [10,15], ...]

            elif type(tok) is list and len(tok) == 2 and type(tok[0]) is int and type(tok[1]) is int:
                tokenEntry["startCharPos"] = tok[0]
                tokenEntry["endCharPos"] = tok[1]
                tokenEntry["textToken"] = self._text[tokenEntry["startCharPos"]:tokenEntry["endCharPos"]]
                tokenEntry["listToken"] = tokenEntry["textToken"]

            # (b.2) [end] <list> char positions only
            # e.g. [ [0], [10], [15], ...]

            elif type(tok) is list and len(tok) == 1 and type(tok[0]) is int:
                tokenEntry["endCharPos"] = tok[0]
                stripToken = self._text[lastEndCharPos:tokenEntry["endCharPos"]].strip()
                charPos = self._text[lastEndCharPos:].find(stripToken)
                if charPos > -1 and charPos < tokenEntry["endCharPos"]:
                    tokenEntry["startCharPos"] = charPos + lastEndCharPos
                    tokenEntry["endCharPos"] = tokenEntry["startCharPos"] + len(stripToken)
                    tokenEntry["textToken"] = self._text[tokenEntry["startCharPos"]:tokenEntry["endCharPos"]]
                    tokenEntry["listToken"] = tokenEntry["textToken"]

            # (b.3) end <int> char positions only
            # e.g. [0,10,15]

            elif type(tok) is int:
                tokenEntry["endCharPos"] = tok
                stripToken = self._text[lastEndCharPos:tokenEntry["endCharPos"]].strip()
                charPos = self._text[lastEndCharPos:].find(stripToken)
                if charPos > -1 and charPos < tokenEntry["endCharPos"]:
                    tokenEntry["startCharPos"] = charPos + lastEndCharPos
                    tokenEntry["endCharPos"] = tokenEntry["startCharPos"] + len(stripToken)
                    tokenEntry["textToken"] = self._text[tokenEntry["startCharPos"]:tokenEntry["endCharPos"]]
                    tokenEntry["listToken"] = tokenEntry["textToken"]
            
            # (c) string,start[,end] triple - end is optional
            # e.g. [ ["a",0,10], ["b",10,15], ["c", ]

            elif type(tok) is list and len(tok) in [2,3] and type(tok[0]) is str and type(tok[1]) is int and ( len(tok) == 3 and type(tok[2]) is int ):
                tokenEntry["listToken"] = tok[0]
                tokenEntry["startCharPos"] = tok[1]
                if len(tok) == 3:
                    tokenEntry["endCharPos"] = tok[2]
                else:
                    tokenEntry["endCharPos"] = tokenEntry["endCharPos"] + len( tokenEntry["listToken"] )
                tokenEntry["textToken"] = self._text[tokenEntry["startCharPos"]:tokenEntry["endCharPos"]]

            # validate tokenEntry 
            
            if tokenEntry["textToken"] is None or tokenEntry["listToken"] is None or len(tokenEntry["textToken"]) == 0 or len(tokenEntry["listToken"]) == 0:
                raise Exception("Not possible to identify 'token' for pTokenList entry '"+str(tokenEntry)+"'");
            if tokenEntry["startCharPos"] == -1:
                raise Exception("Not possible to identify 'startCharPos' for pTokenList entry '"+str(tok)+"'");
            if tokenEntry["endCharPos"] == -1:
                raise Exception("Not possible to identify 'endCharPos' for pTokenList entry '"+str(tok)+"'");
            if tokenEntry["endCharPos"] < lastEndCharPos:
                raise Exception("'endCharPos' is before previous token for pTokenList entry '"+str(tok)+"'");
            
            # add tokenEntry to tokenList and update(increase) lastEndCharPos
            tokenList.append(tokenEntry)
            lastEndCharPos = tokenEntry["endCharPos"]
            
        tokensView = Tokens()
        tokenIndex = -1
        for token in tokenList:
            if indexed:
                tokenIndex += 1
                tokensView.add ( token["startCharPos"] , token["endCharPos"] , token["textToken"] , tokenIndex)
            else:
                tokensView.add ( token["startCharPos"] , token["endCharPos"] , token["textToken"] )
        self.getAnnViewSet().add(tokensView)
        return
    
    #
    # SENTENCE specific methods
    #

    def setSentenceList(self, pSentenceList:list):
        if not type(pSentenceList) is list:
            raise Exception("TextAnnotationSchema 'pSentenceList' parameter type is required to be 'list'");
        if self.getAnnViewSet().exists("SENTENCES"):
            raise Exception("AnnotationView 'SENTENCES' already exists");
        if not self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' does NOT exist yet");
        sentenceList = []
        lastFinalToken = 0
        for sent in pSentenceList:
            sentEntry = {"startToken": -1, "finalToken": -1}

            # (b.3) end <int> token indexes only
            # e.g. [0,10,15,...]
            if type(sent) is int:
                sentEntry["finalToken"] = sent
                sentEntry["startToken"] = lastFinalToken

            # validate sentEntry 
            if sentEntry["startToken"] == -1:
                raise Exception("Not possible to identify 'startToken' for pSentenceList entry '"+str(sent)+"'");
            if sentEntry["finalToken"] == -1:
                raise Exception("Not possible to identify 'finalToken' for pSentenceList entry '"+str(sent)+"'");
            if sentEntry["finalToken"] <= sentEntry["startToken"]:
                raise Exception("'finalToken' needs to be > than 'startToken' for pSentenceList entry '"+str(sent)+"'");
            
            # add sentEntry to tokenList and update(increase) lastEndCharPos
            sentenceList.append(sentEntry)
            lastFinalToken = sentEntry["finalToken"]

        sentView = Sentences()
        for sent in sentenceList:
            sentView.add ( sent["startToken"] , sent["finalToken"] )
        self.getAnnViewSet().add(sentView)
        return

    def getSentenceInfo(self):
        tokenInfo = self.getTokenInfo()
        sentList = []
        if not self.getAnnViewSet().exists("SENTENCES"):
            raise Exception("AnnotationView 'SENTENCES' does NOT exist");
        sentView = self.getAnnViewSet().get("SENTENCES")
        for ann in sentView.getAnnSet().getAnns():
            d = ann.TAS()
            startChar = tokenInfo[ann.getStartToken()]["start_char"]
            finalChar = tokenInfo[ann.getFinalToken()-1]["final_char"]
            d["start_char"] = startChar
            d["final_char"] = finalChar
            d["sentence"] = self.getText()[startChar:finalChar]
            # sentList.append( { "sentence": self.getText()[startChar:finalChar], "label": ann.getLabel(), "start_token": ann.getStartToken(), "final_token": ann.getFinalToken(), "start_char": startChar, "final_char": finalChar } )
            sentList.append( d )
        return sentList

    #
    # TOKEN specific methods
    #
    def addTokenView(self, pViewName:str , pLabelList:list, pType:str = None):
        if not type(pViewName) is str:
            raise Exception("addTokenView 'pViewName' parameter type is required to be 'str'");
        if not type(pLabelList) is list:
            raise Exception("addTokenView 'pLabelList' parameter type is required to be 'list'");
        if self.getAnnViewSet().exists(pViewName):
            raise Exception("AnnotationView '"+pViewName+"' already exists");
        if not self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' does NOT exist yet");
        tokenList = self.getTokenList()
        if len(pLabelList) != len(tokenList):
            raise Exception("Size of 'pLabelList' ("+str(len(pLabelList))+") does NOT match number of tokens ("+str(len(tokenList))+")");
        
        annList = []
        tokenIndex = -1
        for labelEntry in pLabelList:
            tokenEntry = {"tokenIndex": -1, "label": None}
            tokenIndex += 1

            if labelEntry is not None:

                # <str> labels only
                if type(labelEntry) is str or type(labelEntry) is list:
                    tokenEntry["tokenIndex"] = tokenIndex
                    tokenEntry["label"] = labelEntry

                # validate tokenEntry 
                if tokenEntry["tokenIndex"] == -1:
                    raise Exception("Not possible to identify 'tokenIndex' for pLabelList entry '"+str(labelEntry)+"'");
                if tokenEntry["label"] is None:
                    raise Exception("Not possible to identify 'label' for pLabelList entry '"+str(labelEntry)+"'");
            
                # add tokenEntry to tokenList and update(increase) lastEndCharPos
                annList.append(tokenEntry)

        newTokenView = TokenView(pViewName, pType = pType)
        for ann in annList:
            newTokenView.add ( pTokenIndex = ann["tokenIndex"] , pLabel = ann["label"] )
        self.getAnnViewSet().add(newTokenView)
        return

    #
    # SPAN specific methods
    #
    def addSpanAnns(self, pViewName:str , pSpanList:list):
        if not type(pViewName) is str:
            raise Exception("addSpanAnns 'pViewName' parameter type is required to be 'str'");
        if type(pSpanList) is dict:
            pSpanList = [pSpanList]
        if not type(pSpanList) is list:
            raise Exception("addSpanAnns 'pSpanList' parameter type is required to be 'list'");
        if not self.getAnnViewSet().exists(pViewName):
            raise Exception("AnnotationView '"+pViewName+"' does NOT exists");
        if not self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' does NOT exist yet");
        tokenList = self.getTokenList()
    
        theSpanView = self.getAnnViewSet().get(pViewName)
        if not isinstance(theSpanView,SpanView):
            raise Exception("AnnotationView '"+pViewName+"' is required to be 'SpanView'");
        
        annList = []
        for labelEntry in pSpanList:
            spanEntry = {"start_token": -1, "final_token": -1, "label": None}

            # <dict> 
            if type(labelEntry) is dict:
                if "label" in labelEntry:
                    spanEntry["label"] = labelEntry["label"]
                if "start_token" in labelEntry:
                    spanEntry["start_token"] = labelEntry["start_token"]
                if "final_token" in labelEntry:
                    spanEntry["final_token"] = labelEntry["final_token"]
                if "token_index" in labelEntry:
                    spanEntry["start_token"] = labelEntry["token_index"]
                    spanEntry["final_token"] = labelEntry["token_index"]+1

            # <list> 
            if type(labelEntry) is list:
                if len(labelEntry) > 0: 
                    if type(labelEntry[0]) is not str:
                        raise Exception("'label' not found in labelEntry[0] for pSpanList entry '"+str(labelEntry)+"'")
                    else:
                        spanEntry["label"] = labelEntry[0]
                if len(labelEntry) > 1:
                    if type(labelEntry[1]) is not int:
                        raise Exception("'start_index' not found in labelEntry[1] for pSpanList entry '"+str(labelEntry)+"'")
                    else:
                        spanEntry["start_token"] = labelEntry[1]
                        spanEntry["final_token"] = labelEntry[1]+1
                if len(labelEntry) > 2:
                    if type(labelEntry[2]) is not int:
                        raise Exception("'final_index' not found in labelEntry[2] for pSpanList entry '"+str(labelEntry)+"'")
                    else:
                        spanEntry["final_token"] = labelEntry[2]
 
            # validate spanEntry 
            if spanEntry["start_token"] == -1:
                raise Exception("Not possible to identify 'start_token' for pSpanList entry '"+str(labelEntry)+"'");
            if spanEntry["start_token"] < 0 or spanEntry["start_token"] > len(tokenList)-1:
                raise Exception("Invalid 'start_token' index for pSpanList entry '"+str(labelEntry)+"' valid range ("+str(0)+","+str(len(tokenList)-1)+")" )
            if spanEntry["final_token"] == -1:
                raise Exception("Not possible to identify 'final_token' for pSpanList entry '"+str(labelEntry)+"'");
            if spanEntry["final_token"] < 1 or spanEntry["final_token"] > len(tokenList):
                raise Exception("Invalid 'final_token' index for pSpanList entry '"+str(labelEntry)+"' valid range ("+str(1)+","+str(len(tokenList))+")" )
            if spanEntry["label"] is None:
                raise Exception("Not possible to identify 'label' for pSpanList entry '"+str(labelEntry)+"'")
            
            # add spanEntry to tokenList and update(increase) lastEndCharPos
            annList.append(spanEntry)

        #newSpanView = SpanView(pViewName)
        for ann in annList:
            theSpanView.add ( pStartToken = ann["start_token"] , pFinalToken = ann["final_token"] , pLabel = ann["label"], pSpan = " ".join(tokenList[ann["start_token"]:ann["final_token"]]) )
        #self.getAnnViewSet().add(newSpanView)
        return
    

    def addSpanView(self, pViewName:str , pSpanList:list = None, pType:str = None):
        if not type(pViewName) is str:
            raise Exception("addSpanView 'pViewName' parameter type is required to be 'str'");
        #if not pSpanList is None and not type(pSpanList) is list:
        #    raise Exception("addSpanView 'pSpanList' parameter type is required to be 'list'");
        if self.getAnnViewSet().exists(pViewName):
            raise Exception("AnnotationView '"+pViewName+"' already exists");
        if not self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' does NOT exist yet");
        tokenList = self.getTokenList()

        newSpanView = SpanView(pViewName, pType = pType)
        self.getAnnViewSet().add(newSpanView)

        if not pSpanList is None:
            self.addSpanAnns(pViewName , pSpanList)
        return

    #
    # RELATION specific methods
    #
    def addRelationAnns(self, pViewName:str , pRootSpan:dict):
        None

    def addRelationRoot(self, pViewName:str , pRelationName:str, pRootType:str, pRootSpan:dict):
        if not type(pViewName) is str:
            raise Exception("addRelationRoot 'pViewName' parameter type is required to be 'str'");
        if not type(pViewName) is str:
            raise Exception("addRelationRoot 'pRelationName' parameter type is required to be 'str'");
        if not type(pViewName) is str:
            raise Exception("addRelationRoot 'pRootType' parameter type is required to be 'str'");
        if not type(pRootSpan) is dict:
            raise Exception("addRelationRoot 'pRootSpan' parameter type is required to be 'dict'");
        if not self.getAnnViewSet().exists(pViewName):
            raise Exception("AnnotationView '"+pViewName+"' does NOT exists");
        if not self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' does NOT exist yet");
        tokenList = self.getTokenList()
    
        theRelationView = self.getAnnViewSet().get(pViewName)
        if not isinstance(theRelationView,RelationView):
            raise Exception("AnnotationView '"+pViewName+"' is required to be 'RelationView'");
            
        annList = []
        
        labelEntry = pRootSpan
        spanEntry = {"start_token": -1, "final_token": -1, "label": None}

        # <dict> 
        if type(labelEntry) is dict:
            if "label" in labelEntry:
                spanEntry["label"] = labelEntry["label"]
            if "start_token" in labelEntry:
                spanEntry["start_token"] = labelEntry["start_token"]
            if "final_token" in labelEntry:
                spanEntry["final_token"] = labelEntry["final_token"]
            if "token_index" in labelEntry:
                spanEntry["start_token"] = labelEntry["token_index"]
                spanEntry["final_token"] = labelEntry["token_index"]+1

        # validate spanEntry 
        if spanEntry["start_token"] == -1:
            raise Exception("Not possible to identify 'start_token' for pSpanList entry '"+str(labelEntry)+"'");
        if spanEntry["start_token"] < 0 or spanEntry["start_token"] > len(tokenList)-1:
            raise Exception("Invalid 'start_token' index for pSpanList entry '"+str(labelEntry)+"' valid range ("+str(0)+","+str(len(tokenList)-1)+")" )
        if spanEntry["final_token"] == -1:
            raise Exception("Not possible to identify 'final_token' for pSpanList entry '"+str(labelEntry)+"'");
        if spanEntry["final_token"] < 1 or spanEntry["final_token"] > len(tokenList):
            raise Exception("Invalid 'final_token' index for pSpanList entry '"+str(labelEntry)+"' valid range ("+str(1)+","+str(len(tokenList))+")" )
        if spanEntry["label"] is None:
            raise Exception("Not possible to identify 'label' for pSpanList entry '"+str(labelEntry)+"'")
        
        # add spanEntry to tokenList and update(increase) lastEndCharPos
        annList.append(spanEntry)

        #newSpanView = SpanView(pViewName)
        for ann in annList:
            theRelationView.add ( pRelationName = pRelationName, pRootType = pRootType, pRootStartToken = ann["start_token"] , pRootFinalToken = ann["final_token"] , pRootLabel = ann["label"], pRootSpan = " ".join(tokenList[ann["start_token"]:ann["final_token"]]) )
        #self.getAnnViewSet().add(newSpanView)
        return
        
        
    def addRelationView(self, pViewName:str, pType:str = None): # , pRootSpan:dict = None):
        if not type(pViewName) is str:
            raise Exception("addRelationView 'pViewName' parameter type is required to be 'str'");
        #if not pRootSpan is None and not type(pRootSpan) is dict:
        #    raise Exception("addRelationView 'pRootSpan' parameter type is required to be 'dict'");
        if self.getAnnViewSet().exists(pViewName):
            raise Exception("AnnotationView '"+pViewName+"' already exists");
        if not self.getAnnViewSet().exists("TOKENS"):
            raise Exception("AnnotationView 'TOKENS' does NOT exist yet");
        tokenList = self.getTokenList()

        newRelationView = RelationView(pViewName, pType = pType)
        self.getAnnViewSet().add(newRelationView)

        #if not pRootSpan is None:
        #    self.addRelationRoot(pViewName , pRootSpan)
        return

    #
    # jss >> getSchema
    #

    def TAS(self):
        d = {}
        d["type"] = self.getType()
        if not self.getText() is None:
            d["text"] = self.getText()
        if not self.getLang().getAlpha2() is None:
            d["lang"] = self.getLang().getAlpha2()
        if not self.getDate().getTimestamp() is None:
            d["date"] = self.getDate().getTimestamp()
        if self.getMeta() is not None and self.getMeta().size() > 0:
            d["meta"] = self.getMeta().TAS()
        # info (output only)
        if self.getAnnViewSet().exists("TOKENS"):
            ti = self.getTokenInfo()
            if len(ti) > 0:
                d["info"] = {}
                d["info"]["tokens"] = ti
                if self.getAnnViewSet().exists("SENTENCES"):
                    si = self.getSentenceInfo()
                    if len(si) > 0:
                        d["info"]["sentences"] = si
        if self.getBits() is not None and self.getBits().size() > 0:
            d["bits"] = self.getBits().TAS()
        if self.getViews() is not None and self.getViews().size() > 0:
            d["view"] = self.getViews().TAS()
        d["texas.class"] = self._txClass
        return d
