# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:29:02 2016

@author: Brendan
"""

#Import selenium which will control the web browser.
from selenium import webdriver
#Import modules to force the browser to wait.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#Import datetime to calculate different days.
import datetime
#Import the mysql.connector module to connect to the tcf_database.
import MySQLdb
#Import sys and traceback for error debugging.
import sys
import traceback
#Import time module to force the program to wait for web pages to load.
import time
#Import Beckett_Order_Downloader_Functions to process order info.
from beckett_order_downloader_functions import format_item_description
from beckett_order_downloader_functions import format_customer_info

#Connect to inceff database.
user = 'bk00chenb'
password = 'NR8A*Ecb*'
host = 'inceff.ctlel9cvjtqf.us-west-2.rds.amazonaws.com'
database = 'inceff'
cnx = MySQLdb.connect(user=user, password=password,
                              host=host, database=database)
#Create a cursor object to use for the database connection.
cursor = cnx.cursor()
#Set the autocommit to zero.
cursor.execute('SET autocommit = 0')
cnx.commit()

#Set the capabilites.
browser = webdriver.Firefox()
#Set the browser wait time to 10 seconds.
wait = WebDriverWait(browser, 10)

#Get today's date.
today = datetime.date.today()
#Get the date for 8 days ago.
start_date = today - datetime.timedelta(days = 28)
#Get yesterday's date.
end_date = today - datetime.timedelta(days = 1)
#Save the two dates as strings.
start_date = start_date.strftime("%m/%d/%y")
end_date = end_date.strftime("%m/%d/%y")
#Optional date range override##################################################
#start_date = '04/01/2017'
#end_date = '10/4/2016'
#Optional date range override##################################################
#Open the Beckett admin page.
browser.get('https://www.beckett.com/login')
#Find the loginEmail text box.
loginEmail = browser.find_element_by_id('loginEmail')
#Enter loginEmail.
loginEmail.send_keys('dialcard@nycap.rr.com')
#Find the loginPassword text box.
password = browser.find_element_by_id('loginPassword')
#Enter the loginPassword.
password.send_keys('ruthmick')
#Submit the form.
password.submit()
#Wait for the page to load.
time.sleep(10)
#Go to the search orders page.
browser.get('http://marketplace.beckett.com/admin/search_orders')
#Wait for the page to load.
time.sleep(10)
#Find the From Date text box.
fromDate = browser.find_element_by_id('add_date')
#Enter the date for two days ago.
fromDate.send_keys(start_date)
#Find the To Date text box.
toDate = browser.find_element_by_id('modify_date')
#Enter yesterday's date.
toDate.send_keys(end_date)
#Find the filter button.
filterBtn = browser.find_element_by_id('formfilter')
#Click the filter button.
filterBtn.click()

#Wait for the page to load.
time.sleep(5)
#Find the number of pages.
pages = browser.find_element_by_id('sp_1')
print(pages.text)
#Check to see if more than 1 page of records exist.
if pages.text != '1':
    #If more than 1 page, change the number of records displayed.
    #Find the drop down box.
    select = browser.find_element_by_xpath("//select[@class=\"ui-pg-selbox\"]")
    #Save all the drop down box options.
    all_options = select.find_elements_by_tag_name("option")
    #Choose to display 100 records.
    all_options[3].click()
    print(all_options[3].text)
#Wait for the page to load.
time.sleep(10)
#Find and save all order IDs.
orderIds = browser.find_elements_by_xpath('//td[@aria-describedby=' 
                                         + '\"orders_table_order_id\"]')
#Find and save all order dates.
purchaseDate = browser.find_elements_by_xpath('//td[@aria-describedby='
                                             + '\"orders_table_created\"]')
#Find and save all email addresses.
email = browser.find_elements_by_xpath('//td[@aria-describedby='
                                      + '\"orders_table_email\"]')
#Find and save all first names.
firstName = browser.find_elements_by_xpath('//td[@aria-describedby='
                                          + '\"orders_table_first_name\"]')
#Find and save all last names.
lastName = browser.find_elements_by_xpath('//td[@aria-describedby='
                                         + '\"orders_table_last_name\"]')
#Create a list to hold the order information.
orderList = list()
#Cycle through a range to get the same element for the previous lists.
for x in range(0, len(orderIds)):
    #Create a list to store data for a particlular order
    temp = list()
    temp.append(orderIds[x].text)##########list position 0 - orderID
    temp.append(purchaseDate[x].text[:10])#list position 1 - date
    temp.append(purchaseDate[x].text[11:])#list position 2 - time
    temp.append(email[x].text.lower())#############list position 3 - email
    temp.append(firstName[x].text.title())#########list position 4 - firstName
    temp.append(lastName[x].text.title())##########list position 5 - lastName
    #Add the order info to the order list.
    orderList.append(temp)

#Print a message indicating how many orders were found
print(len(orderIds), 'were found between', start_date, 'and', end_date + '.')
print()
#Cycle through the order IDs and query the tables.
for x in range(0, len(orderList)):
    #Create 3 variable to save query results.
    in_orders_table = False
    in_orderdetails_table = False
    in_customers_table = False
    try:
        #Check the orders table.
        query = ('SELECT * FROM tcf_orders WHERE orderID = "{0}"')
        query = query.format(orderList[x][0])
        cursor.execute(query)
        cursor.fetchone()
        #If the order ID was found, print a message.
        if cursor.rowcount == 1:
            in_orders_table = True
            print('Order ' + orderList[x][0] + ' has already been added.')
        #Check the orderDetails table.
        query = ('SELECT * FROM tcf_orderdetails WHERE orderID = "{0}"')
        query = query.format(orderList[x][0])
        cursor.execute(query)
        cursor.fetchall()
        #If the order ID was found, print a message.
        if cursor.rowcount > 0:
            in_orderdetails_table = True
            if cursor.rowcount == 1:
                print(cursor.rowcount, 'card was already added for '
                     + 'order', orderList[x][0] + '.')
            else:
                print(cursor.rowcount, 'cards were already added for '
                     + 'order', orderList[x][0] + '.')
        #Check the customers table.
        query = ('SELECT * FROM tcf_customers WHERE email = "{0}"')
        query = query.format(orderList[x][3])
        cursor.execute(query)
        cursor.fetchone()
        #If the email was found, print a message.
        if cursor.rowcount == 1:
            in_customers_table = True
            print(orderList[x][4], orderList[x][5], 'has already been added.')
    except MySQLdb.Error as err:
        print("Something went wrong: {}".format(err))
        print(query)
        input("Press Enter to continue...")

    #If the order Id or email was not found, process the order.
    if(in_orders_table == False or in_orderdetails_table == False or
       in_customers_table == False):
        #Build the order's web address and open the site.
        linkName = ('http://marketplace.beckett.com'
                   + '/admin/search_orders/view/' + orderList[x][0])
        #Open the order.
        browser.get(linkName)
        
        #Find and save the element that contains customer info.
        customer_info = browser.find_elements_by_xpath('//div[@style='
                                         + '\"padding: 10px;\"]')
        #Find all the card info contained in td elements.
        tableRows = browser.find_elements_by_tag_name('td')
        #Create a list to store the card info.
        cardInfo = list()
        #Create a counter to track the card info being processed.
        counter = 0
        #Create a flag to tell if the last card has been read.
        lastCard = False
        #Cycle through each td element in the card info table.
        for row in tableRows:
            #Update the counter.
            counter += 1
            if lastCard == False:
                if counter == 1:
                    #If row 1 does not contain 'Shipping', save the item ID.
                    #Otherwise, set lastCard flag to True and add the
                    #card info list to the order list.
                    if 'Shipping' not in row.text:
                        itemID = row.text[:8]
                    else:
                        lastCard = True
                        orderList[x].append(cardInfo)#line position 6
                if counter == 2:
                    #Row 2 contains the item description.
                    #Call function to extract each piece
                    itemDesc = format_item_description(row.text)
                if counter == 3:
                    #Row 3 contains the condition.
                    cond = row.text 
                if counter == 4:
                    #Row 4 contains the sport.
                    sport = row.text
                if counter == 7:
                    #Row 7 contains the quantity purchased.
                    qty = row.text
                if counter == 8:
                    #Row 8 contains the price of each card.
                    price = row.text[1:]
                if counter == 9:
                    #Row 9 contains the total (quantity * price)
                    total = row.text[1:]
                    #Reset the counter and add each detail
                    #to the card info list.
                    counter = 0
                    cardInfo.append([itemID, sport, itemDesc[0], itemDesc[1],
                                     itemDesc[2], itemDesc[3], cond, qty,
                                     price, total, itemID])
            else:               
                if counter == 3:
                    #Row 3 (after all card info) contains shipping cost.
                    #Add shiping to the order list.
                    shipping = float(row.text[1:])
                    orderList[x].append(shipping)#line position 7 - shipping
                if counter == 6:
                    #Row 3 (after all card info) contains the tax paid
                    tax = float(row.text[1:])
                    #Add tax to the order list.
                    orderList[x].append(tax)#line position 8 - tax
                if counter == 9:
                    #Row 9 could be the total or a discount applied.
                    #Check for (-) which indicates the discount.
                    if '(-)' not in row.text:
                        #Subtract shipping and tax to get the total.
                        total = float(row.text[1:]) - shipping - tax
                        #Add the total to the order list.
                        orderList[x].append(total)#line position 9 - total
#                    else:
#                        promo = row.text[4:]
                if counter == 12:
                    #If there was a discount row 12 contains the total
                    total = float(row.text[1:]) - shipping - tax
                    orderList[x].append(total)#line position 8 - total

    #Update the orders table if needed.
    if(in_orders_table == False):
        try:
            #Create the query and update the orders table.
            query = ('INSERT INTO tcf_orders(orderID, email, added, date, time, '
                    + 'shipping, tax, total) VALUES("{0}", "{1}", "{2}", '
                    + '"{3}", "{4}", "{5}", "{6}", "{7}")')
            query = query.format(orderList[x][0], orderList[x][3], 1,
                                 orderList[x][1], orderList[x][2],
                                 orderList[x][7], orderList[x][8],
                                 orderList[x][9])
            cursor.execute(query)   
            cnx.commit()
            #Print a message indicating the order was added.
            print('Order', orderList[x][0], 'was added to the orders '
                 + 'table.')
        except MySQLdb.Error as err:
            #If the update fails, print a message and the query.
            print("Something went wrong: {}".format(err))
            print('Order', orderList[x][0], 'was not added!')
            print(query)
            input("Press Enter to continue...")

    #Update the orderdetails table if needed.
    if(in_orderdetails_table == False):
        #Cycle through the cards in each order.
        for card in orderList[x][6]:
            try:
                #Create the query and update the orderdetails table.
                query = ('INSERT INTO tcf_orderdetails(itemID, sport, year, '
                        + 'setName, cardNumber, cardName, cond, qty, '
                        + 'price, total, orderID) VALUES("{0}", "{1}", '
                        + '"{2}", "{3}", "{4}", "{5}", "{6}", "{7}", '
                        + '"{8}", "{9}", "{10}")')
                query = query.format(card[0], card[1], card[2], card[3],
                                     card[4], cnx.escape_string(card[5]),
                                     card[6], card[7], card[8], card[9],
                                     orderList[x][0])
                cursor.execute(query)
#                #Search the tcf_sets table for the set.
#                query2 = ('SELECT set_id FROM tcf_sets '
#                + 'WHERE set_year = "{0}" AND category = "{1}" '
#                + 'AND set_name = "{2}"')
#                query2 = query2.format(card[2], card[1], card[3])
#                cursor.execute(query2)
#                cursor.fetchall()
#                #If the set was found, print a message.
#                temp_str = card[1] + ' ' + card[2] + ' ' + card[3]
#                if(cursor.rowcount == 1):
#                    print(temp_str, 'was found in tcf_sets.')
#                else:
#                    #If the set wasn't found, add it to the table.
#                    query3 = ('INSERT INTO tcf_sets(set_year, category, '
#                    'set_name) VALUES("{0}", "{1}", "{2}")')
#                    query3 = query3.format(card[2], card[1], card[3])
#                    cursor.execute(query3)
#                    cnx.commit()
#                    print(temp_str, 'was added to tcf_sets.')
            except MySQLdb.Error as err:
                print("Something went wrong: {}".format(err))
                for frame in traceback.extract_tb(sys.exc_info()[2]):
                    fname,lineno,fn,text = frame
                    print (("Error in {0} on line {1}").format(fname, lineno))
        #Commit the insert statements.
        cnx.commit()
        #Print a message indicating all cards were added.
        if len(orderList[x][6]) == 1:
            print(len(orderList[x][6]), 'card was added for order '
                 + orderList[x][0] + '.')
        if len(orderList[x][6]) > 1:
            print(len(orderList[x][6]), 'cards were added for order '
                 + orderList[x][0] + '.')

    #Update the customers table if needed.
    if(in_customers_table == False):
        #Create a list to hold customer info
        customerInfo = list()
        #Cycle through the elements in customer_info.
        for element in customer_info:
            if 'Phone Number' in element.text:
                customerInfo = format_customer_info(element.text, customerInfo)
            if 'Address' in element.text:
                customerInfo = format_customer_info(element.text, customerInfo)
        try:
            #Create the query and update the customers table.
            query = ('INSERT INTO tcf_customers(email, added, firstName, '
                    + 'lastName, phone, shipTo, address, city, '
                    + 'state, zipcode, country) VALUES("{0}", "{1}", '
                    + '"{2}", "{3}", "{4}", "{5}", "{6}", "{7}", '
                    + '"{8}", "{9}", "{10}")')
            query = query.format(orderList[x][3], 1, orderList[x][4],
                                orderList[x][5], customerInfo[0],
                                customerInfo[1], customerInfo[2],
                                customerInfo[3], customerInfo[4],
                                customerInfo[5], customerInfo[6])
            cursor.execute(query)
            cnx.commit()
            #Print a message indicating all cards were added.
            print(orderList[x][4], orderList[x][5],
                  'was added to the customers table.')
        except MySQLdb.Error as err:
            #If the update fails, print a message and the query.
            print("Something went wrong: {}".format(err))
            print('Details for order', orderList[x][0],
                  'were not added!')
            print(query)
            input("Press Enter to continue...")
    print()
cursor.close()
cnx.close()
browser.close()
print('All records have been updated.')