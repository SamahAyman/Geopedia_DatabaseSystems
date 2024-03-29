# -*- coding: utf-8 -*-
"""wikipedia_crawler.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iHtVAGM9qn_2-Zl4u22pshGaIy163bo3
"""

#installations
!pip install beautifulsoup4
!pip install pandas

# import the libraries
import requests
import bs4
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re

"""### Getting Continents"""

def get_continents():
    #the seed URL of all continents of the world
    URL = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_"

    #list for the continents names and their wiki URLs
    continents = {}
    continents ['continent_name'] = ['Africa','Asia','Europe','North_America','South_America','Oceania','Antarctica']
    continents ['continent_url']  = []
    
    for i in range(7):
        continents ['continent_url'].append(URL+continents ['continent_name'][i])
    
    return continents

"""### Getting Countries"""

def get_countries(continents):
    #list of all the countries of the world (from all the 7 continents)
    countries = {}
    countries['country_index'] = []
    countries['country_name']  = []
    countries['country_url']  = []
    countries_counter = 0

    #getting the countries names and URLs
    for continent in range(7):
        page = requests.get(continents ['continent_url'][continent])
        soup = BeautifulSoup(page.content)

        # getting the table rows
        table_rows = list(soup.find(class_ = "wikitable").tbody.children) 
        table_rows_num = len(table_rows)
        
        #getting the country_name
        for i in range(table_rows_num): 
            table_row = table_rows[i]
            country_name = None
            if type(table_row)!= bs4.element.NavigableString:           
                for table_data in table_row.children:
                    # getting country_name
                    if type(table_data)!= bs4.element.NavigableString:
                        country_tag = table_data.find("a", title=True)
                        if country_tag:
                            if not country_name:
                                country_name = country_tag.text
                                if country_name:
                                    countries_counter +=1
                                    countries['country_name'].append(country_name)
                                    countries['country_index'].append(countries_counter)
                                    countries['country_url'].append('https://en.wikipedia.org' + country_tag.get('href'))
    return countries

############### defining the methods to get president info ###############
presidents = {}
presidents['name'] = []
presidents['birthdate'] = []
presidents['assuming_office_date'] = []
presidents['political_party'] = []
presidents['president_name'] = []
presidents['ruling_country'] = []

president_entry = []
#getting the president name
def get_president_name(url):
    name=url.rsplit('/',1)
    name=url.rsplit('/',1)[1]
    name=name.replace('_', ' ')
    return name

#getting the president birthdate
def get_president_birthdate(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content)
    table = soup.find(class_ = "infobox vcard").tbody.children     
    if type(table)!= bs4.element.NavigableString:           
        for table_data in table:
            if type(table_data)!= bs4.element.NavigableString:
                tag = table_data.find("th")
                if (tag is None):
                  continue
                if (tag.text == "Born"):
                  birthdate = tag.find_next_sibling()
                  birthdate = birthdate.find("span").text
    return birthdate

#getting the date the president assumed office
def get_president_assuming_office_date(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    table = soup.find(class_ = "infobox vcard").tbody 
    tag = table.find(string=re.compile("Assumed office")).find_parent('td').text
    assuming_office = tag
    return assuming_office

#getting the president political party
def get_president_political_party(url):  #need to pass the url of the president here
    page = requests.get(url)
    soup = BeautifulSoup(page.content)
    table = soup.find(class_ = "infobox vcard").tbody.children     
    if type(table)!= bs4.element.NavigableString:           
        for table_data in table:
            if type(table_data)!= bs4.element.NavigableString:
                tag = table_data.find("th")
                if (tag is None):
                  continue
                if (tag.text == "Political party"):
                  political_party = tag.find_next_sibling().text 
    return political_party 

##########################################################################

url = "https://en.wikipedia.org/wiki/Abdelmadjid_Tebboune"
url = "https://en.wikipedia.org/wiki/Abdel_Fattah_el-Sisi"
name = get_president_name(url)
birthdate = get_president_birthdate(url)
assumed = get_president_assuming_office_date(url)
party = get_president_political_party(url)
print(name)
print(birthdate)
print(assumed)
print(party)

















url = "https://en.wikipedia.org/wiki/Abdelmadjid_Tebboune"
x=url.rsplit('/',1)
x=url.rsplit('/',1)[1]
x=x.replace('_', ' ')
print(x)

#trial cell
presidents['political_party'] = []
page = requests.get("https://en.wikipedia.org/wiki/Abdelmadjid_Tebboune")
soup = BeautifulSoup(page.content)

# table = soup.find(class_ = "infobox vcard").tbody 
# tag = table.find(string=re.compile("Assumed office")).find_parent('td').text
# print (tag)
table = soup.find(class_ = "infobox vcard").tbody.children     
if type(table)!= bs4.element.NavigableString:           
    for table_data in table:
        if type(table_data)!= bs4.element.NavigableString:
            tag = table_data.find("th")
            if (tag is None):
              continue
            if (tag.text == "Born"):
              birthdate = tag.find_next_sibling()
              birthdate = birthdate.find("span").text
              print(birthdate)

############### defining the methods to get country info ###############
#getting the area of the country
def get_country_area()
return 

#getting the area of the country
def get_country_area()
return 

#getting the area of the country
def get_country_area()
return 

#getting the area of the country
def get_country_area()
return 

########################################################################









page = requests.get("https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Africa")
soup = BeautifulSoup(page.content)

# getting the table rows
table_rows = list(soup.find(class_ = "wikitable sortable").tbody.children)

table_rows_num = len(table_rows)
country_name = None     
capital_name = None
latitude = None
longitude = None
Population = None
language = None
counter = 0; 

for i in range(table_rows_num): 
    table_row = table_rows[i]
    country_name = None
    capital_name = None
    language = None
    if type(table_row)!= bs4.element.NavigableString:           
        for table_data in table_row.children:
            # getting country_name
            if type(table_data)!= bs4.element.NavigableString:
                country_tag = table_data.find("a", title=True)
                if country_tag:
                    if not country_name:
                        country_name = country_tag.text
                        counter = counter + 1 
                        print(country_name)
            
            # getting capital_name
            #if type(table_data)!= bs4.element.NavigableString:
            #    capital_tag = table_data.find("a", title=True)
            #    if capital_tag:
            #        if not capital_name:
            #            capital_name = capital_tag.text
            #            print(capital_name)

print("Found", counter, "countries in Africa");

import re
def make_sure_with_regex_that_this_is_ib_country_largest(class_attribute_value):
    return class_attribute_value and re.compile("ib-.*-largest").search(class_attribute_value)

table_rows_num = len(table_rows) # to define the range of our loop
# we will store the scraped data here
country_name = None     
capital_name = None
latitude = None
longitude = None

# of course you can consume the iterator like `for row in table_rows:`
# but I found it helpful to manipulate the current index of iteration in some situations

for i in range(table_rows_num): 
    table_row = table_rows[i]
    for table_data in table_row.children:
        
        # getting name
        country_name_tag = table_data.find(class_="country-name")
        
        # this condition will only be true if the current table_row
        # contains "country_name" class value ... this will make it
        # safe to run the "parsing" logic for every row without
        # the fear of overwriting the data you scraped
        if country_name_tag:
            country_name = country_name_tag.text
        
        # getting the capital name and coordinates
        capital_tag = table_data.find(class_=make_sure_with_regex_that_this_is_ib_country_largest)
        # See the if condition again so we don't overwrite the data
        # we scraped
        if capital_tag:
            second_child = list(table_row.children)[1]
            capital_name_tag = second_child.find(title=True)
            if capital_name_tag:
                capital_name = capital_name_tag.text

            latitude = second_child.find(class_="latitude").text
            longitude = second_child.find(class_="longitude").text

#print the elements separated by ..
print(country_name, capital_name, latitude, longitude, sep = ' .. ')

# we only have one row of data 
import pandas as pd
to_be_transformed_into_pandas_dataframe = [{"id": 1, "name": country_name, "capital": capital_name, "latitude": latitude, "longitude": longitude}]
# transform into dataframe
df = pd.DataFrame(to_be_transformed_into_pandas_dataframe)

#print the data frame
df

#Load this dataframe into csv that would finally go into your database
df.to_csv("country_data.csv", sep=',', encoding='utf-8', index=False)

#try reading the new file
!cat country_data.csv











############################ scratches #################################
#print the list of all continents names and their wiki URLs
print( continents ['continent_name'])
print(*continents ['continent_url'], sep = "\n")

#print the countries
print("number of countries of the world = ", countries_counter)
print (countries['country_name'])
print (countries['country_index'])
print (countries['country_url'])



############################ scratches #################################