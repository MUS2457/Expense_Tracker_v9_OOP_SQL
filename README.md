Expense Tracker v9

A simple command-line expense tracker built with Python and SQLite.

This project allows users to record shopping expenses, store them in a database, and run different types of analysis on the data such as totals, averages, category statistics, and budget checks.

The program is designed with a modular structure, separating data models, database logic, input handling, and analysis tools.

What the Program Can Do
Add Expenses

Users can enter multiple expenses during a session by providing:

product name
category
price

Input validation prevents invalid data such as empty names, digits in names, or negative prices.

After entering expenses, the user can choose whether to save them to the database or keep them only for analysis.

General Expense Analysis

After entering expenses, the program shows a summary including:

total money spent
number of items purchased
average product price
Category Analysis

The program also analyzes spending by category:

total spending per category
number of items in each category
average price per category
categories above the global average
categories below the global average
Product Analysis

The program compares products based on price:

products above the global average price
products below the global average price
most expensive product
cheapest product
Search Expenses by Date

The program can search the database for expenses recorded on a specific date.

It displays:

all products purchased that day
category of each product
price
total spending for that date
Budget Checker

Users can select a date range and enter a budget.

The program calculates the total spending in that range and shows whether the user:

stayed within the budget
or exceeded it
Monthly Expense Report

Users can search expenses by month.

The program displays:

total spending for that month
categories involved
products purchased in each category
Project Structure
ExpenseTracker/

DATA/
    SQL.py
    class_methods.py
    input_data.py

LOGIC/
    calculations.py
    utility.py

main.py
DATA

Contains components related to data management.

SQL.py

Handles database operations:

create database connection
create table
insert expenses

class_methods.py

Defines the Expense class and helper methods used for:

total spending
average calculation
category totals

input_data.py

Handles user input and performs validation before creating expense objects.

LOGIC

Contains the program’s analysis and search logic.

calculations.py

Includes functions that analyze expense data such as:

price comparisons
averages
category statistics
highest and lowest spending

utility.py

Contains database-based tools:

search expenses by date
monthly expense reports
budget checker
main.py

The entry point of the program.

It provides a simple CLI menu where the user can choose actions like:

1 - Enter new expenses
2 - Search shopping by date
3 - Budget checker
4 - Search expenses by month
5 - Exit
Technologies Used
Python
SQLite
Object-Oriented Programming
Modular project structure
Command Line Interface (CLI)
Why I Built This

This project was built to practice:

structuring Python projects into multiple modules
working with SQLite databases
performing data analysis with Python
designing command-line applications
Possible Future Improvements

Some ideas for future versions:

editing or deleting expenses
exporting reports to CSV
adding charts for spending analysis
category budget limits
graphical interface version
