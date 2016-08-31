# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:25:54 2016

@author: Brendan
"""

#Import sys and traceback for error debugging.
import sys
import traceback

def format_item_description(itemString):
    #Strip any whitespace from itemString.
    itemString = itemString.strip()
    #Create a list to store card info.
    itemDesc = list()
    #Split the string.
    temp = itemString.split()
    #Find the card number, which contains a #.
    for x in range(0, len(temp)):
        if '#' in temp[x]:
            cardNumber = x
    #Add the year to itemDesc.
    itemDesc.append(temp[0])#list position 0 - year
    #Build the set name.
    setName = ''
    for y in range(1, cardNumber):
        setName += temp[y] + ' '
    #Add the set name to itemDesc.
    itemDesc.append(setName.strip())#list position 1 - setName
    #Add the card number to itemDesc.
    itemDesc.append(temp[cardNumber])#list position 2 - cardNumber
    #Build the card name.
    cardName = ''
    for z in range(cardNumber + 1, len(temp)):
        #If an item was refunded, a * prints at the end.
        #Break the loop if this character is found.
        if '*' not in temp[z]:
            cardName += temp[z] + ' '
        else:
            break
    #Add the card name to itemDesc (list position 3 - cardName).
    itemDesc.append(cardName.strip())
    return itemDesc

def format_customer_info(text, customerInfo):
    try:
        #Get the phone number.
        if 'Phone Number' in text:
            #Strip any whitespace from the string.
            customer_info_str = text.strip()
            #Split the string by lines.
            temp = customer_info_str.splitlines()
            #Save the phone number.
            customerInfo.append(temp[len(temp) - 1][14:])
        #Get the shipping info
        if 'Address' in text:
            if 'In Store Pickup' in text:
                shipTo = 'In Store Pickup'
                address = ''
                city = ''
                state = 'NY'
                zipcode = ''
                country = 'United States'
            elif len(text.strip()) == 16:
                shipTo = 'In Store Pickup'
                address = ''
                city = ''
                state = 'NY'
                zipcode = ''
                country = 'United States'
            else:
                #Strip any whitespace from the string.
                shipping_info_str = text.strip()
                #Split the string by lines.
                temp = shipping_info_str.splitlines()
                #Save the shipTo, name, address, city, state, zip and country.
                if len(temp) == 5:
                    shipTo = temp[1].title()
                    address = temp[2].title()
                    #Check to see if the city is followed by a comma
                    if ',' in temp[3]:
                        #remove any double commas before splitting
                        city_state_zip = temp[3].replace(',,', ',').split(',')
                        city = city_state_zip[0].title()
                        state_zip = city_state_zip[1].split()
                        #Capitalize both characters if state is abbreviated.
                        if len(state_zip) == 2:
                            state = state_zip[0].upper()
                        else:
                            state = state_zip[0].title()
                        zipcode = state_zip[1]
                    else:
                        city_state_zip = temp[3].split()
                        city = ''
                        for x in range(0, len(city_state_zip) - 2):
                            city = city + city_state_zip[x]
                        state = city_state_zip[len(city_state_zip) - 2].title()
                        if len(state) == 2:
                            state = state.upper()
                        zipcode = city_state_zip[len(city_state_zip) - 1]
                    country= temp[4].title()
                else:
                    print('This address is', len(temp), 'lines!')
                    shipTo = temp[1].title()
                    address = temp[2].title() + temp[3].title()
                    #Check to see if the city is followed by a comma
                    if ',' in temp[4]:
                        #remove any double commas before splitting
                        city_state_zip = temp[4].replace(',,', ',').split(',')
                        city = city_state_zip[0].title()
                        state_zip = city_state_zip[1].split()
                        #Capitalize both characters if state is abbreviated.
                        if len(state_zip) == 2:
                            state = state_zip[0].upper()
                        else:
                            state = state_zip[0].title()
                        zipcode = state_zip[1]
                    else:
                        city_state_zip = temp[4].split()
                        city = ''
                        for x in range(0, len(city_state_zip) - 2):
                            city = city + city_state_zip[x]
                        state = city_state_zip[len(city_state_zip) - 2].title()
                        zipcode = city_state_zip[len(city_state_zip) - 1]
                    country= temp[5].title()
            #Add the remaining data to the customerInfo list
            customerInfo.append(shipTo)
            customerInfo.append(address)
            customerInfo.append(city)
            customerInfo.append(state)
            customerInfo.append(zipcode)
            customerInfo.append(country)
    except Exception as error:
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print (("Error in {0} on line {1}").format(fname, lineno))
        input("Press Enter to continue...")
    return customerInfo