import pyfiglet
import tabulate
import csv

'''
PyCafe Menu and Ordering System

Overview
    This Python script is a simple command-line application for a cafe, PyCafe, which displays a food menu, takes customer orders, and calculates the total order price. It uses pyfiglet for stylized text, tabulate for table formatting, and csv for reading the food menu from a file.

Dependencies
    pyfiglet - Used for generating stylized ASCII art.
    tabulate - Used for formatting tables in the console.
    csv - Used for reading the menu data from a CSV file.
    Function Descriptions

main()
    Purpose: The main function orchestrates the workflow of the application.
    Actions:
        Reads the food menu from a CSV file and prints it in a formatted table.
        Prompts the user to place an order and calculates the total price of the order.
        Displays the total order price.

banner()
    Purpose: Displays a welcome message with shop name in ASCII art.
    Returns: str: as ASCII art.

food_table(filename)
    Purpose: Reads the food menu from a CSV file and returns it as a list of dictionaries.
    Parameters:
        filename (str): The name of the CSV file containing the food menu.
    Returns:
        list of dict: Each dictionary contains Food and Price($) as keys.
    Details:
        Reads the CSV file using csv.DictReader.
        Converts the price from string to float to ensure accurate price calculations.

take_order(filename)
    Purpose: Handles user input to take food orders and calculates the total price.
    Parameters:
        filename (str): The name of the CSV file containing the food menu.
    Returns:
        float: The total price of the user's order.

Details:
    Prompts the user to enter food items and quantities.
    Checks if the entered food item is in the menu.
    Calculates the total price based on the food items and quantities ordered.
    Continues to prompt the user until they type 'done'.
'''

def banner():
    return pyfiglet.figlet_format("Welcome, PyCafe")


def main():
    print(banner())

    filename = "food_menu.csv"

    # Print the food menu
    print(tabulate.tabulate(food_table(filename), headers="keys", tablefmt='grid') + "\n")

    # Take order and calculate total price
    order_total = take_order(filename)
    print(f"\nTotal order price: ${order_total:.2f}\n" + "Thanks for buying ❤️")


def food_table(filename):
    table = []

    with open(filename) as file:
        reader = csv.DictReader(file)
        for line in reader:
            table.append({"Food": line["Food"], "Price($)": float(line["Price($)"])})  # Ensure prices are floats

    return table


def take_order(filename):
    menu = food_table(filename)
    food_items = {item["Food"]: item["Price($)"] for item in menu}
    
    total_price = 0.0
    while True:
        order = input("Enter the food item you want to order (or 'done' to finish): ").title()
        
        if order.lower() == 'done':
            break
        
        if order in food_items:
            quantity = int(input(f"How many {order}(s) would you like? "))
            total_price += food_items[order] * quantity
        else:
            print("Sorry, we don't have that item. Please choose from the menu.")
    
    return total_price


if __name__ == "__main__":
    main()
