
import json
from string import whitespace
from tkinter.font import names

with open('locations.json', 'r') as f:
    locations = json.load(f)


user_data = {}
def login():

     name=input("input your name: ")
     address=input("input your address: ")
     def_pwd = name+"@"+address
     user_data["Name"]=name
     user_data["Address"]=address
     trial = 3
     while True:
         password = input("input you password: ")

         if password == def_pwd:
             user_data["Pass_word"]=password
             print("Granted")
             break
         else:
             trial-=1
             if trial > 0:
                print(f"you have {trial}")
             else:
                 print("illegal user")
                 break
     return user_data
order_data = {}
def get():

    while True:
        location= input("input you location ").capitalize()
        user_data["Location"]=location
        if locations.get(location):
            restaurant = list(locations[location].keys())
            res_names = " ,".join(restaurant)
            print(f"restaurant in you location are {res_names.upper()}")
        while True:
            res_order = input("enter your restaurant")
            menu=locations[location][res_order]
            if res_order in res_names:
                print("-"*8, "Menu of ",res_order,"-"*8)
                for food ,price in menu[f"menu_{res_order}"].items():
                    print("---",food,"      ",price,"---")
                print("-" * 8, "Menu of ", "-" * 8)
            else:
                print("Please enter valid restaurant")
            food = list(menu[f"menu_{res_order}"].keys())
            " ".join(food).upper()

            while True:

                order_food = input("Place your order (or type '0' to cancel): ").upper().strip()
                if order_food == '0':
                    return
                if order_food in food:
                    try:
                        amount=int(input("How much"))
                        if amount > 0:
                            food_price =menu[f"menu_{res_order}"][order_food]
                            total_price = amount*food_price

                        else:
                            print("order somethin bruv")
                    except:
                        print("Input valid amount")

                    if order_food not in order_data:

                        order_data[order_food] = {
                            "Quantity": amount,
                            "price": total_price
                        }

                        # Debugging output after update
                    else:
                        # order_data[order_food]={
                        #     "quantity":amount,
                        #     "price": total_price
                        # }
                        order_data[order_food]["Quantity"] += amount
                        order_data[order_food]["price"] += total_price

                else:
                    print("Out of menu, Please order from the menu")
        else:
            print("Please Enter valid location")
    return order_data




def main(user_data,order_data):
   login()
   get()
   print('-' * 6, "Customer Data", '-' * 6)
   for user,data in user_data.items():
       print(f"--{user}        {data}")
   for item,detail in order_data.items():
       print(f"Item:  {item}")
       for key,value in detail.items():
           print(f"     {key}:{value}")


if __name__=='__main__':
    main(user_data,order_data)
