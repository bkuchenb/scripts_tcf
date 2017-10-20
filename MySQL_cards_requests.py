# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 2017

@author: bk00chenb
"""

import MySQLdb
import requests
from bs4 import BeautifulSoup
#Import time module to force the program to wait.
import time
import random
#******************************************************************************
def sql_insert_card(card_data):
    #Add the card to tcf_cards.
    insert_card = ("INSERT INTO tcf_cards"
                   "(card_id, set_id, card_number, card_name, "
                   "team_id, player_id, value_high, value_low) "
                   "VALUES(%(card_id)s, %(set_id)s, %(card_number)s, "
                   "%(card_name)s, %(team_link)s, %(player_number)s, "
                   "%(value_high)s, %(value_low)s)")
#debugging-------------------------------------------------------------------->
    print(card_data['card_number'], card_data['card_name'])
    try:
        cursor.execute(insert_card, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(card_url)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
#******************************************************************************
def sql_insert_player(card_data):
    #Add the set to tcf_players
    insert_player = ("INSERT INTO tcf_players"
                   "(player_id, player_name) "
                   "VALUES(%(player_number)s, %(player)s)")
#debugging-------------------------------------------------------------------->
    #print(insert_player % card_data)
    try:
        cursor.execute(insert_player, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(player_link)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
#******************************************************************************
def sql_insert_set(card_data):
    #Add the set to tcf_sets2
    insert_set = ("INSERT INTO tcf_sets2"
                   "(set_year, category, set_name) "
                   "VALUES(%(set_year)s, %(category)s, %(set_name)s)")
#debugging-------------------------------------------------------------------->
    #print(insert_set % card_data)
    try:
        cursor.execute(insert_set, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(set_name_link)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
#******************************************************************************
def sql_insert_team(card_data):
    #Add the set to tcf_players
    insert_team = ("INSERT INTO tcf_teams"
                   "(team_id, team_name) "
                   "VALUES(%(team_link)s, %(team)s)")
#debugging-------------------------------------------------------------------->
    #print(insert_team % card_data)
    try:
        cursor.execute(insert_team, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(team_link)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
#******************************************************************************
def sql_select_card(card_data):
    #Get the card_id.
    select_card = ("SELECT card_id "
                  "FROM tcf_cards "
                  "WHERE card_id = %(card_id)s")
#debugging-------------------------------------------------------------------->
    #print(select_card % values_card)
    cursor.execute(select_card, card_data)
    card_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(card_id), 'card(s) were found.')
    return len(card_id)
#******************************************************************************
def sql_select_player(card_data):
    #Get the player_id.
    select_player = ("SELECT player_id "
                  "FROM tcf_players "
                  "WHERE player_id = %(player_number)s")
    cursor.execute(select_player, card_data)
    player_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(player_id), 'player(s) were found.')
    return len(player_id)
#******************************************************************************
def sql_select_set(card_data):
    #Get the set_id.
    select_set = ("SELECT set_id "
                  "FROM tcf_sets2 "
                  "WHERE set_year = %(set_year)s "
                  "AND category = %(category)s AND set_name = %(set_name)s")
#debugging-------------------------------------------------------------------->
    #print(select_set % card_data)
    cursor.execute(select_set, card_data)
    set_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(set_id), 'set(s) were found.')
    return set_id
#******************************************************************************
def sql_select_team(card_data):
    #Get the team_id.
    select_team = ("SELECT team_id "
                  "FROM tcf_teams "
                  "WHERE team_id = %(team_link)s")
    cursor.execute(select_team, card_data)
    team_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(team_id), 'team(s) were found.')
    return len(team_id)
#******************************************************************************
def get_card_page_data(card_soup, card_data):
    #Get the list that contains the data.
    class_name = 'similar-item similar-item-new'
    ul_list = card_soup.find_all('ul', class_name)
    li_list = ul_list[0].find_all('li')
    #Cycle through the li_list and save the data.
    for row in li_list:
        #Strip and save the innerHtml.
        temp_str = row.text.strip()
        if 'Set:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Set:', '').strip()
            #Get the set link.
            a_list = row.find_all('a')
            card_data['set_name_link'] = a_list[0]['href']
            #Get the year from the link.
            temp_list = card_data['set_name_link'].split('/')
            card_data['set_year'] = temp_list[len(temp_list) - 3]
            #Remove the year from the temp_str and save as set_name
            temp_str = temp_str.replace(card_data['set_year'], '', 1)
            card_data['set_name'] = temp_str.strip()
        if 'Card Number:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Card Number:', '').strip()
            card_data['card_number'] = temp_str
        if 'Player:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Player:', '').strip()
            card_data['player'] = temp_str
            #Get the player link.
            a_list = row.find_all('a')
            card_data['player_link'] = a_list[0]['href']
            #Get the player number from the link.
            temp_list = card_data['player_link'].split('-')
            card_data['player_number'] = temp_list[len(temp_list) - 1]
        if 'Sport' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Sport: ', '')
            #If more than 1 category exists, take the first.
            temp_list = temp_str.split(',')
            card_data['category'] = temp_list[0]
        if 'Team:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Team: ', '')
            card_data['team'] = temp_str
            #Get the team link.
            a_list = row.find_all('a')
            temp_str = a_list[0]['href']
            temp_str = temp_str.replace('https://www.beckett.com/', '')
            card_data['team_link'] = temp_str
    #Update the card_name field.
    temp_str = card_data['card_name']
    temp_str = temp_str.replace(card_data['set_year'], '', 1).strip()
    temp_str = temp_str.replace(card_data['set_name'], '', 1).strip()
    temp_str = temp_str.replace(card_data['card_number'], '', 1).strip()
    card_data['card_name'] = temp_str
    #Get price information if available.
#    price_list = list()
#    td_list = card_soup.find_all('td')
#    for entry in td_list:
#        if '$' in entry.text:
#            price = entry.text.replace('$', '')
#            price = price.replace(',', '')
##debugging-------------------------------------------------------------------->
#            #print(card_data['card_name'], price)
#            price_list.append(float(price))
#    #Sort the price list to get high and low values.
#    if(len(price_list) > 0):
#        price_list.sort()
#        card_data['value_high'] = price_list[len(price_list) - 1]
#        card_data['value_low'] = price_list[0]
#debugging-------------------------------------------------------------------->
    #print(card_data)
    return card_data
#******************************************************************************
def get_next_page(url):
    #Get the next page.
    r = requests.get(url)
    #Save the content.
    c = r.content
    #Parse the content and return the results.
    return BeautifulSoup(c, 'lxml')
#******************************************************************************
def get_page_links(soup):
    #Create a dictionary to store return values.
    page_links = {}
    #Get the li element that holds the next page button.
    li_list = soup.find_all('li', 'next')
    #Get the a element that holds the next page link.
    a_list = li_list[0].find_all('a')
    page_links['next_page_link'] = a_list[0]['href']
    #Get the li element that holds the last page button.
    li_list2 = soup.find_all('li', 'last')
    #Get the a element that holds the last page link.
    a_list2 = li_list2[1].find_all('a')
    page_links['last_page_link'] = a_list2[0]['href']
    #Find the next and last page number.
    temp_list = page_links['next_page_link'].split('=')
    page_links['next_page_num'] = int(temp_list[len(temp_list) - 1])
    temp_list = page_links['last_page_link'].split('=')
    page_links['last_page_num'] = int(temp_list[len(temp_list) - 1])
    return page_links
#******************************************************************************
def get_year_page_data(soup, data_list):
    #Get all the card names that are displayed.
    li_list = soup.find_all('li', 'title')
    for i in range(0, len(li_list)):
        #Create a dictionary to store return values.
        card_data = {'value_high': 0, 'value_low': 0,
                     'team_link': '', 'team': '',
                     'player': '', 'player_link': '', 'player_number': ''}
#debugging-------------------------------------------------------------------->
        #print('Card#:', i + 1)
        #Get the a element that contains the information needed.
        a_list = li_list[i].find_all('a')
        card_data['card_name'] = a_list[0].text
        card_data['card_url'] = a_list[0]['href']
        #Get the card_id from the link.
        temp_list = card_data['card_url'].split('-')
        card_data['card_id'] = temp_list[len(temp_list) - 1]
        #Get additional data from the scraped links.
#function call---------------------------------------------------------------->
        card_soup = search_for_card(card_data['card_url'])
#function call---------------------------------------------------------------->
        card_data = get_card_page_data(card_soup, card_data)
        data_list.append(card_data)
    return data_list
#******************************************************************************
def search_for_card(url):
    #Get the card page.
    r = requests.get(url)
    #Save the content.
    c = r.content
    #Parse the content.
    return BeautifulSoup(c, 'lxml')
#******************************************************************************
def search_for_year(year):
    #Search for cards in the given year on Beckett.
    url = ('https://www.beckett.com/search/?term='
           + str(year) + '&year_start=' + str(year))
    #Get the card page.
    r = requests.get(url)
    #Save the content.
    c = r.content
    #Parse the content.
    return BeautifulSoup(c, 'lxml')
#******************************************************************************
#Connect to the inceff database.
user = 'bk00chenb'
password = 'NR8A*Ecb*'
host = 'inceff.ctlel9cvjtqf.us-west-2.rds.amazonaws.com'
database = 'inceff'
cnx = MySQLdb.connect(user = user, password = password,
                      host = host, database = database)
#Create a cursor object to use for the database connection.
cursor = cnx.cursor()
#Set the autocommit to zero.
cursor.execute('SET autocommit = 0')
cnx.commit()

year = 1920
page = 1
#function call---------------------------------------------------------------->
#soup = search_for_year(year)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Optional page override. Change the first range number to (page - 1).
page_override = ('https://www.beckett.com/search/?term=' + str(year)
                 + '&year_start=' + str(year) + '&rowNum=25&page='
                 + str(page))
soup = get_next_page(page_override)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Get the next and last page links.
#function call---------------------------------------------------------------->
page_links = get_page_links(soup)
#Cycle through the pages and scrape each page.
for x in range(page - 1, page_links['last_page_num']):
    print('Viewing page', str(x + 1) + '...')
    #Create a list to store card data.
    data_list = list()
#function call---------------------------------------------------------------->
    data_list = get_year_page_data(soup, data_list)
    #Add the cards to the inceff database.
    for row in data_list:
        #Add the set if it isn't in the table.
        set_id = sql_select_set(row)
        if(len(set_id) == 0):
            sql_insert_set(row)
            set_id = sql_select_set(row)
        row['set_id'] = set_id[0][0]
        #Add the card if it isn't in the table.
        count = sql_select_card(row)
        if(count == 0):
            sql_insert_card(row)
        #Add the team if available.
        if(row['team_link']):
            count = sql_select_team(row)
            if(count == 0):
                sql_insert_team(row)
        #Add the player if available.
        if(row['player_link']):
            count = sql_select_player(row)
            if(count == 0):
                sql_insert_player(row)
    if not(x == page_links['last_page_num'] - 1):
        #Wait a random time between page requests.
        time.sleep(random.randint(20, 30))
#function call---------------------------------------------------------------->
        soup = get_next_page(page_links['next_page_link'])
#function call---------------------------------------------------------------->
        page_links = get_page_links(soup)
        
cursor.close()
cnx.close()
print('All records have been updated.')