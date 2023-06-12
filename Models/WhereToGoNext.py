import pprint
import csv
from datetime import datetime

def get_days_between_release_and_sale(csv_file):
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        results = {}
        for i, row in enumerate(reader):
            try:
                release_date = datetime.strptime(row['Release Date'],
                                                 '%m/%d/%y')
                sale_date = datetime.strptime(row['Order Date'], '%m/%d/%y')
                days_between = abs((sale_date - release_date).days)
                results[i] = days_between

    return days_between

# TODO: Build a function to calculate purchase date/ release date difference?
#   In our function, we would first compare the year as an int, then month as
#   an int, then day as an int, unless there is already a function to compare
#   dates

# TODO: Total value of shoes sold over their retail value?
#   PLANNING:
#   https://stackoverflow.com/questions/48906098/adding-numbers-in-a-csv-file-python-code
#   https://www.w3schools.com/python/python_dictionaries_add.asp
#   https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php
#   All we need is shoe model, original price, and retail price. So...
#   ----------------------------------------------------------------------------------------------------------
#   dataframe = dataframe.drop(['Order Date', 'Brand', 'Release Date', 'Shoe Size', 'Buyer Region'], axis=1)
#   profit = {}
#   for each shoe model:
#       retailSum = sum('Retail Price' of each pair sold)
#       saleSum = sum('Sale Price' of each pair sold)
#       profit['Sneaker Name'] = str(saleSum - retailSum)
#   print(profit)
#   def sort_dict_by_value(d, reverse=False): <-- arranging so the values are in ascending order.
#       return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
#   sort_dict_by_value(profit)
#   arrange/sort profit from greatest to least.
#   print("Most Profit" + str(profit[5])
#   print("Least Profit" + str(profit[-5])
#

# TODO: How long after the release date was the shoe sold?
#   Along with this, we can also see how often they were sold, or in other
#   words,
#   what was the time period between each sell?

# TODO: What are the most and least popular shoes within each category? If
#   we can figure this out, we can figure out which values to exclude from our
#   model
def main():
    csv_file = '/Users/tyrellbaker/PycharmProjects/StockX/resources/stockx.csv'
    sneaker_days = get_days_between_release_and_sale(csv_file)

    for sneaker, days in sneaker_days.items():
        print(f"Sneaker: {sneaker}\nDays between release and sale: {days}\n")

if __name__ == '__main__':
    main()
