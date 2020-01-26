def current_age(birth_year, current_year):
    if birth_year > current_year:
        print("you were not born yet.")
    else:
        return current_year - birth_year


bir_year_string = input("Enter your birth year: ")
curr_year_string = input("Input your current year: ")
bir_year = int(bir_year_string)
curr_year = int(curr_year_string)
your_age = current_age(bir_year, curr_year)
print(your_age)
print (f"your age in year {curr_year} is {your_age}")
