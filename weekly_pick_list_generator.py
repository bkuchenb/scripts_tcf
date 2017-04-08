#Import datetime to calculate different days.
import datetime
#Import the mysql.connector module to connect to the tcf_database.
import mysql.connector
from NaturalSort import natural_sort_1
#Connect to tcf_beckett database.
beckett_cnx = mysql.connector.connect(user='Mickey',password='R00thMick',
                              host='localhost',database='tcf_beckett')
#Connect to tcf_overflow database.
overflow_cnx = mysql.connector.connect(user='Mickey', password='R00thMick', 
                              host='localhost', database='tcf_overflow')

#Get today's date.
today = datetime.date.today()
#Get the date for 8 days ago.
start_date = today - datetime.timedelta(days = 8)
#Get yesterday's date.
end_date = today - datetime.timedelta(days = 1)
#Save the two dates as strings.
#start_date = start_date.strftime("%m/%d/%y")
#end_date = end_date.strftime("%m/%d/%y")
#Optional date range override##################################################
#start_date = '09/28/2016'
#end_date = '10/4/2016'
#Optional date range override##################################################

#Create two cursor objects to use for the database connections.
beckett_cursor = beckett_cnx.cursor()
overflow_cursor = overflow_cnx.cursor()
#Set the autocommit to zero.
beckett_cursor.execute('SET autocommit = 0')
overflow_cursor.execute('SET autocommit = 0')
beckett_cnx.commit()
overflow_cnx.commit()

#Find the orders for the last week.
query = ('SELECT * FROM orders WHERE date > "{0}"')
query = query.format(start_date)
beckett_cursor.execute(query)
orders_list = beckett_cursor.fetchall()
message_str = 'There were ' + str(beckett_cursor.rowcount) + ' orders '
message_str = message_str + 'from ' + start_date.strftime("%m/%d/%y")
message_str = message_str + ' to ' + end_date.strftime("%m/%d/%y") + '.'
#Create a list to store the cards sold for the week.
print_list = list()
#Cycle through each order to get a list of the cards sold.
for order in orders_list:
    #print(order[0])
    #Check the orderDetails table.
    query = ('SELECT * FROM orderdetails WHERE orderID = "{0}"')
    query = query.format(order[0])
    beckett_cursor.execute(query)
    details = beckett_cursor.fetchall()
    for card in details:
        temp_str = str(card[2]) + ' ' + str(card[3]) + ' '
        temp_str = temp_str + str(card[4])  + ' ' + str(card[5])
        temp_list = list()
#        temp_list.append(card[2])
#        temp_list.append(card[3])
#        temp_list.append(card[4])
#        temp_list.append(card[5])
        temp_list.append(temp_str)
        print_list.append(temp_list)
print_list = natural_sort_1(print_list, 0)
#Create a txt file to write the data.
with open('weekly_pick_list.txt', 'w') as file:
    for card in print_list:
#        temp_str = str(card[0]) + ' ' + str(card[1]) + ' '
#        temp_str = temp_str + str(card[2])  + ' ' + str(card[3])
#        file.write(temp_str + '\n')
        file.write(card[0])
        file.write('\n')
print(message_str)
print('There were ' + str(len(print_list)) + ' cards sold.')

beckett_cursor.close()
overflow_cursor.close()
beckett_cnx.close()
overflow_cnx.close()
print('Weekly pick list has been created.')