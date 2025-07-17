# PART 1


# TASK 1: WRITE A PROGRAM USING A FOR LOOP TO PRINT THE SQUARE OF NUMBERS FROM 1 TO 8

# using a for loop to go through numbers 1 to 8
for i in range(1, 9):
    # print the square (i times i)
    print(i**2)



# TASK 2: Define a function check_grades (grades) that: Takes a list of numbers(grades). For each grade, prints: "Pass" if the grade is 60 or more. "Fail" otherwise. Test it with a list of at least 5 grades.

# DEFINE A FUNCTION TO CHECK GRADES
def check_grades(grades):
    for grade in grades:
        if grade >= 60:
            print("Pass")  # if grade is 60 or more itll say pass
        else:
            print("Fail")  # if grade is less than 60 itll say fail

# testing it with 5 grades
check_grades([55, 72, 61, 40, 88])



# TASK 3: Write a function count_vowels (text) that counts the number of vowels (a, e, i, o, u) in a given string. Print the count and also print how many times each vowel appears. Your string: "It's easy to lie with statistics. It's hard to tell the truth without statistics." Andrejs Dunkels

# DEFINE FUNCTION TO COUNT VOWELS. TEXT
def count_vowels(text):
    # vowels we're looking for
    vowels = "aeiou"
    
    # make the text lowercase so "A" and "a" are treated the same
    text = text.lower()
    
    #this will store how many vowels total
    total = 0
    
    # this will store how many times each vowel shows up
    vowel_counts = {}

    # go through each letter in the text one by one
    for char in text:
        # if the letter is a vowel
        if char in vowels:
            #add 1 to the total vowel count
            total += 1

            # if we've already seen this vowel, add 1 to its count
            if char in vowel_counts:
                vowel_counts[char] += 1
            else:
                # if it's the first time seeing this vowel, start counting from 1
                vowel_counts[char] = 1

    # after we finish going through the text, show the total number of vowels
    print("Total vowels:", total)

    # now we go through the dictionary and show each vowel and how many times it appeared
    for v, c in vowel_counts.items():
        print(v, "→", c, "times")

# testing the function with the sentence from the task
count_vowels("It’s easy to lie with statistics. It’s hard to tell the truth without statistics.")



# TASK 4: You are designing a simple data collection tool where users keep entering numbers until they decide to stop. This is useful in real-life scenarios such as survey inputs, form data, or sensor readings. Write a program that:
# 1. Asks the user to enter numbers one by one.
# 2. Keeps storing them in a list.
# 3. The loop continues until the user enters "done" (case insensitive).
# 4. After exiting the loop, the program prints:The total number of values entered and The average of the numbers (rounded to 2 decimal places).
# Skip empty inputs or non-numeric entries with a message like "Invalid input. Try again." Use a while loop.

# i make an empty list to store the numbers the user gives us
numbers = []

# this loop will keep going forever until we break it
while True:
    # ask the user to type a number or "done"
    user_input = input("Enter a number (or 'done' to finish): ")

    # if the user types "done", we stop the loop
    if user_input.lower() == "done":
        break  # this breaks out of the while loop

    # now we try to convert what they typed into a number
    try:
        # if its a number, we change it to float and it can be a decimal
        number = float(user_input)
        #  we add it to our list
        numbers.append(number)
    except:
        # if the user typed something that's not a number, show this message
        print("Invalid number. Try again")

# once we're done asking for input, we check if the list has numbers
if len(numbers) > 0:
    # sum() adds up all the numbers in the list
    total = sum(numbers)
    # we divide total by how many numbers the user gave us
    average = round(total / len(numbers), 2)  # round to 2 decimal places for clean output

    # print both results
    print("Total:", total)
    print("Average:", average)
else:
    # if never entered any valid number
    print("You didn't enter any valid numbers.")



# TASK 5: You are analyzing customer purchase data where each customer can make multiple purchases. The data is stored in a list of tuples like this [("Alice", 120), ("Bob", 80), ("Alice", 50), ("Bob", 20), ("Clara", 200)] Write a program that:
# 1. Iterates over the list of purchases.
# 2. Stores total purchases per customer using a dictionary.
# 3. Prints out how much each customer spent in total.
# Expected Output Example:
# Alice spent $170
# Bob spent $100 ...

#  this is a list of purchases, each one is a (name, amount) pair
purchases = [("Alice", 120), ("Bob", 80), ("Alice", 50), ("Bob", 20), ("Clara", 200)]

# this is to make an empty dictionary to keep track of totals for each customer
totals = {}

# we go through each item in the purchases list
for name, amount in purchases:
    # if the customer's name is already in the dictionary
    if name in totals:
        # we add the new amount to their existing total
        totals[name] += amount
    else:
        # if its the first time we see this customer, we start their total
        totals[name] = amount

# now we print how much each customer spent
# we go through each item in the totals dictionary
for person, total in totals.items():
    # print the name and the total they spent
    print(person, "spent $", total)



# TASK 6: Use the wbdata package to get Population data for the country: India from 2015 to 2020. Print the results in a readable way (country, year, population)
##FIRST METHOD
# import wbdata  ##to get the data
# import datetime  ##to set date ranges

##country code INDIA
# country = "IND"

##population indicator code from World Bank
# indicator = {"SP.POP.TOTL": "Population"}

##set the years from 2015 to 2020
# start = datetime.datetime(2015, 1, 1) ##start year
# end = datetime.datetime(2020, 1, 1) ##end year

##get the data using the wbdata lib
# data = wbdata.get_dataframe(indicator, country=country, data_date=(start, end))

##print what we got
# print("Population of India from 2015 to 2020:")
# print(data)



# TASK 6: Use the wbdata package to get Population data for the country: India from 2015 to 2020. Print the results in a readable way (country, year, population)
# FIRST METHOD COULDNT WORK ON MY MCBOOK, I USED THIS METHOD INSTEAD

import requests  # this lets us make internet requests to get data
import pandas as pd  # importing panda for working with tables and DataFrames

# the link from the World Bank API that gives India's population from 2010 to 2020
url = "https://api.worldbank.org/v2/country/IND/indicator/SP.POP.TOTL?date=2010:2020&format=json"

# we send a GET request to the link and turn the response into JSON format
response = requests.get(url).json()

# the actual population data is in the second part of the response (index 1)
population_data = response[1]

# now we go through the data and make a list of dictionaries
# each one will have the year, country name, and the population
data_list = []
for item in population_data:
    # sometimes the value can be None (empty), so we skip those
    if item["value"] is not None:
        # we make a dictionary with year, country name, and population as a number
        data_list.append({
            "Year": int(item["date"]),  # year as a number
            "Country": item["country"]["value"],  # like "India"
            "Population": int(item["value"])  # convert the population to a number
        })

# to turn the list into a table (DataFrame) using pandas
df = pd.DataFrame(data_list)

# sort the table by year so it goes from 2010 → 2020
df = df.sort_values(by="Year")

# now to go through each row in the table and print it nicely
for _, row in df.iterrows():
    # row["Country"] is the name, row["Year"] is the year, row["Population"] is the number
    print(f"{row['Country']}, {row['Year']}: Population = {row['Population']}")

#I used this on terminal to test and run the code : /opt/anaconda3/bin/python "/Users/stephanie/Downloads/ABI SAAB final exam part 1.py"
