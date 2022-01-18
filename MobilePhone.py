import os
import re
import time

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#This asks user to input personal information
print("how are you doing?")
customerfeelings = input(">>>")
print("that's good to know!")

print("Loading...")
wait = input("PRESS ENTER TO CONTINUE.")
print("loading...")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~Personal Details~~~~~~~~~~~~~~~~~~~~~")
print("what's your name?") #inputting information 
customername = input(">>>")

print("what's your surname?")
customersurname = input(">>>")

print("what's your address?")
customeraddress = input(">>>")

print("what's your postcode?")
customerpostcode = input(">>>")

def validate_email(): #checking if user is using an accurate Email.
    email = input("enter the mail address::")
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
#checks if '@' is included in the email for it to be valid
    if match:
        print("valid email :::"), match.group()
    else:
        print("not valid:::")

validate_email()

print(" Enter your phone number")
customernumber = input(">>>")

print("Enter the account number of your bank card")
userbank = input(">>>")

print ("Enter sort code")
usersortcode = input(">>>")

print("Enter expiry date")
userexpirydate = input(">>>")

print("\n~~~~~~~~~~~~~~~~~~~~~~~Phone's~~~~~~~~~~~~~~~~~~~~~~~~~")
print("During this stage, enter the number of your choice. \nFor example, if the question asks you to enter either [1] or [2] then choose one option.")

#customerdevice = "phone"
#payasyougo = "P"
#contract = "C"

def purchase():
    #change made here
    global cost_of_phone
    global cost_of_contract
    global cost_upfront

    print("\nYou have chosen to purchase a Phone")
    print("1. iphone 11 which costs £600.00")
    time.sleep(1)

    print("2. Samsung Galaxy S10 which costs £494.95")
    time.sleep(1)

    print("3. Samsung Galaxy S20 which costs £545.00")
    time.sleep(1)

    purchase_choice = input("\nwhat phone would you like to purchase, select either 1, 2 or 3 \n>>>")

    #...
    if purchase_choice == "1":
        cost_of_phone = 600.00
        #change made here
        cost_of_contract = 0
        cost_upfront = 0
        phone_name = "iphone 11"
        print("Great choice " + phone_name + ".")

    elif purchase_choice == "2":
        cost_of_phone = 494.95
        #change made here
        cost_of_contract = 0
        cost_upfront = 0
        phone_name = "Samsung Galaxy S10"
        print("Great choice " + phone_name + ".")

    elif purchase_choice == "3":
        cost_of_phone = 545.00
        #change made here
        cost_of_contract = 0
        cost_upfront = 0
        phone_name = "Samsung Galaxy S20"
        print("Great choice " + phone_name + ".")
    else:
        print("Sorry this isn't a valid number")
        exit()

def contract():
  #change made here
    global cost_of_contract
    global cost_upfront
    global cost_of_phone
    print("\nYou have chosen to form a contract")
    print("1. iphone 11 with unlimited calls, texts and 4G date for 12months. £100 upfront + 30p/m.")# using a script 'print' to showcase different phone options
    time.sleep(1)

    print("2. Samsung Galaxy with unlimited calls, texts and 4G data. Only for 12 months and costs £30 p/m.")
    time.sleep(1)

    print("3. Samsung Galaxy with unlimited calls, texts and 4G data. £45 upfront and 30p/m for 12months.")
    time.sleep(1)

    contract_choice = input("\nWhat contract would you like to have? Please select either 1, 2 or 3.\n>>>")

    if contract_choice == "1":
        contract = "iphone 11"
        cost_upfront = 100.00
        cost_of_contract = 30*12
        #change made here
        cost_of_phone = 0
        print("Great choice " + contract + ".")

    elif contract_choice == "2":
        contract = "Samsung Galaxy S10"
        cost_upfront = 0
        cost_of_contract = 30*12
        #change made here
        cost_of_phone = 0
        print("Great choice " + contract + ".")

    elif contract_choice == "3":
        contract = "Samsung Galaxy S20"
        cost_upfront = 45.00
        cost_of_contract = 30*12
        #change made here
        cost_of_phone = 0
        print("Great choice " + contract + ".")

    else:
        print("sorry this number is invalid")
        exit()

transaction_type = input("\nWould you like to purchase a phone or form a contract? Enter [p] or [c].\n>>>")

if transaction_type == "p" or transaction_type == "P":
    purchase()
elif transaction_type == "c" or transaction_type == "C":
    contract()
else:
    exit()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Accessories~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("would you like to have accessories along with your phone?")

def discount():
  #change made here
    global cost_of_accessory
    print("\nYou have chosen to purchase an accessory along with your non-contract phone.")
    print("1. Apple watch")
    time.sleep(1)

    print("2. Bluetooth Headset")
    time.sleep(1)

    discount_accessory = input("\nsince you purchased your phone you get 20% off your accessory's so what accessory would you like. Select 1 or 2.\n>>>")
                               
    if discount_accessory == "1":
        cost_of_accessory = 0.8*150# should give the price after the 20% is calculated
        accessory_name = "Apple Watch"
        print("Great choice " + accessory_name + ".")

    elif discount_accessory == "2":
        cost_of_accessory = 0.8*80.00
        accessory_name = "Bluetooth Headset"
        print("Great choice " + accessory_name + ".")

    else:
        print("Sorry this isn't a valid number")
        exit()

#it's being used to mark the start of a function
def full():
    global cost_of_accessory
    print("\nYou have chosen to purchase an accessory. Select which accessory you would like to buy 1 or 2.\n>>>")
    print("1. Apple watch that costs £150")
    time.sleep(1)

    print("2. Bluetooth Headset that costs £80")
    time.sleep(1)


    full_price_accessory = input("\nWhat accessory would you like to have? Please select either 1 or 2.\n>>>")

    if full_price_accessory == "1":
         cost_of_accessory = 150.00
         accessory_name = "Apple Watch"
         print("Great choice " + accessory_name + ".")

    elif full_price_accessory == "2":
         cost_of_accessory = 80.00
         accessory_name = "Bluetooth Headset"
         print("Great choice " + accessory_name + ".")

    else:
         print("sorry this number is invalid")
         exit()#close program if criteria is not met

transaction_type = input("\nWould you like to purchase a accessory with a purchase phone (discount) or contract phone (full price)? Enter [discount] or [full price].\n>>>")

if transaction_type == "discount" or transaction_type == "Discount":
    discount()
elif transaction_type == "full price" or transaction_type == "Full orice":
    full()
else:
    exit()#transaction
    
    
#................................................................................................


print("Loading")
time.sleep(0.5)

print("Printing receipt. Almost there!")
time.sleep(0.5)

#Final part of the program calculates the total costs and carries out addition then outputs it as a receipt to the user
totalsum = cost_of_contract + cost_upfront + cost_of_accessory 
totalsumofphone = cost_of_phone + (cost_of_accessory * 0.8)


time.sleep(1)

print("---------Receipt---------")
print("Name: " + customername)
print("Surname:" + customersurname)
print("Address:" + customeraddress)
print("Purchase: £",cost_of_phone)
print("contract: £",cost_of_contract)
print("upfront: £",cost_upfront)
print("Accessory: £",cost_of_accessory)
print("Payment (Contract):""£",totalsum)
print("payment (Purchase):""£",totalsumofphone)
print("The total cost is £",totalsum)
print("The total cost is £",totalsumofphone)
print("--------------------------")
os.system("pause")
