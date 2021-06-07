''' 
MultipackageCache class is used to handle load, read, add and write caches for different language models and packages
'''

import json
import hashlib
from datetime import datetime

################################ Cache Class ##################################
class MultipackageCache:

  def __init__(self, map):
    self.map = map


  def load(self, name):
    '''
    name(str): stanza, spacy, udpipe and trankit
    map: a dictionary which maps a language to its corresponding model
    '''
  
    try:
        with open('cache/cache_' + name + '.json') as file_obj:
            cache = json.load(file_obj)
        print("Load cache_" + name + " successfully from cache_stanza.json.")
    except:
        cache = {}
        for lang in self.map[name].keys():
            cache[lang] = {}
        print("Cannot find cache_" + name + ".json and an empty new nested dictionary for cache_" + name + " is created.")
    
    return cache


  def read(self, name, cache_dic, lang, string):
    hash_string = hashlib.sha1(string.encode()).hexdigest()
    if name == 'stanza':
      tokens = cache_dic[lang][hash_string]['tokens']
      end_pos = cache_dic[lang][hash_string]['end_pos']
      lemma = cache_dic[lang][hash_string]['lemma']
      pos = cache_dic[lang][hash_string]['pos']
      nlpWordsList = cache_dic[lang][hash_string]['nlpWordsList']
      hasCompoundWords = cache_dic[lang][hash_string]['hasCompoundWords']
      if 'count' not in cache_dic[lang][hash_string].keys():
          cache_dic[lang][hash_string]['count'] = 1
      else:
          cache_dic[lang][hash_string]['count'] += 1

      print("--------------The annotations is loaded from cache_" + name + "--------------")


      return tokens, end_pos, lemma, pos, nlpWordsList, hasCompoundWords, cache_dic
    
    else:
      tokens = cache_dic[lang][hash_string]['tokens']
      end_pos = cache_dic[lang][hash_string]['end_pos']
      lemma = cache_dic[lang][hash_string]['lemma']
      pos = cache_dic[lang][hash_string]['pos']
      if 'count' not in cache_dic[lang][hash_string].keys():
          cache_dic[lang][hash_string]['count'] =1
      else:
          cache_dic[lang][hash_string]['count'] += 1
      print("--------------The annotations is loaded from cache_" + name + "--------------")

      return tokens, end_pos, lemma, pos, cache_dic


  def add(self, name, cache_dic, lang, string, get_services): 
    '''
    get_services: funtion to produce annotations. Eg: get_services_stanza
    '''
    hash_string = hashlib.sha1(string.encode()).hexdigest()
    if name == 'stanza':
      model = self.map[name][lang]
      docs = model(string)
      tokens, end_pos, lemma, pos, nlpWordsList, hasCompoundWords = get_services(docs)
      cache_dic[lang][hash_string] = {}
      cache_dic[lang][hash_string]['text'] = string
      cache_dic[lang][hash_string]['tokens'] = tokens
      cache_dic[lang][hash_string]['end_pos'] = end_pos
      cache_dic[lang][hash_string]['lemma'] = lemma
      cache_dic[lang][hash_string]['pos'] = pos
      cache_dic[lang][hash_string]['nlpWordsList'] = nlpWordsList
      cache_dic[lang][hash_string]['hasCompoundWords'] = hasCompoundWords
      cache_dic[lang][hash_string]['count'] = 1
      print("--------------The annotations is not included in cache_" + name + "--------------")

      return tokens, end_pos, lemma, pos, nlpWordsList, hasCompoundWords, cache_dic

    else:
      model = self.map[name][lang]
      docs = model(string)
      tokens, end_pos, lemma, pos = get_services(docs)
      cache_dic[lang][hash_string] = {}
      cache_dic[lang][hash_string]['text'] = string
      cache_dic[lang][hash_string]['tokens'] = tokens
      cache_dic[lang][hash_string]['end_pos'] = end_pos
      cache_dic[lang][hash_string]['lemma'] = lemma
      cache_dic[lang][hash_string]['pos'] = pos
      cache_dic[lang][hash_string]['count'] = 1
      print("--------------The annotations is not included in cache_" + name + "--------------")

      return tokens, end_pos, lemma, pos, cache_dic

  def count(self, cache_dic):
    '''
    This function is used to count the number of sentence in a cache
    '''  
    num = sum([len(cache_dic[key]) for key in cache_dic.keys()])

    return num


  def write(self, cache_dic, name):

    json_dic = json.dumps(cache_dic, indent=4)
    with open('cache/cache_'+ name + '_'+ datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.json', 'w') as json_file:
        json_file.write(json_dic)      

