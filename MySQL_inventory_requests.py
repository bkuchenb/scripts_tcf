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
def sql_insert_card(card_data):
    #Add the card to tcf_cards.
    insert_card = ("INSERT INTO tcf_card"
                   "(card_id, set_id, card_number, card_name, "
                   "team_id, player_id, value_high, value_low) "
                   "VALUES(%(card_id)s, %(set_id)s, %(card_number)s, "
                   "%(card_name)s, %(team_link)s, %(player_number)s, "
                   "%(value_high)s, %(value_low)s)")
#debugging-------------------------------------------------------------------->
    #print(insert_card % card_data)
    try:
        cursor.execute(insert_card, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert_card % card_data)
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(card_url)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
def sql_insert_inventory(card_data):
    #Add the card to tcf_inventory.
    insert_card = ("INSERT INTO tcf_inventory"
                   "(card_id, set_id, inventory_id, condition, "
                   "quantity, max, min, price) "
                   "VALUES(%(card_id)s, %(set_id)s, %(inventory_id)s, "
                   "%(condition)s, %(quantity)s, %(max)s, "
                   "%(min)s, %(price)s)")
#debugging-------------------------------------------------------------------->
    #print(insert_card % card_data)
    try:
        cursor.execute(insert_card, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert_card % card_data)
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(card_url)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
def sql_insert_player(card_data):
    #Add the set to tcf_players
    insert_player = ("INSERT INTO tcf_player"
                   "(player_id, player_name) "
                   "VALUES(%(player_id)s, %(player_name)s)")
#debugging-------------------------------------------------------------------->
    #print(insert_player % card_data)
    try:
        cursor.execute(insert_player, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert_player % card_data)
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(player_link)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
def sql_insert_set(card_data):
    #Add the set to tcf_sets2
#    insert_set = ("INSERT INTO tcf_sets2"
#                   "(set_year, category, set_name) "
#                   "VALUES(%(set_year)s, %(category)s, %(set_name)s")
    insert_set = ("INSERT INTO tcf_set"
                   "(set_year, category_id, set_name, manufacturer_id, "
                   "brand_id) "
                   "VALUES(%(set_year)s, %(category_id)s, %(set_name)s, "
                   "%(manufacturer_id)s, %(brand_id)s")
#debugging-------------------------------------------------------------------->
    #print(insert_set % card_data)
    try:
        cursor.execute(insert_set, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert_set % card_data)
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(set_name_link)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
def sql_insert_team(card_data):
    #Add the set to tcf_players
    insert_team = ("INSERT INTO tcf_team"
                   "(team_id, team_name) "
                   "VALUES(%(team_id)s, %(team_name)s)")
#debugging-------------------------------------------------------------------->
    #print(insert_team % card_data)
    try:
        cursor.execute(insert_team, card_data)
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert_team % card_data)
        insert_error = ("INSERT INTO tcf_sql_errors"
                        "(insert_statement) "
                        "VALUES(%(team_link)s)")
        cursor.execute(insert_error, card_data)
        cnx.commit()
def sql_select_card(card_data):
    #Get the card_id.
    select_card = ("SELECT card_id "
                  "FROM tcf_card "
                  "WHERE card_id = %(card_id)s")
#debugging-------------------------------------------------------------------->
    #print(select_card % card_data)
    cursor.execute(select_card, card_data)
    card_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(card_id), 'card(s) were found.')
    return len(card_id)
def sql_select_inventory(card_data):
    #Get the card_id.
    select_card = ("SELECT inventory_id "
                  "FROM tcf_inventory "
                  "WHERE inventory_id = %(inventory_id)s")
#debugging-------------------------------------------------------------------->
    #print(select_card % card_data)
    cursor.execute(select_card, card_data)
    card_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(card_id), 'card(s) were found.')
    return len(card_id)
def sql_select_player(card_data):
    #Get the player_id.
    select_player = ("SELECT player_id "
                  "FROM tcf_player "
                  "WHERE player_id = %(player_id)s")
    cursor.execute(select_player, card_data)
    player_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(player_id), 'player(s) were found.')
    return len(player_id)
def sql_select_set(card_data):
    #Get the set_id.
    select_set = ("SELECT set_id "
                  "FROM tcf_set "
                  "WHERE set_year = %(set_year)s "
                  "AND category_id = %(category_id)s "
                  "AND set_name = %(set_name)s")
#debugging-------------------------------------------------------------------->
    #print(select_set % card_data)
    cursor.execute(select_set, card_data)
    set_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(set_id), 'set(s) were found.')
    return set_id
def sql_select_team(card_data):
    #Get the team_id.
    select_team = ("SELECT team_id "
                  "FROM tcf_team "
                  "WHERE team_id = %(team_id)s")
    cursor.execute(select_team, card_data)
    team_id = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(team_id), 'team(s) were found.')
    return len(team_id)
def get_card_id(card_soup, card_data):
    #Get all the card names that are displayed.
    li_list = card_soup.find_all('li', 'title')
    #Get the a element that contains the information needed.
    a_list = li_list[0].find_all('a')
    #Get the card_id from the link.
    temp_list = a_list[0]['href'].split('-')
    card_data['card_id'] = temp_list[len(temp_list) - 1]
    card_data['checklist_link'] = a_list[0]['href']
#debugging-------------------------------------------------------------------->
    #print(card_data)    
    return card_data
def get_card_checklist_page(card_soup, card_data):
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
            set_name_link = a_list[0]['href']
            #Get the year from the link.
            temp_list = set_name_link.split('/')
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
            card_data['player_name'] = temp_str
            #Get the player link.
            a_list = row.find_all('a')
            player_link = a_list[0]['href']
            #Get the player number from the link.
            temp_list = player_link.split('-')
            card_data['player_id'] = temp_list[len(temp_list) - 1]
        if 'Sport:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Sport:', '').strip()
            #If more than 1 category exists, take the first.
            temp_list = temp_str.split(',')
            card_data['category_name'] = temp_list[0]
        if 'Team:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Team: ', '').strip()
            card_data['team_name'] = temp_str
            #Get the team link.
            a_list = row.find_all('a')
            temp_str = a_list[0]['href']
            temp_list = temp_str.split('=')
            card_data['team_id'] = temp_list[len(temp_list) - 1]
    #Update the card_name field.
    temp_str = card_data['card_name']
    temp_str = temp_str.replace(card_data['set_year'], '', 1).strip()
    temp_str = temp_str.replace(card_data['set_name'], '', 1).strip()
    temp_str = temp_str.replace(card_data['card_number'], '', 1).strip()
    card_data['card_name'] = temp_str
#debugging-------------------------------------------------------------------->
    #print(card_data)
    return card_data
def get_card_tcf_marketplace(card_soup, card_data):
    #Get the span that contains the price data.
    div_list = card_soup.find_all('div', 'price-div')
    for row in div_list:
        #Strip and save the innerHtml.
        temp_str = row.text.strip()
        if 'Price:' in temp_str:
            #Remove the title and discount rate.
            temp_str = temp_str.replace('Price:', '').strip()
            temp_str = temp_str.replace('xx% off Beckett Value', '').strip()
            card_data['price'] = float(temp_str.replace('$', ''))
            break
    #Get the div that contains the grade data.
    div_list = card_soup.find_all('div', 'condition')
    for row in div_list:
        #Strip and save the innerHtml.
        temp_str = row.text.strip()
        if 'Condition:' in temp_str:
            #Remove the title.
            card_data['condition'] = temp_str.replace('Condition:', '').strip()
    #Get the h4 that contains qty data.
    h4_list = card_soup.find_all('h4', 'lineheight-34')
    for row in h4_list:
        #Strip and save the innerHtml.
        temp_str = row.text.strip()
        if 'Qty Available: ' in temp_str:
            temp_str = temp_str.replace('Qty Available:', '').strip()
            card_data['quantity'] = temp_str
            card_data['max'] = temp_str
    #Get the sport, team, brand, and manufaturer.
    li_list = card_soup.find_all('li')
    for row in li_list:
        #Strip and save the innerHtml.
        temp_str = row.text.strip()
        if 'Sport:' in temp_str:
            temp_str = temp_str.replace('Sport:', '').strip()
            card_data['category'] = temp_str
            #Get the team info.
            next_li = row.next_sibling.next_sibling
            temp_str = next_li.text.replace('Team:', '').strip()
            card_data['team_name'] = temp_str
            a_list = next_li.find_all('a')
            temp_list = a_list[0]['href'].split('=')
            card_data['team_id'] = temp_list[len(temp_list) - 1]
            #Get the brand info.
            next_li = next_li.next_sibling.next_sibling
            temp_str = next_li.text.replace('Brand:', '').strip()
            card_data['brand'] = temp_str
            a_list = next_li.find_all('a')
            temp_list = a_list[0]['href'].split('=')
            card_data['brand_id'] = temp_list[len(temp_list) - 1]
            #Get the manufacturer info.
            next_li = next_li.next_sibling.next_sibling
            temp_str = next_li.text.replace('Manufacturer:', '').strip()
            card_data['manufacturer'] = temp_str
            a_list = next_li.find_all('a')
            temp_list = a_list[0]['href'].split('=')
            card_data['manufacturer_id'] = temp_list[len(temp_list) - 1]
    return card_data
def get_card_price(card_soup, card_data):
    #Get the div that contains the price data.
    div_list = card_soup.find_all('div', 'price_to_container')
    if(len(div_list) > 0):
        temp_str = div_list[0].text
        temp_list = temp_str.split('to')
        if len(temp_list) > 0:
            card_data['value_low'] = float(temp_list[0].replace('$', ''))
        if len(temp_list) > 1:
            card_data['value_high'] = float(temp_list[1].replace('$', ''))
        else:
            card_data['value_high'] = card_data['value_low']
    return card_data
def get_inventory_page_data(soup, data_list):
    #Get all the card names that are displayed.
    li_list = soup.find_all('li', 'title')
#debugging-------------------------------------------------------------------->
    #print(len(li_list), 'li elements with className="title"')
    #For each card on the page, scrape the data and check the database.
    for i in range(0, len(li_list)):
        #Create a dictionary to store return values.
        card_data = {'brand_id': '', 'brand_name': '',
                     'category_id': '', 'category_name': '',
                     'manufacturer_id': '', 'manufacturer_name': '',
                     'player_id': '', 'player_name': '',
                     'team_id': '', 'team_name': '',
                     'set_id': '', 'set_year': '', 'set_name': '',
                     'card_id': '', 'card_number': '', 'card_name': '',
                     'value_low': 0, 'value_high': 0,
                     'inventory_id': '', 'condition': '', 'quantity': '',
                     'min': 0, 'max': '', 'price': 0
                     }
        print('Card#:', i + 1)
        #Get the a element that contains the information needed.
        a_list = li_list[i].find_all('a')
        card_url = a_list[0]['href']
        card_data['card_name'] = a_list[0].text
        #Get the inventory_id from the link.
        temp_list = card_url.split('_')
        card_data['inventory_id'] = temp_list[len(temp_list) - 1]
        #Get additional data from the scraped links.
#function call---------------------------------------------------------------->
        card_soup = search_for_card(card_url)
#function call---------------------------------------------------------------->
        card_data = get_card_tcf_marketplace(card_soup, card_data)
        #Find the card_id
        temp_str = card_data['card_name'].replace(' ', '+')
        #Format string for web address.
        temp_str = temp_str.replace('#', '%23')
        temp_str = temp_str.replace('/', '%2F')
        temp_list = card_data['card_name'].split(' ')
        url = ('https://www.beckett.com/search/?term='
               + temp_str + '&year_start=' + temp_list[0])
        #Get the card_id.
#function call---------------------------------------------------------------->
        card_soup = search_for_card(url)
#function call---------------------------------------------------------------->
        card_data = get_card_id(card_soup, card_data)
        #Get price information for the card if available.
        url = ('https://marketplace.beckett.com/search_new/?term='
               + temp_str)
#function call---------------------------------------------------------------->
        card_soup = search_for_card(url)
#function call---------------------------------------------------------------->
        card_data = get_card_price(card_soup, card_data)
        #Get more information from the checklist_link.
#function call---------------------------------------------------------------->
        card_soup = search_for_card(card_data['checklist_link'])
#function call---------------------------------------------------------------->
        card_data = get_card_checklist_page(card_soup, card_data)      
        data_list.append(card_data)
    return data_list
def get_next_page(url):
    #Get the next page.
    r = requests.get(url)
    #Save the content.
    c = r.content
    #Parse the content and return the results.
    return BeautifulSoup(c, 'lxml')
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
def search_for_card(url):
    #Get the card page.
    r = requests.get(url)
    #Save the content.
    c = r.content
    #Parse the content.
    return BeautifulSoup(c, 'lxml')
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

page = 1
#Go to the tcf marketplace page and search newly added items.
url = ('https://marketplace.beckett.com/thecollectorsfriend_700/'
       'search_new/?result_type=59&NewlyMPAdded=1&page=' + str(page))
#Make the soup.
#function call---------------------------------------------------------------->
try:
    soup = get_next_page(url)
except requests.Timeout as err:
    print('Something went wrong: {}'.format(err))
    print(url)
#Get the next and last page links.
#function call---------------------------------------------------------------->
page_links = get_page_links(soup)
#Cycle through the pages and scrape each page.
for x in range(page - 1, page_links['last_page_num']):
    print('Page', x + 1)
    #Create a list to store card data.
    data_list = list()
#function call---------------------------------------------------------------->
    data_list = get_inventory_page_data(soup, data_list)
    #Add the cards to the inceff database.
    for row in data_list:
        #Check tcf_inventory to see if this card has been added.
#function call---------------------------------------------------------------->
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
        count = sql_select_inventory(row)
        if(count == 0):
            sql_insert_inventory(row)
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