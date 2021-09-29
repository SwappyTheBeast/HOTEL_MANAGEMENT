#IMPORTING REQUIRED MODULES
import mysql.connector
import datetime
import pyautogui

#CONNECTING TO DB AND CREATING CURSOR OBJECT
mycon = mysql.connector.connect(user='root',passwd='',host='localhost',database='hotel_management')
cursor = mycon.cursor()

#DEFINING GLOBAL VARIABLES NEEDED
global action
global count
count = 0

#DEFINING NEEDED FUNCTIONS

#Checkin
def add_customer():
    try:
        fName = str(input("ENTER CUSTOMER NAME : "))
        Phone_Number = str(input("ENTER PHONE NUMBER : "))
        customer_id = str(input("CUSTOMER ID TYPE : "))
        id_number = str(input("ID NUMBER : "))
        room_id = str(input("SELECT ONE ROOM OUT OF " + rooms_available() + " : "))
    
        cursor.execute("INSERT INTO customers(fName,Phone_Number,customer_id,id_number,room_id) VALUE('{}',{},'{}','{}',{});".format(fName,Phone_Number,customer_id,id_number,room_id))
        mycon.commit()
        cursor.execute("SELECT Sr_No FROM customers WHERE fName = '{}' AND Phone_Number = {};".format(fName,Phone_Number))
        data = cursor.fetchone()
        Sr_No = data[0]
        cursor.execute("UPDATE rooms SET Occupied_by_customer = {} WHERE room_id = {};".format(Sr_No,room_id))
        cursor.execute("UPDATE rooms SET availabilty = 'Booked' WHERE room_id = {};".format(room_id))
        mycon.commit()
        print("Customer has been succesfully added to database.")
    except:
        print("There was an error in making new entry. Please try again")
        add_customer()

#returns a string made of available rooms    
def rooms_available():
    cursor.execute("SELECT room_id FROM rooms WHERE availabilty = 'available';")
    data = cursor.fetchall()
    rooms = ''
    for room in data:
        for r in room:
            rooms = rooms + str(r) + ' ' 
    return rooms

#to search database for customer name,phone number and their id, of the customer currently staying in the room
def customer_info_based_on_room():
    try:
        room_id = str(input("Enter room number : "))
        cursor.execute("SELECT fName,Phone_Number,id_number FROM customers WHERE room_id = {} AND doc IS NULL".format(room_id))
        record = cursor.fetchone()
        if record is not None:
            name = record[0]
            phone = record[1]
            id_num = record[2]
            print("{} is staying in room {}. \nHis phone number is {}. \nHis id number is {}.".format(name,room_id,phone,id_num))
        elif room_id in ['1001','1002','1003','1004','1005','1006','1007','1008','1009','1010']:
            print("No one is staying in room {}".format(room_id))
        else:
            print("No such room exists")
            customer_info_based_on_room()
    except:
        print("There was an error in finding information. Please try again")
        customer_info_based_on_room()

#checkout
def checkout():
    try:
        name = str(input("ENTER NAME OF CUSTOMER ABOUT TO CHECKOUT : "))
        cursor.execute("SELECT Sr_No,fName,doa,doc,room_id FROM customers WHERE fName = '{}' AND doc IS NULL;".format(name))
        record = cursor.fetchone()
        if record is not None:
            Sr_No = record[0]
            name = record[1]
            doa = record[2]
            room_id = record[4]
            make_bill(Sr_No,name,doa,room_id)
            cursor.execute("UPDATE customers SET doc = CURRENT_TIMESTAMP() WHERE Sr_No = {}".format(Sr_No))
            cursor.execute("UPDATE rooms SET Occupied_by_customer = NULL, availabilty = 'available' WHERE room_id = {};".format(room_id))
            mycon.commit()
        
        else:
            print("Customer {} is not staying here right now".format(name))
            checkout()
    except:
        print("There was an error in checkout. Please try again")
        checkout()
        
#makes bill and adds to table bills
def make_bill(Sr_No,name,doa,room_id):
    cursor.execute("SELECT cost_pernight FROM rooms WHERE room_id = {}".format(room_id))
    record = cursor.fetchone()
    cost = record[0]
    doc = datetime.datetime.today()
    days = (doc-doa).days
    amount = days * cost
    cursor.execute("SELECT bill_id FROM bills")
    last_bill_id = cursor.fetchall()[-1][0]
    number = int(last_bill_id[2:5]) + 1
    no_of_zeros = 3-len(str(number))
    new_bill_id = 'AA' + '0'*no_of_zeros + str(number)
    payment_method = str(input("ENTER PAYMENT METHOD : "))
    discount = amount / 10
    cursor.execute("INSERT INTO bills(Bill_id,customer_name,Sr_No,amount,discount,payment_method) VALUE('{}','{}',{},{},{},'{}');".format(new_bill_id,name,Sr_No,amount,discount,payment_method))
    print("Bill has been created successfully.\nBill id is {} \nAmount to be paid is {}".format(new_bill_id,amount))

#searches table for room if currently staying, or else for phone number and id
def info_based_on_customer_name():
    try:
        name = str(input("ENTER CUSTOMER NAME : "))
        phone = input("ENTER PHONE NUMBER(not necessary) : ")
        if phone == '':
            cursor.execute("SELECT Sr_No,customer_id,id_number,doa,doc,room_id FROM customers WHERE fName = '{}'".format(name))
            data = cursor.fetchall()
            if data != []:
                customer_id = data[0][1]
                id_number = data[0][2]
                room_id = data[0][5]
                if data[-1][4] is None:
                    print("Customer {} is currently staying in room {}. \nHis {} number is {}.".format(name,room_id,customer_id,id_number) )
                else:
                    times = len(data)
                    print("Customer {} has stayed {} times. \nHis {} number is {}.".format(name,times,customer_id,id_number))
            else:
                print("No such customer exists")
                #info_based_on_customer_name()
        else:
            cursor.execute("SELECT Sr_No,customer_id,id_number,doa,doc,room_id FROM customers WHERE fName = '{}' AND Phone_number = {}".format(name,phone))
            data = cursor.fetchall()
            if data != []:
                customer_id = data[0][1]
                id_number = data[0][2]
                room_id = data[0][5]
                if data[-1][4] is None:
                    print("Customer {} is currently staying in room {}. \nHis {} number is {}.".format(name,room_id,customer_id,id_number) )
                else:
                    times = len(data)
                    print("Customer {} has stayed {} times. \nHis {} number is {}.".format(name,times,customer_id,id_number))
            else:
                print("No such customer exists")
                info_based_on_customer_name()
    except:
        print("There was an error in searching database. Please try again")
        info_based_on_customer_name()

#calculates sum of total money intake and discount given
def money_made():
    cursor.execute("SELECT SUM(ALL net_to_be_paid),SUM(ALL discount) FROM bills;")
    data = cursor.fetchall()
    money = data[0][0]
    discount = data[0][1]
    print("The cash inflow is \u20B9{} since the hotel's opening, after giving \u20B9{} as discount.".format(money,discount))

#takes input for choice of action
def input_action():
    global action
    try:
        action = int(input("Please select one action from list above(enter the number associated with action)"))
        if action not in [1,2,3,4,5,6,7]:
            print("Not a valid option, please select again")
            input_action()
    except:
        print("Not a valid option, please select again.")
        input_action()

#prints a lot of new line characters to make previous printed lines go up, and gives a clear screen to print more to
def clear_screen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#scrolls up so that the heading of main menu appear always as first line on screen
def scroll():
    global count
    if count != 1:
        pyautogui.keyDown('ctrl')
        pyautogui.press('down', presses = 27)
        pyautogui.keyUp('ctrl')

#The Main Menu of the program that controls everything    
def main_menu():
    global action
    global count
    print("#################~~-*-*-*-*-WELCOME TO HOTEL PLAZA-*-*-*-*-~~#################",end = '\n\n\n\n')
    print("Following are what this program can do -----")
    print("1. Add new customer(CheckIn)")
    print("2. CheckOut")
    print("3. Search for available rooms")
    print("4. Search for a customer's information staying in some room")
    print("5. Search for room and id information based on customer name and/or phone number")
    print("6. Calculate lifetime money intake for the hotel")
    print("7. Exit Program")
    print("================================================================================================================")
    count += 1
    scroll()
    input_action()

    if action == 1:
        add_customer()
        input()
        clear_screen()
        main_menu()
    elif action == 2:
        checkout()
        input()
        clear_screen()
        main_menu()
    elif action == 3:
        print("Following rooms are available --")
        print(rooms_available())
        input()
        clear_screen()
        main_menu()
    elif action == 4:
        customer_info_based_on_room()
        input()
        clear_screen()
        main_menu()
    elif action == 5:
        info_based_on_customer_name()
        input()
        clear_screen()
        main_menu()
    elif action == 6:
        money_made()
        input()
        clear_screen()
        main_menu()
    elif action == 7:
        mycon.close()

#CALLING THE MAIN MENU
main_menu()




    



