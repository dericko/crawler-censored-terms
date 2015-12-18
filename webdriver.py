#!/usr/bin/python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver():
  def __init__(self, base, search_bar, search_btn):
    self.base = base
    self.search_bar = search_bar
    self.search_btn = search_btn
#    self.driver = webdriver.PhantomJS() # headless would be nice
    self.driver = webdriver.Firefox() # GUI to deal w/ captchas
    self.driver.set_window_size(1120, 550)
    self.driver.get(self.base)

  def search(self, term):

    # Run search 
    searchbar = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, self.search_bar)))
    searchbtn = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, self.search_btn)))

    if not (searchbar and searchbtn): 
      print 'missing searchbar'
      self.driver.quit()
      return;

    searchbar.clear()
    searchbar.send_keys(term)
    searchbtn.click()

    # Wait and store results
    try:
      self.search_feed = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.CLASS_NAME, "search_feed"))) # only used for waiting
      self.last_source = self.driver.page_source
      self.last_url = self.driver.current_url
    except:
      self.driver.save_screenshot('ss.png') # try to print the problem
      self.driver.quit()


  def page_source(self):
    return self.last_source
  
  def url(self):
    return self.last_url 

  def quit(self):
    self.driver.quit()
