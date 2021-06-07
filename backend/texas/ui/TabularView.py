from texas.core.TextAnnotationSchema import TextAnnotationSchema

##############################################################################

class TabularRow():
	cells = []
	lastTokenUsed = 0
	def __init__(self,noTokens=0):
		# print (">>>>>>>>>>>>>>>>>>", noTokens)
		self.cells = []
		self.lastToken = 0
		for c in range(noTokens):
			self.cells.append(TabularCell())

class TabularCell():
	text = ""
	css = None
	colSpan = -1
	hidden = False
	border_left = False
	border_right = False
	def __init__(self):
		self.text = ""
		self.css = None
		self.colSpan = -1
		self.hidden = False
		self.border_left = False
		self.border_right = False

def markBorders(sent,viewLabel,start_token,final_token):
	for aLabel in sent["anns"]:
		ann = sent["anns"][aLabel]
		for rownum in range(len(ann["rows"])):
			if aLabel != viewLabel or rownum+1 < len(ann["rows"]):
				# print("aLabel",aLabel,rownum,start_token,final_token)
				row = ann["rows"][rownum]
				if not row.cells[start_token].text and (start_token == 0 or not row.cells[start_token-1].text): row.cells[start_token].border_left = True
				if final_token < len(row.cells):
					if False or not row.cells[final_token-1].text: row.cells[final_token].border_left = True
				else:
					if False or not row.cells[final_token-1].text: row.cells[final_token-1].border_right = True
		if aLabel == viewLabel: return

##############################################################################

class UITabularView():
    #_TAS = None
	#_text = ""
	#_token = []
	#_annLabels = []
	#_sentenceEndPositions = []
	#_sentence = []

    def __init__(self, TAS:TextAnnotationSchema = None):
        if not isinstance(TAS, TextAnnotationSchema):
            raise Exception("'TAS' parameter is required to be 'TextAnnotationSchema'")
        self._TAS = TAS
        self._text = self._TAS.getText()
        self._tokens = self._TAS.getTokenList()
        for t in self._TAS.getTokenInfo():
            if "index" in t:
                self._tokens[t["index"]] = t["label"]
        self._annLabels = []
        self._sentenceEndPositions = []
        self._sentences = []
        start_token = 0
        for s in self._TAS.getSentenceInfo():
            self._sentenceEndPositions.append(s["final_token"])
            final_token = s["final_token"]
            newSentence = {}
            newSentence["start_token"] = start_token
            newSentence["final_token"] = final_token
            newSentence["tokens"] = self._tokens[start_token:final_token]
            newSentence["anns"] = {}
            self._sentences.append(newSentence)
            start_token = final_token

    # Annotation Label (List)

    def getAnnLabels(self):
        return self._annLabels

    def addAnnLabel(self,viewLabel:str = None):
        if not viewLabel or viewLabel == "": return False
        if viewLabel in self.getAnnLabels(): return False
        self._annLabels.append(viewLabel)
        for s in self._sentences:
            s["anns"][viewLabel] = {"rowSpan":0,"rows":[],"lastRow":None}
        return True		

    def addTokenDef(self, viewLabel = '', tokenType = '', tokenLabel = '', tokenIndex = 0, labelCSS:bool = True):
        for sidx in range(len(self._sentences)):
            s = self._sentences[sidx]
            # print(">>>>>>>", "sentence", sidx, "tokens", len(s["tokens"]))
            if viewLabel in s["anns"]:
                sannlab = s["anns"][viewLabel]
                # -- OLD --
                # start = startToken - s["start_token"]
                # end = endToken - s["start_token"]
                token_index_rel = tokenIndex - s["start_token"]
                # -- OLD --
                # if start >=0 and end >= 0 and start < len(s["tokens"]) and end <= len(s["tokens"]):
                if not ( token_index_rel >= 0 and token_index_rel < len(s["tokens"]) ):
                    # DO NOT RIASE EXCEPTION AS IT IS ALSO LOOKING AT OTHER SENTENCES
                    # raise Exception("Invalid relative 'token_index' = '"+str(token_index_rel)+"' in sentence.");
                    None
                else:
                    # print(s["tokens"])
                    row = sannlab["lastRow"]
                    # if not row or row.lastTokenUsed > start:
                    if not row or row.lastTokenUsed > token_index_rel:
                        row = TabularRow(len(s["tokens"]))
                        sannlab["rows"].append(row)
                        sannlab["rowSpan"] += 1
                        sannlab["lastRow"] = row
                    row.cells[token_index_rel].text = tokenLabel
                    if labelCSS:
                        row.cells[token_index_rel].css = "w3-border w3-round-small "+viewLabel+"-"+tokenType
                    else:
                        row.cells[token_index_rel].css = "w3-border w3-round-small "+viewLabel
                    row.lastTokenUsed = token_index_rel
                    # if end-start>1: row.cells[start].colSpan = end-start
                    # for i in range(start+1,end):
                    #     row.cells[i].hidden = True
                    #     row.cells[i].text = row.cells[start].text
                    markBorders(s,viewLabel,token_index_rel,token_index_rel+1)
                    # print(">>>>>>>", "rows", len(sannlab["rows"]))
                    # print(">>>>>>>", "row", "cells", len(row.cells))
        return

    def addSpanDef(self, viewLabel = '', spanType = '', spanLabel = '', startToken = 0, finalToken = 0, labelCSS:bool = True):
        for sidx in range(len(self._sentences)):
            s = self._sentences[sidx]
            # print(">>>>>>>", "sentence", sidx, "tokens", len(s["tokens"]))
            if viewLabel in s["anns"]:
                sannlab = s["anns"][viewLabel]
                # -- OLD --
                # start = startToken - s["start_token"]
                # end = finalToken - s["start_token"]
                start_token_rel = startToken - s["start_token"]
                final_token_rel = finalToken - s["start_token"]
                # --
                if not (start_token_rel >=0 and final_token_rel >= 0 and start_token_rel < len(s["tokens"]) and final_token_rel <= len(s["tokens"]) and final_token_rel > start_token_rel ):
                    # DO NOT RIASE EXCEPTION AS IT IS ALSO LOOKING AT OTHER SENTENCES
                    # raise Exception("Invalid relative span ('start_token','final_token') = ('"+str(start_token_rel)+"','"+str(final_token_rel)+"') in sentence.");
                    None
                else:
                    # print(s["tokens"])
                    row = sannlab["lastRow"]
                    # if not row or row.lastTokenUsed > start:
                    if not row or row.lastTokenUsed > start_token_rel:
                        row = TabularRow(len(s["tokens"]))
                        sannlab["rows"].append(row)
                        sannlab["rowSpan"] += 1
                        sannlab["lastRow"] = row
                    row.cells[start_token_rel].text = spanLabel
                    if labelCSS:
                        row.cells[start_token_rel].css = "w3-border w3-round-small "+viewLabel+"-"+spanType
                    else:
                        row.cells[start_token_rel].css = "w3-border w3-round-small "+viewLabel
                    row.lastTokenUsed = final_token_rel
                    if final_token_rel-start_token_rel>1: row.cells[start_token_rel].colSpan = final_token_rel-start_token_rel
                    for i in range(start_token_rel+1,final_token_rel):
                        row.cells[i].hidden = True
                        row.cells[i].text = row.cells[start_token_rel].text
                    markBorders(s,viewLabel,start_token_rel,final_token_rel)
                    # print(">>>>>>>", "rows", len(sannlab["rows"]))
                    # print(">>>>>>>", "row", "cells", len(row.cells))
        return

	# def addSpanList(self, textAnnViews = {}, annViewName = '', annLabel = ''):
    def addTokenView(self, view, viewLabel:str, labelCSS:bool=True):
        if not self.addAnnLabel(viewLabel): return
        # if not "anns" in view: return
        anns = view.getAnnSet().getAnns()
        for c in anns:
            # (IGNORE) if "label" in c and "token_index" in c:
            tokenLabel = c.getLabel()
            tokenIndex = c.getTokenIndex()
            # self.addSpan(annLabel,tokenType, c["label"],c["start"],c["end"])
            # self.addLinkedSpan(annLabel, tokenType = 'EDL', tokenLabel = c["label"], startToken = c["start"], endToken = c["end"], annURL = "https://en.wikipedia.org/wiki/"+spanLink)
            if type(tokenLabel) is list:
                self.addTokenDef(viewLabel = viewLabel, tokenType = tokenLabel[0], tokenLabel = "|".join(tokenLabel), tokenIndex = tokenIndex, labelCSS=labelCSS )
            else:
                self.addTokenDef(viewLabel = viewLabel, tokenType = tokenLabel, tokenLabel = tokenLabel, tokenIndex = tokenIndex, labelCSS=labelCSS )
        # print(">>" , "addtokenLabelView" , annLabel)

    def addSpanView(self, view, viewLabel:str, labelCSS:bool=True):
        if not self.addAnnLabel(viewLabel): return
        anns = view.getAnnSet().getAnns()
        for c in anns:
            # (IGNORE) if "label" in c and "token_index" in c:
            spanLabel = c.getLabel()
            startToken = c.getStartToken()
            finalToken = c.getFinalToken()
            # self.addSpan(annLabel,tokenType, c["label"],c["start"],c["end"])
            # self.addLinkedSpan(annLabel, tokenType = 'EDL', tokenLabel = c["label"], startToken = c["start"], endToken = c["end"], annURL = "https://en.wikipedia.org/wiki/"+spanLink)
            self.addSpanDef(viewLabel = viewLabel, spanType = spanLabel, spanLabel = spanLabel, startToken = startToken, finalToken = finalToken, labelCSS=labelCSS)
        # print(">>" , "addtokenLabelView" , annLabel)
        
    def showView(self, viewName:str, viewLabel:str = None, labelCSS:bool=True):
        if viewLabel is None:
            viewLabel = viewName
        if not self._TAS.getViews().exists(viewName):
            raise Exception("'"+viewName+"' view not found");
        view = self._TAS.getViews().get(viewName)
        if view.getTexasClass() == "tx.view.TokenView":
            self.addTokenView(view, viewLabel, labelCSS)
        if view.getTexasClass() == "tx.view.SpanView":
            self.addSpanView(view, viewLabel, labelCSS)

    def HTML(self):
        html = ''
        # html += self._TAS.getText() + '\n'
        for s in self._sentences:
            html += '<div class="w3-panel w3-border w3-border-amber" style="overflow-x: auto;white-space: nowrap;">' + '\n'
            html += '&nbsp;' + '\n'
            html += ' <table class="w3-center w3-small">' + '\n'
            html += '  <tr>' + '\n'
            html += '   <td class="w3-border w3-right-align ANN-Label">Sentence&nbsp;&raquo;&nbsp;</td><td>&nbsp;</td>' + '\n'
            # html += '   <td>&nbsp;</td>' + '\n'
            for t in s["tokens"]:
                html += '   <td><b>'+ t +'</b></td>' + '\n'
            html += '  </tr>' + '\n'
            
            for annLabel in s["anns"]:
                # print(annLabel)
                ann = s["anns"][annLabel]
                for rownum in range(len(ann["rows"])):
                    # print(rownum)
                    row = ann["rows"][rownum]
                    html += '  <tr>' + '\n'
                    if False or rownum == 0:
                        html += '   <td class="w3-border w3-right-align ANN-Label"'
                        # if ann["rowSpan"] > 1: html += ' rowspan="'+str(ann["rowSpan"])+'"'
                        if ann["rowSpan"] > 1: html += ' rowspan="'+str(len(ann["rows"]))+'"'
                        html += '>'+annLabel+'&nbsp;&raquo;&nbsp;</td>' + '\n'
                    # html += '   <td>'+str(rownum)+'</td>\n'
                    # html += '   <td>'+str(len(row.cells))+'</td>\n'
                    html += '   <td>&nbsp;</td>' + '\n'
                    for cell in row.cells:
                        if not cell.hidden:
                            html += '   <td'
                            if cell.colSpan > 1: html += ' colspan="'+str(cell.colSpan)+'"'
                            # if cell.css: 
                            html += ' class="'+str(cell.css)
                            if not cell.text and cell.border_left: html += " w3-border-left"
                            if not cell.text and cell.border_right: html += " w3-border-right"
                            html += '"' 
                            html += '>'+cell.text+'</td>' + '\n'
                    #html += '   <td class="w3-border">'+str(rownum)+'</td>\n'

                    html += '  </tr>\n'

            html += ' </table>' + '\n'
            # 3.21 Need to add an extra line for better visualization
            html += '<br>'
            html += '</div>' + '\n'


        return html
