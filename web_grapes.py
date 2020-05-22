#!/usr/bin/env python
# coding: utf-8

# imports
import pandas as pd
import requests
import numpy as np
import re
from bs4 import BeautifulSoup
import datetime

# pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# create empty dataframe
all_data = pd.DataFrame(index=[], columns=['Varietal','Type','Appellation','Qty','Price','Date','Listing_ID'])

# find final record and set maximum page
URL = "https://www.winebusiness.com/classifieds/grapesbulkwine/?sort_type=1&sort_order=desc&start=1#anchor1"
res = requests.get(URL)
soup = BeautifulSoup(res.content,'lxml')
searched_word = 'Results'
find_string = soup.body.find(text=re.compile(searched_word), recursive=True)
def largestNumber(in_str):
    l=[int(x) for x in in_str.split() if x.isdigit()]
    return max(l) if l else None
max_result = largestNumber(find_string)
page_max = ((int(max_result/50))*50)+2

#Create loop through URL's
for i in range(1,page_max,50):
    # Set URL
    URL = "https://www.winebusiness.com/classifieds/grapesbulkwine/?sort_type=1&sort_order=desc&start={}#anchor1".format(i)
    res = requests.get(URL)
    soup = BeautifulSoup(res.content,'lxml')

    # Define specific table
    table = soup.find("table", attrs={"class": "table wb-cl-table"})
    df = pd.read_html(str(table))[0]

    # Add Listing_ID's
    tbody = table.find("tbody")
    df['Listing_ID'] = [np.where(tag.has_attr('href'),tag.get('href'),"no link") for tag in tbody.find_all('a')]
    
    #Create output table
    all_data = pd.concat([all_data, df], ignore_index=True)
    
#Add datestamp
now = datetime.datetime.now()
datestamp = now.strftime("%Y-%m-%d %H:%M:%S")
all_data['Datestamp'] = datestamp
all_data