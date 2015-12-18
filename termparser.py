#!/usr/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import re
from requests.utils import quote

placeholder = {
    "apple":
    {
      "term":"apple", 
      "morphs": [
        {
        "morph":"apple", 
        "type": "og",
        "res": "None"
        }, 
        {
        "morph":"oooloolalalack i", 
        "type": "py",
        "res": "None"
        }
      ]
    },
    "orange":
    {
      "term":"orange", 
      "morphs": [
        {
        "morph":"orange", 
        "type": "og",
        "res": "None"
        }, 
        {
        "morph": u"西朝鲜", 
        "type": "py",
        "res": "None"
        }
      ]
    }
  } 

class TermParser():

  def __init__(self, file):
    with open(file, 'r') as html:
      self.soup = BeautifulSoup(html, "html.parser")

  def get_terms(self):
    terms = {}

    for list_item in self.soup.find_all("li"):
      if list_item.get('class'): continue

      a_refs = list_item.find_all("a")
      py = list_item.find_all("i")

      if len(a_refs) is not 2:
        continue

      term = a_refs[0].get_text(' ', strip=True)
      english = a_refs[1].get_text(' ', strip=True)
      if py:
        pinyin = py[0].get_text(' ', strip=True)
        pinyin = re.sub(r"\(|\)", "", pinyin) 
      else:
        pinyin = "n/a"

      #TODO add more morph types
      morphs = [] 
      morphs.append({"morph": term, "type": "og", "res": "None"})
      morphs.append({"morph": pinyin, "type": "py", "res": "None"})

      morph_data = {}
      morph_data.update({"meaning": english})
      morph_data.update({"term": term})
      morph_data.update({"morphs": morphs})

      terms.update({term : morph_data})

    return terms
