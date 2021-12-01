# -*- coding: utf-8 -*-
"""
Script to get Address based off Landmark
"""

import pandas as pd
import csv
from serpapi import GoogleSearch

NYCPLACES = pd.read_csv('NYC.csv')
nycPlaces = NYCPLACES['Name']
nycPlaces = nycPlaces[:]

i=0
for x in nycPlaces:
    try:
        params = {
          "engine": "google_maps",
          "q": x,
          "ll": "@40.7455096,-74.0083012,15.1z",
          "type": "search",
          "api_key": "2ad6802d00cafff9f1a3419ce791e40d0ca25939f79cc8fda2ba003af97fd821"
        }
    
        search = GoogleSearch(params)
        result = search.get_dict()['place_results']['address']
        result = result.split(", ")
        statezip = result.pop().split(" ")
        NYCPLACES['Address'][i] = result[0]
        NYCPLACES['City'][i] = result[1]
        NYCPLACES['State'][i] = statezip[0]
        NYCPLACES['Zipcode'][i] = statezip[1]
        print(x + ':'+ str(i), '\n')
        i += 1  
        NYCPLACES.to_csv('NYC.csv', index = False)
    except:
        i += 1 
            
