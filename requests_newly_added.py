# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 2017

@author: bk00chenb
"""

import MySQLdb
import requests
import re
from bs4 import BeautifulSoup

def sql_insert_attribute(card_data: dict, index: int):
    insert = ("INSERT INTO tcf_attribute(attribute_name) "
              "VALUES({attribute_name!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_brand(card_data: dict, index: int):
#Add the item if the number of ids and names matches.
    if(len(card_data['brand_id']) != len(card_data['brand_name'])):
        print("The number of ids and names doesn't match.")
        return
    insert = ("INSERT INTO tcf_brand(brand_id, brand_name, brand_url) "
              "VALUES({brand_id[" + str(index) + "]}, "
              "{brand_name[" + str(index) + "]!r}, "
              "{brand_url[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the statement.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_card(card_data: dict):
    insert = ("INSERT INTO tcf_card"
              "(card_id, set_id, card_number, card_name, "
              "image_src_back, image_src_front, "
              "value_high, value_low, print_run, card_url) "
              "VALUES({card_id}, {set_id}, {card_number!r}, "
              "{card_name!r}, {image_src_back!r}, {image_src_front!r}, "
              "{value_high}, {value_low}, {print_run}, {card_url!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_card_attribute(card_data: dict, index: int):
    insert = ("INSERT INTO tcf_card_attribute(card_id, attribute_id) "
              "VALUES({card_id}, {attribute_id})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_card_player(card_data: dict, index: int):
    insert = ("INSERT INTO tcf_card_player(player_id, card_id) "
              "VALUES({player_id[" + str(index) + "]}, "
              "{card_id})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_card_team(card_data: dict, index: int):
    insert = ("INSERT INTO tcf_card_team(team_id, card_id) "
              "VALUES({team_id[" + str(index) + "]}, "
              "{card_id})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_category(card_data: dict, index: int):
    insert = ("INSERT INTO tcf_category"
              "(category_id, category_name, category_url) "
              "VALUES({category_id[" + str(index) + "]}, "
              "{category_name[" + str(index) + "]!r}, "
              "{category_url[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_inventory(card_data: dict):
    insert = ("INSERT INTO tcf_inventory(inventory_id, card_id, grade, "
              "quantity, max, min, price, inventory_url) "
              "VALUES({inventory_id}, {card_id}, {condition!r}, "
              "{quantity}, {max}, {min}, {price}, {inventory_url!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_manufacturer(card_data: dict, index: int):
    #Add the item if the number of ids and names matches.
    if(len(card_data['manufacturer_id'])
    != len(card_data['manufacturer_name'])):
        print("The number of ids and names doesn't match.")
        return
    insert = ("INSERT INTO tcf_manufacturer"
              "(manufacturer_id, manufacturer_name, manufacturer_url) "
              "VALUES({manufacturer_id[" + str(index) + "]}, "
              "{manufacturer_name[" + str(index) + "]!r}, "
              "{manufacturer_url[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the statement.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_player(card_data: dict, index: int):
    #Add the item if the number of ids and names matches.
    if(len(card_data['player_id']) != len(card_data['player_name'])):
        print("The number of ids and names doesn't match.")
        return
    insert = ("INSERT INTO tcf_player(player_id, player_name, player_url) "
              "VALUES({player_id[" + str(index) + "]}, "
              "{player_name[" + str(index) + "]!r}, "
              "{player_url[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_set(card_data: dict):
    #Add the set to tcf_set if there is only one manufacturer and one brand.
    if(len(card_data['manufacturer_id']) > 1
       or len(card_data['brand_id']) > 1):
        print('There is more than 1 manufacturer or brand id.')
        return
    insert = ("INSERT INTO tcf_set"
              "(set_id, set_year, set_name, manufacturer_id, "
              "brand_id, set_url) "
              "VALUES({set_id}, {set_year!r}, {set_name!r}, "
              "{manufacturer_id[0]}, {brand_id[0]}, {set_url!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_set_category(card_data: dict, index: int):
    insert = ("INSERT INTO tcf_set_category(category_id, set_id) "
              "VALUES({category_id[" + str(index) + "]}, "
              "{set_id})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_insert_team(card_data: dict, index: int):
    #Add the item if the number of ids and names matches.
    if(len(card_data['team_id']) != len(card_data['team_name'])):
        print("The number of ids and names doesn't match.")
        return
    insert = ("INSERT INTO tcf_team(team_id, team_name, team_url) "
              "VALUES({team_id[" + str(index) + "]}, "
              "{team_name[" + str(index) + "]!r}, "
              "{team_url[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))


def sql_select_attribute(card_data: dict, index: int) -> list:
    select = ("SELECT attribute_id "
              "FROM tcf_attribute "
              "WHERE attribute_name = {attribute_name[" + str(index) + "]!r}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_brand(card_data: dict, index: int) -> list:
    select = ("SELECT brand_id "
              "FROM tcf_brand "
              "WHERE brand_id = {brand_id[" + str(index) + "]}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_card(card_data: dict) -> list:
    select = ("SELECT card_id "
              "FROM tcf_card "
              "WHERE card_id = {card_id}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_card_attribute(card_data: dict, index: int) -> list:
    select = ("SELECT * "
              "FROM tcf_card_attribute "
              "WHERE card_id = {card_id} "
              "AND attribute_id = {attribute_id}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_card_player(card_data: dict, index: int) -> list:
    select = ("SELECT * "
              "FROM tcf_card_player "
              "WHERE card_id = {card_id} "
              "AND player_id = {player_id[" + str(index) + "]}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_card_team(card_data: dict, index: int) -> list:
    select = ("SELECT * "
              "FROM tcf_card_team "
              "WHERE card_id = {card_id} "
              "AND team_id = {team_id[" + str(index) + "]}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_category(card_data: dict, index: int) -> list:
    select = ("SELECT category_id "
              "FROM tcf_category "
              "WHERE category_id = {category_id[" + str(index) + "]}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_inventory(card_data: dict) -> list:
    select = ("SELECT inventory_id "
              "FROM tcf_inventory "
              "WHERE inventory_id = {inventory_id}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_manufacturer(card_data: dict, index: int) -> list:
    select = ("SELECT manufacturer_id "
              "FROM tcf_manufacturer "
              "WHERE manufacturer_id = {manufacturer_id[" + str(index) + "]}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_player(card_data: dict, index: int) -> list:
    select = ("SELECT player_id "
              "FROM tcf_player "
              "WHERE player_id = {player_id[" + str(index) + "]}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_set(card_data: dict, index: int) -> list:
    select = ("SELECT tcf_set.set_id "
              "FROM tcf_set "
              "INNER JOIN tcf_set_category "
              "ON tcf_set.set_id = tcf_set_category.set_id "
              "WHERE tcf_set.set_year = {set_year!r} "
              "AND tcf_set_category.category_id = "
              "{category_id[" + str(index) + "]} "
              "AND tcf_set.set_name = {set_name!r}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_set_category(card_data: dict, index: int) -> list:
    select = ("SELECT * "
              "FROM tcf_set_category "
              "WHERE set_id = {set_id} "
              "AND category_id = {category_id[" + str(index) + "]}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_select_set_id() -> list:
    select = ("SELECT set_id FROM tcf_set ORDER BY set_id DESC LIMIT 1")
    cursor.execute(select)
    result = cursor.fetchone()[0]
#debugging-------------------------------------------------------------------->
    #print(result)
    return result


def sql_select_team(card_data: dict, index: int) -> list:
    select = ("SELECT team_id "
              "FROM tcf_team "
              "WHERE team_id = {team_id[" + str(index) + "]}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**card_data))
    cursor.execute(select.format(**card_data))
    result = cursor.fetchall()
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return result


def sql_update_inventory(card_data: dict):
    update = ("UPDATE tcf_inventory "
              "Set quantity = {quantity}, price = {price} "
              "WHERE inventory_id = {inventory_id}")
#debugging-------------------------------------------------------------------->
    #print(update.format(**card_data))
    try:
        cursor.execute(update.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the update fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(update.format(**card_data))


def add_card_data(card_data: dict):
    try:
        #Check to see if there is more than 1 brand_id.
        for index in range(0, len(card_data['brand_id'])):
            #Check to see if the brand has already been added.
            result = sql_select_brand(card_data, index)
            #If the brand doesn't exist, insert it into tcf_brand.
            if(len(result) == 0):
                sql_insert_brand(card_data, index)
                
        #Check to see if there is more than 1 manufacturer_id.
        for index in range(0, len(card_data['manufacturer_id'])):
            #Check to see if the manufacturer has already been added.
            result = sql_select_manufacturer(card_data, index)
            #If the manufacturer doesn't exist, insert it.
            if(len(result) == 0):
                sql_insert_manufacturer(card_data, index)

        #Check to see if there is more than 1 category_id.
        for index in range(0, len(card_data['category_id'])):
            #Check to see if the category has already been added.
            result = sql_select_category(card_data, index)
            #If the category doesn't exist, insert it into tcf_category.
            if(len(result) == 0):
                sql_insert_category(card_data, index)
                        
            #Check to see if the set has already been added.
            result = sql_select_set(card_data, index)
            #If the set doesn't exist, insert it into tcf_set.
            if(len(result) == 0):
                sql_insert_set(card_data)
            #If more than 1 set was found there is a problem.
            elif(len(result) > 1):
                print('More than 1 set:', card_data['set_name'],
                      'was found.')
                
            #Check to see if the set_category has already been added.
            result = sql_select_set_category(card_data, index)
            #If the set_category doesn't exist, insert it.
            if(len(result) == 0):
                sql_insert_set_category(card_data, index)
        
        #Check to see if the card has already been added to tcf_card.
        result = sql_select_card(card_data)
        if(len(result) == 0):
            #If the card_id doesn't exist, insert it.
            sql_insert_card(card_data)
            
        #Check to see if the card has already been added to tcf_inventory.
        result = sql_select_inventory(card_data)
        if(len(result) == 0):
        #If the inventory_id doesn't exist, insert it.
            sql_insert_inventory(card_data)
            
        #Check to see if there is more than 1 player_id.
        for index in range(0, len(card_data['player_id'])):
            #Check to see if the player has already been added.
            result = sql_select_player(card_data, index)
            #If the player doesn't exist, insert it into tcf_player.
            if(len(result) == 0):
                sql_insert_player(card_data, index)
            #Check to see if the card_player has already been added.
            result = sql_select_card_player(card_data, index)
            #If the card_player doesn't exist, insert it.
            if(len(result) == 0):
                sql_insert_card_player(card_data, index)

        #Check to see if there is more than 1 team_id.
        for index in range(0, len(card_data['team_id'])):
            #Check to see if the team has already been added.
            result = sql_select_team(card_data, index)
            #If the team doesn't exist, insert it into tcf_team.
            if(len(result) == 0):
                sql_insert_team(card_data, index)
            #Check to see if the card_team has already been added.
            result = sql_select_card_team(card_data, index)
            #If the card_team doesn't exist, insert it into tcf_card_team.
            if(len(result) == 0):
                sql_insert_card_team(card_data, index)
                
        #Check to see if there is more than 1 attribute_name.
        for index in range(0, len(card_data['attribute_name'])):
            #Check to see if the attribute has already been added.
            result = sql_select_attribute(card_data, index)
            #If the attribute doesn't exist, insert it into tcf_attribute.
            if(len(result) == 0):
                sql_insert_attribute(card_data, index)
                #Get the attribute_id just created.
                result = sql_select_attribute(card_data, index)
                card_data['attribute_id'] = result[0][0]
                #Check to see if the card_attribute has already been added.
                result = sql_select_card_attribute(card_data, index)
                #If the card_attribute doesn't exist, insert it.
                if(len(result) == 0):
                    sql_insert_card_attribute(card_data, index)
            else:
                card_data['attribute_id'] = result[0][0]
                #Check to see if the card_attribute has already been added.
                result = sql_select_card_attribute(card_data, index)
                #If the card_attribute doesn't exist, insert it.
                if(len(result) == 0):
                    sql_insert_card_attribute(card_data, index)
    except IndexError as err:
        print('Something went wrong: {}'.format(err))


def get_card_id(url: str, card_data: dict, page_num: int) -> dict:
    try:
        #Make the soup.
#function call---------------------------------------------------------------->
        soup = request_page(url)
        #Find the link with the set_id.
        a_list = soup.find_all(href=re.compile('\?set_id='))
#debugging-------------------------------------------------------------------->
        if debugging:
            print('url:', a_list[0]['href'])
        #Save the set_url and set_id.
        card_data['set_url'] = a_list[0]['href']
        temp_list = card_data['set_url'].split('set_id=')
        temp_list = temp_list[1].split('&')
        card_data['set_id'] = temp_list[0]
#debugging-------------------------------------------------------------------->
        if debugging:
            print(card_data['set_id'])
        #Request the set page.
        soup = request_page(a_list[0]['href'])
        #Create a string to match the href attribute.
        temp_str = (card_data['temp_year_name'] + '/'
                    + card_data['temp_set_name'].replace(' ', '-').lower()
                    + '/' + card_data['temp_card_number'].lower() + '-')
        temp_list = []
        while len(temp_list) == 0 and page_num < 101:
            #Find the link with the card_id.
            temp_list = soup.find_all(href=re.compile(temp_str))
#debugging-------------------------------------------------------------------->
            if debugging:
                print(temp_str)
                print(len(temp_list), 'matches were found for the card')
            #If found, save the card_url and card_id.
            if len(temp_list) == 1:
                #Save the link.
                card_data['card_url'] = temp_list[0]['href']
                #Get the card_id
                temp_list = temp_list[0]['href'].split('-')
                card_data['card_id'] = temp_list[-1]
                return card_data
            #If not found, check the next page if available.
            elif len(temp_list) == 0 and card_data['card_url'] == '':
                page_num += 1
                #Create the url for the next page.
                temp_url = (a_list[0]['href'] + '&rowNum=25&page='
                            + str(page_num))
            #If more than one is found there is a problem.
            elif len(temp_list) > 1:
                #Print the link.
                print(temp_str)
                temp_str = str(len(temp_list))
                temp_str += (' cards have the same number! '
                             'Which one should we use?')
                index = int(input(temp_str))
                #Save the link.
                card_data['card_url'] = temp_list[index]['href']
                print(card_data['card_url'])
                #Get the card_id
                temp_list = temp_list[index]['href'].split('-')
                card_data['card_id'] = temp_list[-1]
                print(card_data['card_id'])
                return card_data
            #Request the next page.
            soup = request_page(temp_url)
    except IndexError as err:
        print('Something went wrong: {}'.format(err))


def get_card_url(card_soup: 'BeautifulSoup', card_data: dict) -> dict:
    #Find the list that contains more card_data.
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
            #Find and save the set link.
            a_list = row.find_all('a')
            set_name_link = a_list[0]['href']
            #Get the year from the link.
            temp_list = set_name_link.split('/')
            card_data['set_year'] = temp_list[-3]
            #Remove the year from the temp_str and save as set_name.
            temp_str = temp_str.replace(card_data['set_year'], '', 1)
            card_data['set_name'] = temp_str.strip()
        if 'Card Number:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Card Number:', '').strip()
            card_data['card_number'] = temp_str
        if 'Other Attributes:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Other Attributes:', '').strip()
            temp_str = temp_str.replace('(', '').strip()
            temp_str = temp_str.replace(')', '').strip()
            temp_list = temp_str.split(',')
            for row in temp_list:
                card_data['attribute_name'].append(row.strip())
        if 'Attributes:' in temp_str:
            #Find the links with the attribute_name.
            a_list = row.find_all('a')
            for entry in a_list:
                temp_str = entry.text.strip()
                temp_str = temp_str.replace('(', '').strip()
                temp_str = temp_str.replace(')', '').strip()
                card_data['attribute_name'].append(entry.text)
        if 'Print Run:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Print Run:', '').strip()
            card_data['print_run'] = temp_str
        if 'Player:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Player:', '').strip()
            #Check to see if more than one player is listed.
            a_list = row.find_all('a')
            for entry in a_list:
                card_data['player_url'].append(entry['href'])
                #Get the official player_name.
#function call---------------------------------------------------------------->
                card_soup = request_page(entry['href'])
#function call---------------------------------------------------------------->
                card_data = get_player_name(card_soup, card_data)
                temp_list = entry['href'].split('-')
                temp_str = temp_list[-1]
                card_data['player_id'].append(temp_str)
    #Update the card_name field.
    temp_str = card_data['card_name']
    temp_str = temp_str.replace(card_data['set_year'], '', 1).strip()
    temp_str = temp_str.replace(card_data['set_name'], '', 1).strip()
    temp_str = temp_str.replace(card_data['card_number'], '', 1).strip()
    card_data['card_name'] = temp_str
#debugging-------------------------------------------------------------------->
    if debugging:
        print(card_data)
    return card_data


def get_inventory_url(card_soup: 'BeautifulSoup', card_data: dict) -> dict:
    #Get the image links.
    temp_img = card_soup.find_all(id='item_image_front')
    card_data['image_src_front'] = temp_img[0]['src']
    temp_img = card_soup.find_all(id='item_image_back')
    card_data['image_src_back'] = temp_img[0]['src']
    #Get the span that contains the price data.
    try:
        div_list = card_soup.find_all('div', 'price-div')
        for row in div_list:
            #Strip and save the innerHtml.
            temp_str = row.text.strip()
            if 'Price:' in temp_str:
                #Remove the title and discount rate.
                temp_str = temp_str.replace('Price:', '').strip()
                temp_str = temp_str.replace('xx% off Beckett Value', '')
                temp_str = temp_str.strip()
                #Check to see if a Canadian price is present.
                if 'CAD' in temp_str:
                    temp_list = temp_str.split('CAD')
                    card_data['price'] = float(temp_list[0].replace('$', ''))
                else:
                    card_data['price'] = float(temp_str.replace('$', ''))
                    break
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
    #Get the div that contains the grade data.
    try:
        div_list = card_soup.find_all('div', 'condition')
        for row in div_list:
            #Strip and save the innerHtml.
            temp_str = row.text.strip()
            if 'Condition:' in temp_str:
                #Remove the title.
                temp_str = temp_str.replace('Condition:', '').strip()
                card_data['condition'] = temp_str
                break
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
    #Get the h4 that contains quantity data.
    try:
        h4_list = card_soup.find_all('h4', 'lineheight-34')
        for row in h4_list:
            #Strip and save the innerHtml.
            temp_str = row.text.strip()
            if 'Qty Available: ' in temp_str:
                temp_str = temp_str.replace('Qty Available:', '').strip()
                card_data['quantity'] = temp_str
                card_data['max'] = temp_str
                break
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
    #Get the sport, team, brand, and manufaturer.
    try:
        li_list = card_soup.find_all('li')
        for row in li_list:
            #Strip and save the innerHtml.
            temp_str = row.text.strip()
            #Get the category_name and category_id.
            if 'Sport:' in temp_str:
                temp_str = temp_str.replace('Sport:', '').strip()
                #Check to see if more than one category is listed.
                temp_list = temp_str.split(',')
                card_data['category_name'] = temp_list
                a_list = row.find_all('a')
                for entry in a_list:
                    card_data['category_url'].append(entry['href'])
                    temp_list = entry['href'].split('=')
                    temp_str = temp_list[len(temp_list) - 1]
                    card_data['category_id'].append(temp_str)
            #Get the team_name and team_id.
            if 'Team:' in temp_str:
                temp_str = temp_str.replace('Team:', '').strip()
                #Check to see if more than one team is listed.
                temp_list = temp_str.split(',')
                card_data['team_name'] = temp_list
                a_list = row.find_all('a')
                for entry in a_list:
                    card_data['team_url'].append(entry['href'])
                    temp_list = entry['href'].split('=')
                    temp_str = temp_list[len(temp_list) - 1]
                    card_data['team_id'].append(temp_str)
            #Get the brand info.
            if 'Brand:' in temp_str:
                temp_str = temp_str.replace('Brand:', '').strip()
                #Check to see if more than one brand is listed.
                temp_list = temp_str.split(',')
                card_data['brand_name'] = temp_list
                a_list = row.find_all('a')
                for entry in a_list:
                    card_data['brand_url'].append(entry['href'])
                    temp_list = entry['href'].split('=')
                    temp_str = temp_list[len(temp_list) - 1]
                    card_data['brand_id'].append(temp_str)
            #Get the manufacturer info.
            if 'Manufacturer:' in temp_str:
                temp_str = temp_str.replace('Manufacturer:', '').strip()
                #Check to see if more than one brand is listed.
                temp_list = temp_str.split(',')
                card_data['manufacturer_name'] = temp_list
                a_list = row.find_all('a')
                for entry in a_list:
                    card_data['manufacturer_url'].append(entry['href'])
                    temp_list = entry['href'].split('=')
                    temp_str = temp_list[len(temp_list) - 1]
                    card_data['manufacturer_id'].append(temp_str)
                break
        return card_data
    except IndexError as err:
        print('Something went wrong: {}'.format(err))


def get_page_links(soup: 'BeautifulSoup') -> dict:
    #Create a dictionary to store return values.
    page_links = {'next_page_link': '', 'last_page_link': '',
                  'next_page_num': 1, 'last_page_num': 1, 'records': ''}
    try:
        #Find the total number of records.
        temp_str = soup.find(string=re.compile('Showing records '))
        temp_list = temp_str.split('of')
        page_links['records'] = int(temp_list[-1].strip())
#debugging-------------------------------------------------------------------->
        if debugging:
            print(page_links['records'], 'records were found.')        
        #Find the li element that holds the next page button.
        li_list = soup.find_all('li', 'next')
        if li_list != 0:
            #Find the a element that holds the next page link.
            a_list = li_list[0].find_all('a')
            page_links['next_page_link'] = a_list[0]['href']
            #Get the next page number.
            temp_list = page_links['next_page_link'].split('=')
            page_links['next_page_num'] = int(temp_list[-1])
        #Find the li element that holds the last page button.
        li_list = soup.find_all('li', 'last')
        if li_list != 0:
            #Get the a element that holds the last page link.
            a_list = li_list[1].find_all('a')
            page_links['last_page_link'] = a_list[0]['href']
            #Get the last page number.
            temp_list = page_links['last_page_link'].split('=')
            page_links['last_page_num'] = int(temp_list[-1])
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
    return page_links


def get_player_name(card_soup: 'BeautifulSoup', card_data: dict) -> dict:
    class_name = 'pull-left paddingLeft10'
    #Get the official player_name.
    try:
        div_list = card_soup.find_all('div', class_name)
        temp_str = div_list[0].text.strip()
        card_data['player_name'].append(temp_str)
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
    return card_data


def search_dealer_home(soup: 'BeautifulSoup'):
    #Get all the card names that are displayed.
    try:
        li_list = soup.find_all('li', 'title')
        #For each card, get the card_name, inventory_url, and inventory_id.
        for i in range(card_start - 1, card_end):
            #Create a dictionary to store return values.
            card_data = {'brand_id': list(), 'brand_name': list(),
                         'brand_url': list(),
                         'category_id': list(), 'category_name': list(),
                         'category_url': list(),
                         'manufacturer_id': list(),
                         'manufacturer_name': list(),
                         'manufacturer_url': list(),
                         'player_id': list(), 'player_name': list(),
                         'player_url': list(),
                         'team_id': list(), 'team_name': list(),
                         'team_url': list(),
                         'set_id': '', 'set_year': '', 'set_name': '',
                         'card_id': '', 'card_number': '', 'card_name': '',
                         'value_low': 0, 'value_high': 0,
                         'inventory_id': '', 'condition': '', 'quantity': '',
                         'min': 1, 'max': '', 'price': 0,
                         'attribute_name': list(), 'print_run': 0,
                         'card_url': '', 'inventory_url': ''
                         }
            print('Card#:', i + 1)
            #Find the a element that contains the inventory_url.
            a_list = li_list[i].find_all('a')
            #Save the link.
            card_data['inventory_url'] = a_list[0]['href']
            #Get the inventory_id from the link.
            temp_list = card_data['inventory_url'] .split('_')
            card_data['inventory_id'] = temp_list[-1]
            #Save the unformatted card_name.
            card_data['card_name'] = a_list[0].text.strip()
            #Save the set_name, set_year, and card_number.
            temp_list = card_data['card_name'].split('#')
            temp_list2 = temp_list[0].split(' ')
            card_data['temp_year_name'] = temp_list2[0]
            temp_str = ' '.join(temp_list2[1:]).strip()
            card_data['temp_set_name'] = temp_str.replace("'", '')
            temp_list3 = temp_list[1].split(' ')
            card_data['temp_card_number'] = temp_list3[0]
            #Request the inventory_url page.
#function call---------------------------------------------------------------->
            card_soup = request_page(card_data['inventory_url'])
#function call---------------------------------------------------------------->
            card_data = get_inventory_url(card_soup, card_data)
            #Check to see if the card has been added to tcf_inventory.
            result = sql_select_inventory(card_data)
            #If the inventory_id is found, update the quantity and price.
            if len(result) == 1:
                sql_update_inventory(card_data)
            #If the inventory_id is not found, get the card_id.
            elif len(result) == 0:
                #Create a page number to ensure that the card_id is found.
                page_num = 1
                #Create a url for the set page.
                url = ('https://www.beckett.com/'
                       + card_data['category_name'][0].lower() + '/'
                       + card_data['temp_year_name'] + '/'
                       + card_data['temp_set_name'].replace(' ', '-').lower()
                       + '/')
#debugging-------------------------------------------------------------------->
                if debugging:
                    print('debugging-->', url, '\ndebugging\n')
#function call---------------------------------------------------------------->
                #Get the set_id and card_id.
                card_data = get_card_id(url, card_data, page_num)
                #Get more information from the card_url.
#function call---------------------------------------------------------------->
                card_soup = request_page(card_data['card_url'])
#function call---------------------------------------------------------------->
                card_data = get_card_url(card_soup, card_data)
                #Add the card_data to the appropriate table.
#function call---------------------------------------------------------------->
                add_card_data(card_data)
            elif len(result) > 1:
                temp_str = 'More than one record was found for inventory_id: '
                temp_str += card_data['inventory_id'] + '.'
                print(temp_str)
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
        print(len(li_list), 'li elements with className="title" were found.')
        print(len(a_list), 'a elements were found in li element #:', i, '.')


def search_for_term(location: str, search_str: str, page_str: str):
    #Create the url to search.
    url = (location + search_str + page_str)
#function call---------------------------------------------------------------->
    soup = request_page(url)
    #Get the next and last page links.
#function call---------------------------------------------------------------->
    page_links = get_page_links(soup)
    if page_links['records'] > 10000:
        print('This search will need to be refined.')
        print('There are more than 10,000 records.')
    #Cycle through the pages and scrape each page.
    for x in range(page - 1, page_links['last_page_num']):
        print('Page', x + 1)
        #Set the default currency.
        set_currency()
#function call---------------------------------------------------------------->
        search_dealer_home(soup)
        if not(x == page_links['last_page_num'] - 1):
#function call---------------------------------------------------------------->
            soup = request_page(page_links['next_page_link'])
#function call---------------------------------------------------------------->
            page_links = get_page_links(soup)


def request_page(url: str) -> 'BeautifulSoup':
    try:
        #Get the page requested.
        r = requests.get(url)
        #Save the content.
        c = r.content
        #Parse the content.
        return BeautifulSoup(c, 'lxml')
    except requests.Timeout as err:
        print('Something went wrong: {}'.format(err))


def set_currency():
    url = ('https://www.beckett.com/home/update_currency_country')
    payload = {'currency': '1'}
    try:
        r = requests.post(url, data=payload)
        print(r.status_code)
        #Save the content.
        c = r.content
        #Parse the content.
        soup = BeautifulSoup(c, 'lxml')
        #Check the active currency.
        span_list = soup.find_all('span', 'currency')
        print('Currency:', span_list[0].text)
        if(span_list[0].text != 'USD'):
            print('The default currency should be USD.')
    except requests.Timeout as err:
        print('Something went wrong: {}'.format(err))


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

#Global variables.
year = 2017
page = 17
card_start = 1
card_end = 100
debugging = False
#debugging = True
#TCF marketplace dealer home.
dealer_home = ('https://marketplace.beckett.com/thecollectorsfriend_700/'
               'search_new/')
#Beckett Pricing/Checklists.
beckett_home = ('https://www.beckett.com/search/')
#search_str = ('?attr=RC')#All rookie cards.
#search_str = ('?result_type=59')#First 10,000 items.
#search_str = ('?result_type=59&NewlyMPAdded=1')#Newly added items.
#search_str = ('?term=')#Specific search term.
search_str = ('?term=' + str(year))#Specific year.
page_str = ('&page=' + str(page))

#Start the search.
search_for_term(dealer_home, search_str, page_str)
        
cursor.close()
cnx.close()
print('All records have been updated.')