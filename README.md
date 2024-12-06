# PyCafe Menu and Ordering System ☕
### Video Demo:  <https://youtu.be/kyk3BNCzKZ4>
## Description:

***PyCafe*** is a simple application that computes the total order cost, shows a menu of available foods, and accepts customer orders. The purpose of this project is to demonstrate fundamental Python ideas and capabilities, like file management, input from users, and data processing. The user is prompted to enter the food products along with their quantities. In addition to determining the total cost based on the goods and amounts ordered, it verifies if the submitted food item is available on the menu. The user is prompted again and again until they input "done."

## Table of Contents

- [Features](#features)
- [Dependencies](#dependencies)
- [Function Descriptions](#function-descriptions)


## Features

- **Display Menu**: Shows the available food items and their prices.
- **Order Taking**: Allows users to input their desired food items and quantities.
- **Total Calculation**: Calculates and displays the total price of the order.


## Dependencies

 -   **pyfiglet** - Used for generating stylized ASCII art.
 -   **tabulate** - Used for formatting tables in the console.
 -   **csv** - Used for reading the menu data from a CSV file.


## Function Descriptions

### 1. main()

 -   **Purpose:** The main function orchestrates the workflow of the application.
    
 -   **Actions:**
     -   Displays a welcome message in ASCII art.
     -  Reads the food menu from a CSV file and prints it in a formatted table.
     -  Prompts the user to place an order and calculates the total price of the order.
     - Displays the total order price.

### 2. banner()
 -   **Purpose:** Displays a welcome message with shop name in ASCII art.  
 -   **Returns:** str: as ASCII art.

### 3. food_table(filename)
 -   **Purpose:** Reads the food menu from a CSV file and returns it as a list of dictionaries.
 -   **Parameters:**
     -   *filename (str):* The name of the CSV file containing the food menu.
 -   **Returns:**
     -   *list of dict:* Each dictionary contains Food and Price($) as keys.
    Details:
        Reads the CSV file using csv.DictReader.
        Converts the price from string to float to ensure accurate price calculations.

### 4. take_order(filename)
 -   **Purpose:** Handles user input to take food orders and calculates the total price.
 -   **Parameters:**
      -   *filename (str):* The name of the CSV file containing the food menu.
 -   **Returns:**
     -   float: The total price of the user's order.
