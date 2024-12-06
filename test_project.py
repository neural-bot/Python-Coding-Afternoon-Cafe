import pytest
import pyfiglet
from project import banner, food_table, take_order

# Mock data for testing
mock_menu = [
    {"Food": "Pizza", "Price($)": 12.99},
    {"Food": "Burger", "Price($)": 9.99},
    {"Food": "Pasta", "Price($)": 11.49}
]

# Helper function to simulate input
def mock_input(monkeypatch, inputs):
    def input_gen(_):
        return inputs.pop(0)
    monkeypatch.setattr('builtins.input', input_gen)

# Test for food_table function
def test_food_table(monkeypatch):
    # Mock CSV content
    filename = "mock_food_menu.csv"
    with open(filename, 'w') as f:
        f.write("Food,Price($)\nPizza,12.99\nBurger,9.99\nPasta,11.49\n")

    # Assert the food_table function returns the expected data
    assert food_table(filename) == mock_menu

# Test for take_order function
def test_take_order(monkeypatch):
    # Mock the input to simulate ordering process
    inputs = ["Pizza", "2", "Burger", "1", "done"]
    mock_input(monkeypatch, inputs)
    
    # Mock CSV content
    filename = "mock_food_menu.csv"
    with open(filename, 'w') as f:
        f.write("Food,Price($)\nPizza,12.99\nBurger,9.99\nPasta,11.49\n")

    # Assert the take_order function returns the expected total price
    assert take_order(filename) == 35.97  # 2*12.99 + 1*9.99

def test_banner():
    expected_output = pyfiglet.figlet_format("Welcome, PyCafe")
    actual_output = banner()
    assert actual_output == expected_output

if __name__ == "__main__":
    pytest.main()
