#!/usr/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import re

def failure(html):
  return html.find_all("div", {"class":"pl_noresult"})

def success(html):
  return html.find_all("div", {"class":"feed_lists search_notes"})

# Term cannot be displayed
def blocked(html):
  return failure(html, fail_message) 

def no_results(w):
  return re.match(u'\u62b1\u6b49\uff0c\u672a\u627e\u5230\u201c', w)

def few_results(html):
  all_res = success_msg(html) 
  return len(all_res) < 5

def many_results(html):
  all_res = success_msg(html) 
  return len(all_res) >= 5


class ResponseHandler():
  def __init__(self, html):
    self.soup = BeautifulSoup(html, "html.parser")

  def response_type(self):
    res = failure(self.soup)

    if res:

      if no_results(res[0].find_all("p", {"class":"noresult_tit"})[0].get_text(' ', strip=True)):
        return "NO_RESULTS"
      else:
        return "BLOCKED"

    elif success(self.soup):

      if success(self.soup) < 5:
        return "FEW_RESULTS"
      else:
        return "MANY_RESULTS"

    else:
      return "ERROR CHECKING RESULTS"
