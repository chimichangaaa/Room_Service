"""""
This is the assesment we as a class learnt, and now putting it into a project. I have made the room service with the theme 
of a video game that I enjoy playing; Genshin Impact. We used if, while, subjects, keys, etc.

This project is made by Uyanga 10B
"""""

#We type in the neccesary values so we can get the needed questions.
import datetime

#this will be the dictionary for the room numbers and guests.
guests = {'100':'Kazuha', '101':'Ayaka', '102':'Sayu', '103':'Thoma'}

#Dictionaries with the menu for each section.
appetizer = {'200':'Bread and Pesto', '201':'Mushroom Soup', '202':'Jade Parcels'} 
main_course = {'201':'Sakura Tempura', '202':'Moon Pie', 
'202':'Dumpling Soup'} 
desserts = {'300':'Greem Tea Mochi', '301':'Red Bean Puff', '303':'Raspberry Sundae'}

#make sure these exist in the program.
name = None
room = None
#we now 'create' a dictionary with the customer's order. 
order = {}
#now it's time to check if the room has been booked.
while room not in guests.keys():
    room = input('Good day, please enter your room number \(^^)/: ')
    #check if the room is valid.
    if room in guests.keys():
        name = input('Please kindly enter your name (+_+)_/: ')
        #we check if each of them correspond to one another and if it doesn't, we go back to the 'starter' page.
        if guests[room] != name:
            print ('I am sorry, your name does not match our records. Please try again- ')
            room = None
    else:
        print (f'Room {room} was not validated, please try again T-T ')

#We now make the menu for appetizers for the viewers to select from.
print ()
print ('++ Appetizers ++')
print ('- - - - - - - - -')
for code, food in appetizer.items():
    print (code, '->', food)

#add a blank line
print()
#after this we make the program for appetizers.
starters = None
#now we go ahead and check whether the menu goes with the others. 
while starters not in appetizer.keys():
    starters = input ('Please enter the code for your appetizer (^^)/: ')
    if starters not in appetizer:
        print('Apolagies, the code you have put does not exist; please try again \(T-T)')
    else:
        order[starters] = appetizer[starters]

#now, we go ahead and make the Main course menu to choose from.
print ()
print ('    Main Course     ')
print ('- - - - - - - - - - ')
print()
for code, food in main_course.items():
    print (code, '->', food)

print()
#It's main course time!
main_coursee = None
#we do the main course as the same for appetizers now;
while main_coursee not in main_course.keys():
    main_coursee = input ('Please choose a main course for your meal (^o^)/ :  ')
    if main_coursee not in main_course:
        print('The code you typed was not valid please try again (o-o)-/ ')
    else:
        order[main_coursee] = main_course[main_coursee]

#Now desserts menu; as you can see while coding, this is getting repetivitve, just with different subjects and options.
print ()
print ('  D e s s e r t s  ')
print ('- - - - - - - - - - - ')
print()
for code, food in desserts.items():
    print (code, '->', food)
print()
print('---------------')
print()


dessert = None
while dessert not in desserts.keys():
    dessert = input ('Please type in your code for the most magical part of the meal; + d e s s e r t + : ')
    if dessert not in desserts:
        print('The code you put does not exist, please try again (T_T)/ you must have dessert : ')
    else:
        order[dessert] = desserts[dessert]

#now that we have the three important ones, we go and make the time because, people need the time for the meal.
timeformat = "%H:%M"

validtime = False

while not validtime:
    delivery_time = input("Kindly type in the time you want the food to be delivered (^-^) : ")
    try:
        validtime = datetime.datetime.strptime(delivery_time, timeformat)
    except ValueError:
       print ('Time format hh:mm')
#at first I didn't know how to put in the time program, so I went through google and searched for the most practical one.

#We're almost done, now we just need to have the summary of the menu the guest has chosen.
print ()
print ('For our dear guest {guests} : ')
print ('- - - - - - - - - - - - - - - - - ')
print()
for code, food in order.items():
    print (code, '->', food)

print('Delivery time at : ', delivery_time)

place_order = ''

while place_order.lower() not in ('yes', 'no'):
    place_order = input ('Ready to place your order? (yes/no)?')

print()
if place_order == 'yes':
    print ('Your order is 99 percent complete....')
else:
    print ('Your order has been cancelled')

print ('Order has been confirmed; Thank you so much for choosing us! (^o^)/*****')