import csv
from datetime import datetime
import pprint

import csv
from datetime import datetime


def get_days_between_release_and_sale(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        results = {}
        for i, row in enumerate(reader):
            try:
                release_date = datetime.strptime(row['Release Date'],
                                                 '%m/%d/%Y')
                sale_date = datetime.strptime(row['Order Date'], '%m/%d/%Y')
                days_between = abs((sale_date - release_date).days)
                results[i] = days_between
            except ValueError:
                print(
                    f"Skipping row {i} due to missing or malformed data: {row}")

        f.seek(0)  # Reset file pointer to beginning of file

        # Create a new dictionary mapping sneaker names to days_between values
        sneaker_days = {}
        for row in reader:
            sneaker_name = row['Sneaker Name']
            days_between = results.get(reader.line_num - 2,
                                       None)  # Subtract 2 because of header row and 0-indexing
            if days_between is not None:
                sneaker_days[sneaker_name] = days_between

    return sneaker_days


# TODO: Build a function to calculate purchase date/ release date difference?
#   In our function, we would first compare the year as an int, then month as
#   an int, then day as an int, unless there is already a function to compare
#   dates

# TODO: Total value of shoes sold over their retail value?

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
