import sqlite3
from tabulate import tabulate
import os
import pandas as pd
import csv
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt


# Creating and connect to database
conn = sqlite3.connect(r'../asset/database/assiment.db')
c = conn.cursor()

# Clear terminal
os.system("cls")

# Create table
c.execute('CREATE TABLE IF NOT EXISTS taco_friday(id INTEGER PRIMARY KEY AUTOINCREMENT, item VARCHAR(55) NOT NULL UNIQUE, price INT(55) NOT NULL)')
conn.commit()

choice = ''


# Color style
COLORS = { \
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\033[0;32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}


# Colors and backgrounds function
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


# Printing out an ASCII file /logo
f = open(r"../asset/logo/start_logo.txt")
ascii = "".join(f.readlines())
print(colorText(ascii))

user_budget = float(input('What is your budget? '))


class TacoFriday:

    def __init__(self):
        pass

    def main_program(self):

        os.system("cls")
        self.display()

        done_var = ''.lower()

        while done_var != 'done':

    # List of options
            self.option_list()

            print("\u001b[34;1m \n")
            choice = input('What do you want? ').lower()

    # Adding new items
            if choice == 'add item':
                self.add_item()
    # See all items
            elif choice == 'all items':
                self.see_items()
    # Updating a item
            elif choice == 'update':
                self.update()
    # Sort after low prices
            elif choice == 'low prices':
                self.sort_low_to_high()
    # Sort after high prices
            elif choice == 'high prices':
                self.sort_high_to_low()
    # Find cheapest item
            elif choice == 'cheapest':
                self.cheapest_item()
    # Find most expensive item
            elif choice == 'expensive':
                self.expensive_item()
    # Find the average price for items
            elif choice == 'average':
                self.average_price()
    # Delete a item
            elif choice == 'delete item':
                self.delete_item()
    # Delete the list
            elif choice == 'delete list':
                self.delete_list()
    # Create a new list
            elif choice == 'new list':
                self.new_item_list()
    # Graph the item prices
            elif choice == 'prices':
                self.check_prices_graph()
    # See your budget
            elif choice == 'budget':
                self.check_budget()
    # Close the program
            elif choice == 'done':
                self.close_program()
                break

    def display(self):

        # Printing out an ASCII file / logo
        f = open(r"../asset/logo/start_logo.txt")
        ascii = "".join(f.readlines())
        print(colorText(ascii))

    def option_list(self):

        # Options
        program_information = {'For adding a new item': 'add item', 'To see all items': 'all items',
                               'Creating a new shopping list': 'new list',
                               'For sorting items from low to high': 'low prices',
                               'For sorting items from high to low': 'high prices',
                               'Check for the cheapest item': 'cheapest', 'Check for the expensive item': 'expensive',
                               'Check for the average price': 'average', 'Update item': 'update',
                               'Deleting a item by item name': 'delete item', 'Deleting the list': 'delete list',
                               'When done enter': 'Done'}

        # Graph options
        visualization_info = {'Graph for your budget': 'budget', 'Graph for the prices of all items': 'prices'}
        instruction = program_information.items()
        visualization = visualization_info.items()

        headers = ['', 'OPTIONS']
        table = tabulate(instruction, headers, tablefmt="github")

        print("\u001b[33;1m")
        visualization_table = tabulate(visualization, headers, tablefmt="github")

        print("\u001b[37m")
        print(table)
        print("\u001b[33;1m")
        print(visualization_table)
        print()

    def add_item(self):

        c.execute('select sum(price) from taco_friday')
        sum_of_price = (c.fetchall())

        print(sum_of_price[0])

        try:
            print("\n \u001b[33;1m")
            item = input('Enter item: ')
            price = float(input('Enter price: '))
            c.execute("insert into taco_friday(item, price) values(?, ?)", (item, price))
            conn.commit()

            print("\u001b[35m", f"Item: {item} with the price: {price} is added to the shopping list")
            print("\u001b[34;1m \n")

        except sqlite3.Error as e:
            print("\n \033[0;31m", e)
            print(f"The item {item} is already in the shopping list!")
            print("\u001b[34;1m \n")

    def see_items(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()
        headers = ['id', 'item', 'price']

        if len(all_items) != 0:

            print("\n \u001b[36m", tabulate(all_items, headers, tablefmt="github"))
            print("\u001b[34;1m \n")

        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def update(self):
        print("\u001b[33;1m")


        c.execute('select * from taco_friday')
        all_items = c.fetchall()
        # Update items
        if len(all_items) !=0:
            update = input('Do you want to update item or price? ').lower()
            if update == 'item':

                try:
                    choice_item = input('What item do you want to update? ')
                    new_item = input('What is the new item name? ')
                    sql = "update taco_friday set item = ? where item = ? "
                    c.execute(sql, (new_item, choice_item))
                    conn.commit()

                    choice_item_price = input('What is the new price of the item? ')
                    sql = "update taco_friday set price= ? where item = ?"
                    c.execute(sql, (choice_item_price, new_item))
                    conn.commit()

                    print("\n \u001b[36m", f"The item name {choice_item} was changed to {new_item} and price is {choice_item_price}")
                    print("\u001b[34;1m \n")

                except sqlite3.Error as e:
                    print("\033[0;31m", e)
                    print("\u001b[34;1m")

            elif update == 'price':

                try:
                    choice_item = str(input('Which item do you want to update the price for?'))
                    new_price = int(input('New price? '))
                    sql = "update taco_friday set price = ? where item = ? "
                    c.execute(sql, (new_price, choice_item))
                    conn.commit()


                    print("\n \u001b[36m", f"The item {choice_item} price was changed to {new_price}")
                    print("\u001b[34;1m \n")


                except sqlite3.Error as e:

                    print("\033[0;31m", e)
                    print("\u001b[34;1m")

        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def sort_low_to_high(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()
        if len(all_items) != 0:
            headers = ['id', 'item', 'price']
            c.execute('Select * from taco_friday order by price ASC')
            filter_prices = c.fetchall()

            print("\n \u001b[36m", tabulate(filter_prices, headers, tablefmt="github", stralign='center', numalign='center'))
            print("\u001b[34;1m \n")

        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def sort_high_to_low(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()
        if len(all_items) != 0:
            headers = ['id', 'item', 'price']

            c.execute('Select * from taco_friday order by price DESC')
            filter_prices = c.fetchall()
            print(f"\n Filter prices from high to low: ")
            print("\u001b[36m", tabulate(filter_prices, headers, tablefmt="orgtbl"))
            print("\u001b[34;1m \n")

        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def cheapest_item(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()
        if len(all_items) != 0:

            c.execute('Select item, price, min(price) from taco_friday')
            min_price = c.fetchone()

            print(f"\n Cheapest item:")
            print("\033[0;32m", min_price[0], min_price[1], 'kr')
            print("\u001b[34;1m \n")

        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def expensive_item(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()

        if len(all_items) != 0:

            c.execute('Select item, price, max(price) from taco_friday')
            max_price = c.fetchone()
            print(f"\n Expensive item:")
            print("\033[0;31m", max_price[0], max_price[1], 'kr')
            print("\u001b[34;1m \n")

        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def average_price(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()

        if len(all_items) != 0:
            c.execute('Select avg(price) from taco_friday')
            avg_price = c.fetchone()

            print("\n \u001b[36m", f"Average price: {avg_price[0]}")
            print("\u001b[34;1m \n")
        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def delete_item(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()
        # Delete items
        if len(all_items) != 0:

            print("\u001b[33;1m")
            choice_item = str(input('Which item do you want to delete? '))

            control = input(f"Are you sure you want to delete {choice_item} from item list? (Type yes or no) ").lower()
            if control == 'yes':
                sql = (f"DELETE from taco_friday where item = ?")
                c.execute(sql, (choice_item,))
                conn.commit()
                print('\n Item is deleted!')
                print("\u001b[34;1m \n")
            else:
                print('\n Nothing is deleted')
                print("\u001b[34;1m \n")
        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def delete_list(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()
        # Delete list
        if len(all_items) != 0:

            print("\033[0;31m")
            control = input('Are you sure you want to delete the shopping list? (yes or no) ').lower()
            if control == 'yes':
                c.execute('DROP TABLE taco_friday')
                c.execute(
                        'CREATE TABLE IF NOT EXISTS taco_friday(id INTEGER primary key AUTOINCREMENT, item varchar(55) not null unique, price int(55) not null)')
                print('')
                print("\u001b[33;1m", 'Shopping list is deleted')
                print("\u001b[34;1m")
                print('')
            else:
                print('')
                print("\u001b[33;1m", 'The list is not deleted')
                print("\u001b[34;1m")
                print('')
        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def new_item_list(self):

        print("\n \u001b[31;1m", 'Alert! All item list will be deleted \n')
        delete_item_list = input('Are you sure you want to create a new item list? (Type Yes or No) ')
        print("\u001b[34;1m \n")

        # Ask if is ok to deleted shopping list
        if delete_item_list == 'yes'.lower():
            c.execute('DROP TABLE taco_friday')
            c.execute(
                    'CREATE TABLE IF NOT EXISTS taco_friday(id INTEGER primary key AUTOINCREMENT, item varchar(55) not null unique, price int(55) not null)')
            print("\u001b[33;1m", 'Old item list deleted.')
            print("\u001b[33;1m", "New item list created!")
            print("\u001b[34;1m \n")
        else:
            print("\n \u001b[33;1m", 'Continue on the same list!')
            print("\u001b[34;1m \n")

    def check_prices_graph(self):

        c.execute('select * from taco_friday')
        all_items = c.fetchall()
        # Graph prices
        if len(all_items) != 0:

            query1 = "select * from taco_friday"

            conne = sqlite3.connect(r'../asset/database/assiment.db', isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
            db_df = pd.read_sql_query(query1, conne)
            db_df.to_csv(r'../asset/csv/items.csv', index=False)

            all_items_df = pd.read_csv(r'../asset/csv/items.csv')

            sns.barplot(x='item', y='price', hue='item', palette='winter', data=all_items_df)
            plt.legend(ncol=2, loc='upper left')

            plt.savefig(r'../asset/images/item_sum.png')
            plt.show()

        else:
            print("\n \033[0;31m", " EMPTY LIST!")
            print("\u001b[34;1m \n")

    def check_budget(self):

        # Create a CSV file with user input
        header = 'budget'
        dataset = {'id': 1, header: user_budget}
        with open(r'../asset/csv/budget_dataset.csv', 'w', newline='') as userinput_file:
            fieldnames = ['id', 'budget']
            writer = csv.DictWriter(userinput_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(dataset)

        # Create a DataFrame from user input CSV file
        budget = pd.read_csv(r'../asset/csv/budget_dataset.csv', sep=',')
        NO_INDEX = DataFrame.reset_index(budget)
        NO_INDEX.index = NO_INDEX['id']
        df = NO_INDEX.drop(['id'], axis=1)

        # Get the budget from DataFrame
        user_data_df = df['budget'][1]

        # All items and prices from database
        query1 = "select * from taco_friday"

        conne = sqlite3.connect(r'../asset/database/assiment.db', isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pd.read_sql_query(query1, conne)
        db_df.to_csv(r'../asset/csv/items_cost.csv', index=False)

        all_items_df = pd.read_csv(r'../asset/csv/items_cost.csv')
        how_many_items = all_items_df['id'].max()
        cost_of_item = all_items_df['price'].sum()

        after_payment = int(user_data_df - cost_of_item)

        subjects = ['cost', 'budget', 'left']
        bar_with = 10


        fig, ax = plt.subplots()
        ax.grid(zorder=0)
        ax.bar(10, cost_of_item, bar_with, color='y', label='cost')
        ax.bar(30, user_data_df, bar_with, color='g', label='budget')
        ax.bar(50, user_data_df - cost_of_item, bar_with, color='r', label='money left')

        plt.title('Visualization of your budget ')

        plt.figtext(0.45, 0.05, f" {user_data_df} - {cost_of_item} = {after_payment}",
                                    bbox=dict(facecolor='red'))


        ax.set_ylabel('money')

        ax.set_xticklabels('')
        ax.legend()
        fig.savefig(r'../asset/images/budget.png')
        plt.show()

        print(
                f"Cost of items is {cost_of_item} and your budget is {user_data_df}. It will be {user_data_df} - {cost_of_item} =",
                user_data_df - cost_of_item)

    def close_program(self):

        print('\u001b[33;1m The program is closed.')

        # Example printing out an ASCII file
        f = open("../asset/logo/close_logo.txt")
        ascii = "".join(f.readlines())
        print(colorText(ascii))
        conn.close()


obj = TacoFriday()
obj.main_program()