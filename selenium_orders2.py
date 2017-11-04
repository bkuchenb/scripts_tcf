# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:29:02 2016

@author: Brendan
"""

import datetime
import time

import MySQLdb
import pprint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def sql_insert_customer(temp_dict: dict):           
#Add the customer.
    insert = ("INSERT INTO tcf_customer"
              "(email_address, first_name, last_name, phone_number, "
              "shipping_address) "
              "VALUES({email_address!r}, {first_name!r}, {last_name!r}, "
              "{phone_number!r}, {shipping_address!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**temp_dict))
    try:
        cursor.execute(insert.format(**temp_dict))
        cnx.commit()
        #Print a message indicating all cards were added.
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the statement.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**temp_dict))


def sql_insert_order(temp_dict: dict):           
#Add the order.
    insert = ("INSERT INTO tcf_order"
              "(order_id, email_address, order_date, order_time, "
              "shipping, tax, total, order_url) "
              "VALUES({order_id}, {email_address!r}, {order_date}, "
              "{order_time}, {shipping}, {tax}, {total}, {order_url!r})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**temp_dict))
    try:
        cursor.execute(insert.format(**temp_dict))
        cnx.commit()
        print('Order', temp_dict['order_id'],
              'was added to the tcf_order table.')
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the statement.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**temp_dict))


def sql_insert_order_detail(temp_dict: dict):           
#Add the order_detail.
    insert = ("INSERT INTO tcf_order_detail"
              "(order_id, inventory_id, quantity) "
              "VALUES({order_id}, {inventory_id!r}, {quantity})")
#debugging-------------------------------------------------------------------->
    #print(insert.format(**temp_dict))
    try:
        cursor.execute(insert.format(**temp_dict))
        cnx.commit()
    except MySQLdb.Error as err:
        #If the insert fails, print a message and the statement.
        print('Something went wrong: {}'.format(err))
        print(insert.format(**temp_dict))


def sql_select_customer(temp_dict: dict) -> list:
    select = ("SELECT email_address, shipping_address "
              "FROM tcf_customer "
              "WHERE email_address = {email_address!r}")
#debugging-------------------------------------------------------------------->
    #print(select.format(**temp_dict))
    cursor.execute(select.format(**temp_dict))
    #If the email was found, print a message.
    if cursor.rowcount == 1:
        print(temp_dict['first_name'], temp_dict['last_name'],
              'has already been added.')
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return cursor.fetchall()


def sql_select_order(temp_dict: dict) -> int:
    select = "SELECT * FROM tcf_order WHERE order_id = {order_id}"
#debugging-------------------------------------------------------------------->
    #print(select.format(**temp_dict))
    cursor.execute(select.format(**temp_dict))
    #If the order_id was found, print a message.
    if cursor.rowcount == 1:
        print('Order', temp_dict['order_id'],
              'has already been added.')
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return cursor.rowcount


def sql_select_order_detail(temp_dict: dict) -> list:
    select = "SELECT * FROM tcf_order_detail WHERE order_id = {order_id}"
#debugging-------------------------------------------------------------------->
    #print(select.format(**temp_dict))
    cursor.execute(select.format(**temp_dict))
    #If the order_id was found, print a message.
    if cursor.rowcount > 0:
        if cursor.rowcount == 1:
            print('1 card was already added for order',
                  temp_dict['order_id'] + '.')
        else:
            print(cursor.rowcount, 'cards were already added for order',
                  temp_dict['order_id'] + '.')
#debugging-------------------------------------------------------------------->
    #print(len(result), 'record(s) were found.')
    return cursor.fetchall()


#Connect to inceff database.
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

debugging = False
debugging = True

#Set the capabilites.
browser = webdriver.Firefox()
#Set the browser wait time to 10 seconds.
wait = WebDriverWait(browser, 10)

#Get today's date.
today = datetime.date.today()
#Get the date for 28 days ago.
start_date = today - datetime.timedelta(days = 28)
#Get yesterday's date.
end_date = today - datetime.timedelta(days = 1)
#Save the two dates as strings.
start_date = start_date.strftime("%m/%d/%y")
end_date = end_date.strftime("%m/%d/%y")
#start_date = '04/01/2017'
#end_date = '10/4/2016'

#Open the Beckett admin page.
browser.get('https://www.beckett.com/login')
#Find the loginEmail text box.
login_email = browser.find_element_by_id('loginEmail')
#Enter loginEmail.
login_email.send_keys('dialcard@nycap.rr.com')
#Find the loginPassword text box.
login_password = browser.find_element_by_id('loginPassword')
#Enter the loginPassword.
login_password.send_keys('ruthmick')
#Submit the form.
login_password.submit()
#Wait for the page to load.
time.sleep(10)
#Go to the search orders page.
browser.get('http://marketplace.beckett.com/admin/search_orders')
#Wait for the page to load.
time.sleep(10)
#Find the From Date text box.
add_date = browser.find_element_by_id('add_date')
#Enter the start_date.
add_date.send_keys(start_date)
#Find the To Date text box.
modify_date = browser.find_element_by_id('modify_date')
#Enter the end_date.
modify_date.send_keys(end_date)
#Find the filter button.
filter_btn = browser.find_element_by_id('formfilter')
#Click the filter button.
filter_btn.click()

#Wait for the page to load.
time.sleep(5)
#Find the number of pages.
pages = browser.find_element_by_id('sp_1')
if pages.text == '1':
    print(pages.text, 'page of orders was found.')
else:
    print(pages.text, 'pages of orders were found.')
#If there is more than 1 page of records, change the number displayed.
if pages.text != '1':
    #Find the drop down box.
    select = browser.find_element_by_xpath('//select[@class="ui-pg-selbox"]')
    #Save all the drop down box options.
    all_options = select.find_elements_by_tag_name('option')
    #Choose to display 100 records.
    all_options[3].click()
#Wait for the page to load.
time.sleep(10)

#Find and save all the order and customer data.
orders_table = browser.find_element_by_id('orders_table')
tbody = orders_table.find_element_by_tag_name('tbody')
tr_list = tbody.find_elements_by_tag_name('tr')
if debugging:
    print(len(tr_list), 'rows were found in the orders table.')
#Find and save all order_id(s).
temp_str = '//td[@aria-describedby="orders_table_order_id"]'
order_id_list = browser.find_elements_by_xpath(temp_str)
temp_str = '//td[@aria-describedby="orders_table_created"]'
order_date_list = browser.find_elements_by_xpath(temp_str)
#Find and save all email_addresse(s).
temp_str = '//td[@aria-describedby="orders_table_email"]'
email_address_list = browser.find_elements_by_xpath(temp_str)
#Find and save all first_name(s).
temp_str = '//td[@aria-describedby="orders_table_first_name"]'
first_name_list = browser.find_elements_by_xpath(temp_str)
#Find and save all last_name(s).
temp_str = '//td[@aria-describedby="orders_table_last_name"]'
last_name_list = browser.find_elements_by_xpath(temp_str)
#Find and save all order_url(s).
order_url_list = list()
temp_str = '//td[@aria-describedby="orders_table_actions"]'
temp_list = browser.find_elements_by_xpath(temp_str)
for row in temp_list:
    temp_a = row.find_element_by_tag_name('a')
    order_url_list.append(temp_a.get_attribute('href'))
if debugging:
    print(len(order_id_list), len(order_date_list), len(email_address_list), 
          len(first_name_list), len(last_name_list), len(order_url_list))
#Create a list to hold the order information.
order_list = list()

#Cycle through a range to get the same element for the previous lists.
for x in range(0, len(order_id_list)):
    #Create a dict to store data for a particlular order.
    temp_dict = {}
    temp_dict['order_id'] = order_id_list[x].text.strip()
    temp_dict['order_date'] = order_date_list[x].text[:10].strip()
    temp_dict['order_time'] = order_date_list[x].text[11:].strip()
    temp_dict['email_address'] = email_address_list[x].text.strip().lower()
    temp_dict['first_name'] = first_name_list[x].text.strip().title()
    temp_dict['last_name'] = last_name_list[x].text.strip().title()
    temp_dict['order_url'] = order_url_list[x]
    #Add the order info to the order list.
    order_list.append(temp_dict)

#Print a message indicating how many orders were found.
print(len(order_id_list), ' orders were found between', start_date,
      'and', end_date + '.\n')

#Check to see if the order, order_detail, and customer already exist.
for x in range(0, len(order_list)):
    #Open the order.
    browser.get(order_list[x]['order_url'])
    #Create a list to store card_data.
    card_list = list()
    #Find all the card_url links and quantities.
    desc_list = browser.find_elements_by_css_selector('td.description')
    qty_list = browser.find_elements_by_css_selector('td.qty')
    if debugging:
        print(len(desc_list), 'card_url cells were found.')
        print(len(qty_list), 'qty cells were found.')
    #Add the information to card_data.
    for i in range(0, len(qty_list)):
        #Create a dict to store the card_data.
        card_data = {}
        #Find and save the card_url.
        temp_a = desc_list[i].find_element_by_tag_name('a')
        card_data['card_url'] = temp_a.get_attribute('href')
        #Get the inventory_id from the card_url.
        temp_list = card_data['card_url'].split('_')
        card_data['inventory_id'] = temp_list[-1]
        #Save the quantity purchased.
        card_data['quantity'] = qty_list[i].text.strip()
        #Add the card_data to the card_list.
        card_list.append(card_data)
    #Find the shipping, tax, and total.
    temp_str = '//td[@colspan="2"]'
    td_list = browser.find_elements_by_xpath(temp_str)
    order_list[x]['shipping'] = float(td_list[0].text[1:])
    order_list[x]['tax'] = float(td_list[1].text[1:])
    if len(td_list) == 3:
        temp_float = float(td_list[2].text[1:])
    if len(td_list) == 4:
        temp_float = float(td_list[3].text[1:])
    temp_float -= (order_list[x]['shipping'] + order_list[x]['tax'])
    order_list[x]['total'] = temp_float

    #Find and save the phone_number.
    temp_str = '//div[@style="padding: 10px;"]'
    div_list = browser.find_elements_by_xpath(temp_str)
    temp_p = div_list[0].find_element_by_tag_name('p')
    temp_list = temp_p.text.split('Phone Number:')
    order_list[x]['phone_number'] = temp_list[-1].strip()
    #Find and save the shipping information.
    temp_p = div_list[1].find_element_by_tag_name('p')
    order_list[x]['shipping_address'] = temp_p.text
    if debugging:
        pprint.pprint(order_list[x])
        #Check to see if the order has been added.
    if sql_select_order(order_list[x]) == 0:
        sql_insert_order(order_list[x])
    #Check to see if all the cards in the order have been added.
    result = sql_select_order_detail(order_list[x])
    if debugging:
        print(len(result), 'cards found in order_details.')
        print(len(card_list), 'cards to be added.')
    #If no cards have been added, add the cards from card_list.
    if len(result) == 0:
        for row in card_list:
            sql_insert_order_detail(row)
    #If some, but not all, cards were added, add those missing.
    elif len(result) != len(card_list):
        for row in card_list:
            if row['inventory_id'] in result
            sql_insert_order_detail(row)
    if sql_select_customer(order_list[x]) == 0:
        sql_insert_customer(order_list[x])

cursor.close()
cnx.close()
browser.close()
print('All records have been updated.')