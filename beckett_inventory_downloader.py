# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:29:02 2016

@author: Brendan
"""

#Import selenium which will control the web browser.
from selenium import webdriver
#Import the select module.
from selenium.webdriver.support.select import Select
#Import urllib
import urllib
#Import modules to force the browser to wait.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Import sys, traceback and mysql.errors for error debugging.
import sys
import traceback
from mysql.connector.errors import Error
#Import time module to force the program to wait for web pages to load.
import time
#Import the mysql.connector module to connect to the tcf databases.
import mysql.connector

#Connect to tcf_overflow database.
cnx = mysql.connector.connect(user='Mickey', password='R00thMick', 
                              host='localhost', database='tcf_overflow')
#Create a cursor object to use with this database.
cursor = cnx.cursor()
#Connect to tcf_inventory_baseball database.
cnx_2 = mysql.connector.connect(user='Mickey', password='R00thMick', 
                          host='localhost',
                          database='tcf_inventory_baseball')
#Create a cursor object to use with this database.
cursor_2 = cnx_2.cursor()
#Set the autocommit to zero.
cursor_2.execute('SET autocommit = 0')
cnx_2.commit()
try:
    year_input = input('Enter the year: ')
    #find the name of all the baseball sets
    query = ('SELECT id, year, set_name FROM baseball '
            + 'WHERE year = "{0}" AND details = "0"')
    cursor.execute(query.format(year_input))
    results = cursor.fetchall()
    total_sets = cursor.rowcount
    #Print the results.
    print(total_sets, 'sets were found.')
    #If there are no records,
    #close all databse connections and end the program.
    if(cursor.rowcount == 0):
        cnx.close()
        cnx_2.close()
        sys.exit()
except Exception as error:
    for frame in traceback.extract_tb(sys.exc_info()[2]):
        fname,lineno,fn,text = frame
        print (("Error in {0} on line {1}").format(fname, lineno))
#Select the Firefox browser.
browser = webdriver.Firefox()
#Force Firefox to open in full screen mode.
browser.maximize_window()
#Set the browser wait time to 10 seconds.
wait = WebDriverWait(browser, 10)

#Open the Beckett admin page.
browser.get('http://marketplace.beckett.com/admin')
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
#*****************************************************************************#
#Get the sport.
sport = 'baseball'
#Build the Item Management page string.
item_management_str = ('http://marketplace.beckett.com/admin/accelerator'
                      + '/sets/search#sport=')
if sport.lower() == 'baseball':
    item_management_str += '185223'
#*****************************************************************************#
#Create a counter to tell which set was processed.
set_number = 1
for row in results:
    try:
        #Open the Item Management page.
        browser.get(item_management_str)
        #Force the browser to wait until the search box is present.
        wait.until(EC.presence_of_element_located((By.ID,'search_text')))
        #Wait for the page to load.
        time.sleep(5)
        #Find the search box.
        search_box = browser.find_element_by_id('search_text')
        search_text = row[1] + ' ' + row[2]
        #Enter setName.
        search_box.send_keys(search_text)
        #Submit the form.
        search_box.submit()
        #Find the number of pages.
        pages = browser.find_element_by_id('sp_1')
        #Check to see if more than 1 page of records exist.
        if pages.text != '1':
            #If more than 1 page, change the number of records displayed.
            #Find the drop down box.
            select = browser.find_element_by_xpath("//select[@class=\"ui-pg-selbox\"]")
            #Save all the drop down box options.
            all_options = select.find_elements_by_tag_name("option")
            #Choose to display 100 records.
            all_options[3].click()
        #Wait for the page to load.
        time.sleep(5)
        #Find all the check boxes.
        check_boxes = browser.find_elements_by_class_name('cbox')
        #Build the xpath to the set names link.
        set_names_str = "//td[@aria-describedby=\"search_results_table_disp_title\"]"
        #Find all the set names.
        set_names = browser.find_elements_by_xpath(set_names_str)
        #Check the box that corresponds to the set name.
        for y in range(0, len(set_names)):
            if set_names[y].text == search_text:
                check_boxes[y + 1].click()
        #Find the Export button
        export_btn = browser.find_element_by_id('export_selected_to_accelerator')
        #Click the Export button.
        export_btn.click()
        #Wait for the page to load.
        time.sleep(10)
        #Find and save the number of pages.
        pages = browser.find_element_by_id('sp_1_inventory_table_toppager')
        num_pages = pages.text
        if(num_pages == ''):
            num_pages = 0
        #Build xpath of the next page button.
        next_btn_str = ("//span[@class=\"ui-icon ui-icon-seek-next\"]")
        #Find the next page button.
        next_btn = browser.find_element_by_xpath(next_btn_str)
        #Create a new table to store the data.
        table_name = 'baseball_' + str(row[0])
        create = ('CREATE TABLE ' + table_name + ' LIKE template')
        cursor_2.execute(create)
        cnx_2.commit()
        #save all the information on each page
        for page in range(1, int(num_pages) + 1):
            #Build the xpath to the qty.
            qty_str = "//td[@aria-describedby=\"inventory_table_quantity_total\"]/input"
            #Find all the quantities.
            qty_cells = browser.find_elements_by_xpath(qty_str)
            #Build the xpath to the description.
            desc_str = "//td[@aria-describedby=\"inventory_table_title\"]"
            #Find all the descriptions.
            desc_cells = browser.find_elements_by_xpath(desc_str)
            #Build the xpath to the rookie chard checkboxes.
            rc_str = "//td[@aria-describedby=\"inventory_table_rookie_card\"]/input"
            #Find all the rookie cards.
            rc_cells = browser.find_elements_by_xpath(rc_str)
            #Build the xpath to the autographed check box.
            auto_str = "//td[@aria-describedby=\"inventory_table_autographed\"]/input"
            #Find all the autographs.
            auto_cells = browser.find_elements_by_xpath(auto_str)
            #Build the xpath to the memorabilia checkboxes.
            mem_str = "//td[@aria-describedby=\"inventory_table_memorabilia\"]/input"
            #Find all the memorabilia.
            mem_cells = browser.find_elements_by_xpath(mem_str)
            #Build the xpath to the serial number checkboxes.
            ser_str = "//td[@aria-describedby=\"inventory_table_serial_numbered\"]/input"
            #Find all the serial numbered cards.
            ser_cells = browser.find_elements_by_xpath(ser_str)
            #Find all the drop down boxes.
            drop_downs = browser.find_elements_by_tag_name('select')
            #Build the xpath to the conditional prices.
            cond_str = ("//td[@aria-describedby=\"inventory_table_conditional_price\"]")
            #Find all the conditional prices.
            cond_cells = browser.find_elements_by_xpath(cond_str)
            #Build the xpath to the high price.
            price_str = "//td[@aria-describedby=\"inventory_table_price_high\"]"
            #Find all the prices.
            price_cells = browser.find_elements_by_xpath(price_str)
            #Find all the view buttons.
            view_buttons = browser.find_elements_by_class_name('ajax-popup-link')    
            #Cycle through each card.
            for x in range(0, len(qty_cells)):
                #Save the item description.
                temp = desc_cells[x].text
                #Split the string.
                temp = temp.split()
                #Find the card number, which contains a #.
                for index in range(0, len(temp)):
                    if '#' in temp[index]:
                        cardNumber = index
                #Build the card name.
                cardName = ''
                for z in range(cardNumber + 1, len(temp)):
                    cardName += temp[z] + ' '
                cardName = cardName.strip()
                #Save the two price strings.
                price = price_cells[x].text
                cond_price = cond_cells[x].text
                #Get the drop down box selection.
                select = Select(drop_downs[x + 3])
                #Save the condition.
                condition = select.first_selected_option

                #Create the insert statement and add the card to the database.
                insert = ('INSERT INTO {0}(set_id, quantity, card_number, '
                        + 'name, price, rc, auto, mem, ser, cond_price, cond) VALUES("{1}", '
                        + '"{2}", "{3}", "{4}", "{5}", "{6}", "{7}", "{8}", '
                        + '"{9}", "{10}", "{11}")')
                insert = insert.format(table_name, row[0],
                                     qty_cells[x].get_attribute('value'),
                                     temp[cardNumber], cardName, price[1:],
                                     rc_cells[x].get_attribute('value'),
                                     auto_cells[x].get_attribute('value'),
                                     mem_cells[x].get_attribute('value'),
                                     ser_cells[x].get_attribute('value'),
                                     cond_price[1:], condition.text)
#*****************************************************************************#
#                print(insert)
#                #Click on the view stock photo link.
#                view_buttons[x].click()
#                #Get the div element that contains the images.
#                div_parent = browser.find_element_by_id('cboxContent')
#                #Print the number of divs in div_parent.
#                children = div_parent.find_elements_by_tag_name('img')
#                print(len(children))
#                print(div_parent.text)
#                #Get the front img element.
#                images = div_image.find_elements_by_tag_name('img')
#                print(len(images))
#                print(images[0].get_attribute('src'))
#                #Create a new file name for the image.
#                file_name = sport + '_' + str(row[0]) + '_' + str(x + 1) + '_front.jpg'
#                #Download and save the image.
#                file, headers = urllib.request.urlretrieve(src, file_name)
#                html = open(file)
#                html.close()
#                #Get and save the back image.
#                file_name_back = file_name.replace('front', 'back')
#                src = images[x + 1].get_attribute('src')
#                #Download and save the image.
#                file, headers = urllib.request.urlretrieve(src, file_name_back)
#                html = open(file)
#                html.close()
#                #Close the popup.
#                browser.find_element_by_id('cboxClose').click()
#*****************************************************************************#
                cursor_2.execute(insert)
#*****************************************************************************#
#            print('Page', page, 'of', num_pages, 'has been downloaded for',
#                  search_text + '.')
#*****************************************************************************#
            if page != int(num_pages):
                #Click the next page button.
                next_btn.click()
                #Wait for the page to load.
                time.sleep(5)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    #Commit all the insert statements.
    cnx_2.commit()
    #Update the details column in the tcf_overflow database.
    update = ('UPDATE baseball SET details = 1 WHERE id = {0}')
    update = update.format(row[0])
    cursor.execute(update)
    cnx.commit()
    #Print a message indicating which set was added.
    print('Set', set_number, 'of', total_sets, 'finished downloading.')
    print('(' + search_text + ') is up to date.')
    set_number += 1
#Close all databse connections and the web browser.
cnx.close()
cnx_2.close()
browser.close()
sys.exit()