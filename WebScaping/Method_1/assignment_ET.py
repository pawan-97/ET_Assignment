# Importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# Scraping data with Exceptional handling
try:
    # sending request to the website
    html = requests.get('https://www.ongcindia.com/wps/wcm/connect/en/about-ongc/board-of-directors/')
    # persing the website with Beuatifulsoup
    bs = BeautifulSoup(html.text, 'lxml')
    # finding required html tag
    gnd_id = bs.find_all('div',class_='accordion-container')

    #creating list
    names=[]
    roles = []
    
    # fetching data using for loops
    for bod in gnd_id:
        name = bod.find_all('span',class_='bod-name')
        for i in name:
            names.append(i.text)
        role = bod.find_all('span',class_='bod-ds')
        for i in role:
            roles.append(i.text)
    print(names)
    print(roles)

    # Creating a dictionary
    raw_data = {'Name':names,'Role':roles}
    # Importing data into data frames
    data = pd.DataFrame(raw_data)
    # Saving data into csv
    data.to_csv('ongc_bod.csv')

except Exception as e:
    print(e)

