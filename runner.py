#!/usr/bin/python
# coding: utf-8

from responsehandler import ResponseHandler
from termparser import TermParser
from webdriver import Driver
import copy

BATCH_SIZE = 10

def harvest_html(driver, term):
  driver.search(term)
  return driver.page_source()

def export_batch(batch_no, terms_d, items):
  # Export results
  with open('./output/morphs-res-'+str(batch_no)+'.csv', 'w') as f:
    for term in items:
      payload = items.get(term)
      for morph_data in payload.get('morphs'):

        morph = morph_data.get('morph')
        meaning = payload.get('meaning')
        type = morph_data.get('type')
        res = morph_data.get('res')

        if not morph: morph = "n/a"
        if not meaning: meaning = "n/a"
        if not type: type = "n/a"
        if not res: res = "n/a"

        f.write((
            term + '\t' + 
            meaning + '\t' +
            morph + '\t' +
            type + '\t' +
            res + '\n'
            ).encode('utf-8'))
  print 'Done writing: batch', batch_no

# Run Driver 
driver = Driver("http://s.weibo.com", "searchInp_form", "searchBtn")

# Populate terms
termparser = TermParser("gmh-lex-glossary.html")
terms = termparser.get_terms()

# Crawl for term results
morphs = {}
i = 0
for term in terms:
  i = i + 1
  print i
  morph_list = [] 
  for morph_data in terms.get(term).get("morphs"):

    html = harvest_html(driver, morph_data.get("morph"))
    handler = ResponseHandler(html)
    morph_data.update({"res": handler.response_type()})
    morph_list.append(morph_data)

  morphs.update({term: {"term": term, "morphs": morph_list}})
  export_batch(i, terms, morphs)

driver.quit()
