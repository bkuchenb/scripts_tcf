# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 2017

@author: bk00chenb
"""

import MySQLdb
import requests
import re
from bs4 import BeautifulSoup

def sql_insert_brand(card_data, index):
#Add the item if the number of ids and names matches.
    if(len(card_data['brand_id']) != len(card_data['brand_name'])):
        exception_list.append('The number of ids and names doesn\'t match.')
        return
    insert = ("INSERT INTO tcf_brand(brand_id, brand_name) "
              "VALUES({brand_id[" + str(index) + "]}, "
              "{brand_name[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the statement.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))
def sql_insert_card(card_data):
    insert = ("INSERT INTO tcf_card"
              "(card_id, set_id, card_number, card_name, "
              "image_src_back, image_src_front, "
              "value_high, value_low, print_run) "
              "VALUES({card_id}, {set_id}, {card_number!r}, "
              "{card_name!r}, {image_src_back!r}, {image_src_front!r}, "
              "{value_high}, {value_low}, {print_run})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))
def sql_insert_card_attribute(card_data, index):
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
def sql_insert_card_player(card_data, index):
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
def sql_insert_card_team(card_data, index):
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
def sql_insert_category(card_data, index):
    insert = ("INSERT INTO tcf_category(category_id, category_name) "
              "VALUES({category_id[" + str(index) + "]}, "
              "{category_name[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))
def sql_insert_inventory(card_data):
    insert = ("INSERT INTO tcf_inventory(inventory_id, card_id, grade, "
              "quantity, max, min, price) "
              "VALUES({inventory_id}, {card_id}, {condition!r}, "
              "{quantity}, {max}, {min}, {price})")
#debugging-------------------------------------------------------------------->
    print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))
def sql_insert_manufacturer(card_data, index):
    #Add the item if the number of ids and names matches.
    if(len(card_data['manufacturer_id']) != len(card_data['manufacturer_name'])):
        exception_list.append('The number of ids and names doesn\'t match.')
        return
    insert = ("INSERT INTO tcf_manufacturer"
              "(manufacturer_id, manufacturer_name) "
              "VALUES({manufacturer_id[" + str(index) + "]}, "
              "{manufacturer_name[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the statement.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))
def sql_insert_player(card_data, index):
    #Add the item if the number of ids and names matches.
    if(len(card_data['player_id']) != len(card_data['player_name'])):
        exception_list.append('The number of ids and names doesn\'t match.')
        return
    insert = ("INSERT INTO tcf_player(player_id, player_name) "
              "VALUES({player_id[" + str(index) + "]}, "
              "{player_name[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))
def sql_insert_set(card_data):
    #Add the set to tcf_set if there is only one manufacturer and one brand.
    if(len(card_data['manufacturer_id']) > 1
       or len(card_data['brand_id']) > 1):
        exception_list.append('There is more than 1 manufacturer or brand id.')
        return
    insert = ("INSERT INTO tcf_set"
              "(set_year, set_name, manufacturer_id, brand_id) "
              "VALUES({set_year!r}, {set_name!r}, "
              "{manufacturer_id[0]}, {brand_id[0]})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))
def sql_insert_set_category(card_data, index):
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
def sql_insert_team(card_data, index):
    #Add the item if the number of ids and names matches.
    if(len(card_data['team_id']) != len(card_data['team_name'])):
        exception_list.append('The number of ids and names doesn\'t match.')
        return
    insert = ("INSERT INTO tcf_team(team_id, team_name) "
              "VALUES({team_id[" + str(index) + "]}, "
              "{team_name[" + str(index) + "]!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**card_data))
    try:
        cursor.execute(insert.format(**card_data))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the query.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**card_data))
def sql_select_attribute(card_data, index):
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
def sql_select_brand(card_data, index):
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
def sql_select_card(card_data):
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
def sql_select_card_attribute(card_data, index):
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
def sql_select_card_player(card_data, index):
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
def sql_select_card_team(card_data, index):
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
def sql_select_category(card_data, index):
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
def sql_select_inventory(card_data):
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
def sql_select_manufacturer(card_data, index):
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
def sql_select_player(card_data, index):
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
def sql_select_set(card_data, index):
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
def sql_select_set_category(card_data, index):
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
def sql_select_set_id():
    select = ("SELECT set_id FROM tcf_set ORDER BY set_id DESC LIMIT 1")
    cursor.execute(select)
    result = cursor.fetchone()[0]
#debugging-------------------------------------------------------------------->
    #print(result)
    return result
def sql_select_team(card_data, index):
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
def sql_update_inventory(card_data):
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
def add_card_data(card_data):
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
                #Get the set_id just created.
                result = sql_select_set_id()
                card_data['set_id'] = result
            #If only 1 set was found update the card_data field.
            elif(len(result) == 1):
                card_data['set_id'] = result[0][0]
            #If more than 1 set was found log an exception.
            elif(len(result) > 1):
                temp_str = ('More than 1 set: ' + card_data['set_name']
                + ' was found.')
                exception_list.append(temp_str)
                
            #Check to see if the set_category has already been added.
            result = sql_select_set_category(card_data, index)
            #If the set_category doesn't exist, insert it.
            if(len(result) == 0):
                sql_insert_set_category(card_data, index)
        
        #Check to see if the card has already been added to tcf_card.
        result = sql_select_card(card_data)
        if(len(result) == 0):
            sql_insert_card(card_data)
            
        #Add the card to tcf_inventory.
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
            #If the card_player doesn't exist, insert it into tcf_card_player.
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
            #If the attribute doesn't exist, log an exception.
            if(len(result) == 0):
                exception_list.append(card_data['attribute_name'][index])
            else:
                card_data['attribute_id'] = result[0][0]
                #Check to see if the card_attribute has already been added.
                result = sql_select_card_attribute(card_data, index)
                #If the card_attribute doesn't exist, insert it.
                if(len(result) == 0):
                    sql_insert_card_attribute(card_data, index)
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
def get_card_id(url, card_data, page_num):
    try:
#function call---------------------------------------------------------------->
        #Make the soup.
        card_soup = request_page(url)
        #Create a string to search the href for a matching value.
        temp_list = card_data['card_name'].split('#')
        temp_str = temp_list[0].replace(' ', '/', 1)
        temp_str = temp_str.replace(' ', '-') + '/'
        temp_str += temp_str[1].replace(' ', '-')
        print(temp_str)
        #Get the a element with the card_id.
        temp_a = card_soup.find_all(href=re.compile(temp_str))
        print(len(temp_a))
        if(len(temp_a) == 1):
            #Save the link.
            card_data['card_id_url'] = temp_a[0]['href']
            #Get the card_id
            temp_list = temp_a[0]['href'].split('-')
            card_data['card_id'] = temp_list[len(temp_list) - 1]
            return card_data
        #If the card was not found, check the next page if available.
        elif(card_data['card_id_url'] == '' and page_num < 5):
            page_num += 1
            temp_url = url + '&rowNum=25&page=' + str(page_num)
            print(url)
            card_data = get_card_id(temp_url, card_data, page_num)
            return card_data
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
def get_card_id_url(card_soup, card_data):
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
        if 'Other Attributes:' in temp_str:
            temp_str = temp_str.replace('Other Attributes:', '').strip()
            temp_str = temp_str.replace('(', '').strip()
            temp_str = temp_str.replace(')', '').strip()
            card_data['attribute_name'].append(temp_str)
        if 'Attributes:' in temp_str:
            #Get the links with the attribute_name.
            a_list = row.find_all('a')
            for entry in a_list:
                temp_str = entry.text.strip()
                temp_str = temp_str.replace('(', '').strip()
                temp_str = temp_str.replace(')', '').strip()
                card_data['attribute_name'].append(entry.text)
        if 'Print Run:' in temp_str:
            temp_str = temp_str.replace('Print Run:', '').strip()
            card_data['print_run'] = temp_str
        if 'Player:' in temp_str:
            #Remove the title.
            temp_str = temp_str.replace('Player:', '').strip()
            #Check to see if more than one player is listed.
            a_list = row.find_all('a')
            for entry in a_list:
                temp_str = entry['href']
                #Get the official player_name.
#function call---------------------------------------------------------------->
                card_soup = request_page(temp_str)
#function call---------------------------------------------------------------->
                card_data = get_player_name(card_soup, card_data)
                temp_list = temp_str.split('-')
                temp_str = temp_list[len(temp_list) - 1]
                card_data['player_id'].append(temp_str)
    #Update the card_name field.
    temp_str = card_data['card_name']
    temp_str = temp_str.replace(card_data['set_year'], '', 1).strip()
    temp_str = temp_str.replace(card_data['set_name'], '', 1).strip()
    temp_str = temp_str.replace(card_data['card_number'], '', 1).strip()
    card_data['card_name'] = temp_str
#debugging-------------------------------------------------------------------->
    #print(card_data)
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
def get_inventory_id_url(card_soup, card_data):
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
                temp_str = temp_str.replace('xx% off Beckett Value', '').strip()
                card_data['price'] = float(temp_str.replace('$', ''))
                break
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
        exception_list.append(str(len(div_list)) + ' div elements with '
        'className="price-div" were found.')
    #Get the div that contains the grade data.
    try:
        div_list = card_soup.find_all('div', 'condition')
        for row in div_list:
            #Strip and save the innerHtml.
            temp_str = row.text.strip()
            if 'Condition:' in temp_str:
                #Remove the title.
                card_data['condition'] = temp_str.replace('Condition:', '').strip()
                break
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
        exception_list.append(str(len(div_list)) + ' div elements with '
        'className="condition" were found.')
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
        exception_list.append(str(len(h4_list)) + ' h4 elements with '
        'className="lineheight-34" were found.')
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
                    temp_str = entry['href']
                    temp_list = temp_str.split('=')
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
                    temp_str = entry['href']
                    temp_list = temp_str.split('=')
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
                    temp_str = entry['href']
                    temp_list = temp_str.split('=')
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
                    temp_str = entry['href']
                    temp_list = temp_str.split('=')
                    temp_str = temp_list[len(temp_list) - 1]
                    card_data['manufacturer_id'].append(temp_str)
                break
        return card_data
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
        exception_list.append(str(len(div_list)) + ' li elements were found.')
        exception_list.append(str(len(a_list)) + ' a elements were found '
        'in the li element.')
def get_page_links(soup):
    #Create a dictionary to store return values.
    page_links = {}
    try:
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
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
        exception_list.append(str(len(li_list)) + ' li elements with '
        'className="next" were found.')
        exception_list.append(str(len(a_list)) + ' a elements were found '
        'in the first li element.')
        exception_list.append(str(len(li_list2)) + ' li elements with '
        'className="last" were found.')
        exception_list.append(str(len(a_list2)) + ' a elements were found '
        'in the first li element.')
def get_player_name(card_soup, card_data):
    class_name = 'pull-left paddingLeft10'
    #Get the official player_name.
    try:
        div_list = card_soup.find_all('div', class_name)
        temp_str = div_list[0].text.strip()
        card_data['player_name'].append(temp_str)
    except IndexError as err:
        print('Something went wrong: {}'.format(err))
        exception_list.append(str(len(div_list)) + ' div elements with '
        'className="pull-left paddingLeft10" were found.')
    return card_data
def get_tcf_dealer_home_search(soup):
    #Get all the card names that are displayed.
    try:
        li_list = soup.find_all('li', 'title')
        #For each card, get the card_name, inventory_id_url, and inventory_id.
        for i in range(0, len(li_list)):
            #Create a dictionary to store return values.
            card_data = {'brand_id': list(), 'brand_name': list(),
                         'category_id': list(), 'category_name': list(),
                         'manufacturer_id': list(),
                         'manufacturer_name': list(),
                         'player_id': list(), 'player_name': list(),
                         'team_id': list(), 'team_name': list(),
                         'set_id': '', 'set_year': '', 'set_name': '',
                         'card_id': '', 'card_number': '', 'card_name': '',
                         'value_low': 0, 'value_high': 0,
                         'inventory_id': '', 'condition': '', 'quantity': '',
                         'min': 1, 'max': '', 'price': 0,
                         'attribute_name': list(), 'print_run': 0,
                         'card_id_url': ''
                         }
            print('Card#:', i + 1)
            #Get the a element that contains the inventory_id_url.
            a_list = li_list[i].find_all('a')
            #Save the link.
            inventory_id_url = a_list[0]['href']
            #Save the unformatted card_name.
            card_data['card_name'] = a_list[0].text
            #Get the inventory_id from the link.
            temp_list = inventory_id_url.split('_')
            card_data['inventory_id'] = temp_list[len(temp_list) - 1]
            #Get the inventory_id_url page.
#function call---------------------------------------------------------------->
            card_soup = request_page(inventory_id_url)
#function call---------------------------------------------------------------->
            card_data = get_inventory_id_url(card_soup, card_data)
            #Check to see if the card has been added to tcf_inventory.
            result = sql_select_inventory(card_data)
            #If the inventory_id is found, update the quantity and price.
            if len(result) == 1:
                sql_update_inventory(card_data)
            #If the card is not found, get the card_id.
            elif len(result) == 0:
                #Create a link to search for the page that contains the card_id.
                temp_str = card_data['card_name'].replace(' ', '+')
                #Format temp_str for web address.
                temp_str = temp_str.replace('#', '%23')
                temp_str = temp_str.replace('/', '%2F')
                temp_list = card_data['card_name'].split(' ')
                #Create a page number to ensure that the card_id is found.
                page_num = 1
                url = ('https://www.beckett.com/search/?term='
                       + temp_str + '&year_start=' + temp_list[0])
#function call---------------------------------------------------------------->
                #Get the card_id.
                card_data = get_card_id(url, card_data, page_num)
                #Get more information from the card_id_url.
#function call---------------------------------------------------------------->
                card_soup = request_page(card_data['card_id_url'])
#function call---------------------------------------------------------------->
                card_data = get_card_id_url(card_soup, card_data)
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
def request_page(url):
    try:
        #Get the page requested.
        r = requests.get(url)
        #Save the content.
        c = r.content
        #Parse the content.
        return BeautifulSoup(c, 'lxml')
    except requests.Timeout as err:
        print('Something went wrong: {}'.format(err))
        exception_list.append(url)
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
        exception_list.append(url)
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

#Create a list to hold exceptions.
exception_list = list()

# page = 29
# #Go to the tcf marketplace page and search newly added items.
# url = ('https://marketplace.beckett.com/thecollectorsfriend_700/'
       # 'search_new/?result_type=59&NewlyMPAdded=1&page=' + str(page))
# #Override for first 10,000 items.
# page = 33
# #Go to the tcf marketplace page and search all items.
# url = ('https://marketplace.beckett.com/thecollectorsfriend_700/'
       # 'search_new/?result_type=59&page=' + str(page))

#Override for rookie cards.
page = 1
#Go to the tcf marketplace page and search all rookie cards.
url = ('https://marketplace.beckett.com/thecollectorsfriend_700/'
       'search_new/?attr=RC')
       
#Get the first page.
#function call---------------------------------------------------------------->
soup = request_page(url)
#Get the next and last page links.
#function call---------------------------------------------------------------->
page_links = get_page_links(soup)
#Cycle through the pages and scrape each page.
for x in range(page - 1, page_links['last_page_num']):
# for x in range(page - 1, 1):
    print('Page', x + 1)
    #Set the default currency.
    set_currency()
#function call---------------------------------------------------------------->
    get_tcf_dealer_home_search(soup)
    if not(x == page_links['last_page_num'] - 1):
#function call---------------------------------------------------------------->
        soup = request_page(page_links['next_page_link'])
        print(page_links['next_page_link'])
#function call---------------------------------------------------------------->
        page_links = get_page_links(soup)
        
cursor.close()
cnx.close()
print('Exceptions---->')
print(exception_list)
print('All records have been updated.')