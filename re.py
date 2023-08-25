from restaurants_data import restaurants_data
import time
from welcome import *

welcome_message()
def welcome_message():
    print("Welcome to the Restaurant Finder!")

def chunked_menu(menu, chunk_size):
    for i in range(0, len(menu), chunk_size):
        yield menu[i:i + chunk_size]

def display_menu(menu):
    for index, chunk in enumerate(chunked_menu(menu, 5), start=1):
        for i, cuisine in enumerate(chunk, start=(index - 1) * 5 + 1):
            print(f"{i}. {cuisine.capitalize()}", end="   ")
        print()

def ask_user_cuisine():
    available_cuisines = list(restaurants_data.keys())

    print("Available cuisines:")
    display_menu(available_cuisines)
    print("-" * 40)
    
    while True:
        user_input = input("Enter the number of the cuisine you want: ")
        if user_input.isdigit():
            user_choice = int(user_input)
            if 1 <= user_choice <= len(available_cuisines):
                selected_cuisine = available_cuisines[user_choice - 1]
                return selected_cuisine
            else:
                print("Invalid choice. Please select a valid number.")
        else:
            print("Invalid input. Please enter a valid number.")

def display_restaurants(cuisine):
    print("Please wait...\n")
    time.sleep(1)
    print(". . .\n")
    print("AH HA I GOT IT")
    if cuisine in restaurants_data:
        restaurants = restaurants_data[cuisine]
        print(f"\n{cuisine.capitalize()} restaurants:")
        restaurant_index = 1
        for restaurant in restaurants:
            print(f"{restaurant_index}. Name: {restaurant['name']}")
            print(f"   Address: {restaurant['address']}")
            print(f"   Rating: {restaurant['rating']}")
            print(f"   Price: {restaurant['price']}")
            print("-" * 40)
            restaurant_index += 1
    else:
        print("No restaurants found for the selected cuisine.")

def main():
    welcome_message()
    
    while True:
        cuisine = ask_user_cuisine()
        display_restaurants(cuisine)
        
        while True:
            repeat = input("Do you want to search for another cuisine? (yes/no): ").lower()
            if repeat == "yes" or repeat == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if repeat == "no":
            break
    
    print("Thank you for using the Restaurant Finder!")
    print("Have a great day and stay safe!")
    print("""
   ,ad8PPPP88b,     ,d88PPPP8ba,
  d8P"      "Y8b, ,d8P"      "Y8b
 dP'           "8a8"           `Yd
 8(              "              )8
 I8                             8I
  Yb,                         ,dP
   "8a,                     ,a8"
     "8a,                 ,a8"
       "Yba             adP"   
         `Y8a         a8P'
           `88,     ,88'
             "8b   d8"
              "8b d8"
               `888'
                 "
          """)
if __name__ == "__main__":
    main()
