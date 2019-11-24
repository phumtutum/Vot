import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime
import pandas as pd


urlpageDiaspora = 'https://prezenta.bec.ro/prezidentiale24112019/abroad-precincts'
urlpageRomania = 'https://prezenta.bec.ro/'
fnameDiaspora = "DateDiaspora.txt"
fnameRomania = "DateRomania.txt"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

driver = webdriver.Firefox()

intervalTimp = 280 # poate fi modificat pentru a obtine intervalul de timp la care se cer datele(by default sunt ~5 min)

while 0 < 1 :
    driver.get(urlpageDiaspora)
    driver.execute_script(
     "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(10)

    resultsDiaspora = driver.find_elements_by_xpath("//*[@id=\"root\"]/main/section/div[1]/div[1]")

    for result in resultsDiaspora:
        with open(fnameDiaspora , "a+", encoding="utf-8") as output:
           output.write( str( datetime.now().time() ) )
           output.write( str( result.text ) )
           output.write("\n\n\n\n\n")

    driver.get(urlpageRomania)
    driver.execute_script( "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;" )
    time.sleep(10)

    resultsRomania = driver.find_elements_by_xpath("//*[@id=\"root\"]/main/section/div[1]/div[1]")

    for result in resultsRomania:
        with open(fnameRomania, "a+", encoding="utf-8") as outputRomania:
            outputRomania.write(str(datetime.now().time()))
            outputRomania.write( str( result.text ) )
            outputRomania.write("\n\n\n\n\n")

    time.sleep(intervalTimp);
