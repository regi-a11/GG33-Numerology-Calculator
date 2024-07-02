# Define a function to calculate the sum of digits of a number
def sum_of_digits(n):
  # Check if the number is a master number
  if n in [11, 22, 33]:
    return n
  s = 0
  while n > 0:
    s += n % 10
    n //= 10
  return s

# Define a function to check if a date is valid
def is_valid_date(d, m, y):
  # Check if the year is in the range of 2000 to 2100
  if y < 2000 or y > 2100:
    return False
  # Check if the month is in the range of 1 to 12
  if m < 1 or m > 12:
    return False
  # Check the number of days in each month
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # Check for leap year
  if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    days_in_month[1] = 29
  # Check if the day is in the frange of 1 to the number of days in the month
  if d < 1 or d > days_in_month[m - 1]:
    return False
  # If all the conditions are satisfied, return True
  return True

# Define a function to find dates that have a given sum of digits
def find_dates(sum):
  # Create an empty list to store the dates
  dates = []
  # Loop through all the possible years from 2000 to 2100
  for y in range(2000, 2101):
    # Loop through all the possible months from 1 to 12
    for m in range(1, 13):
      # Loop through all the possible days from 1 to 31
      for d in range(1, 32):
        # Check if the date is valid
        if is_valid_date(d, m, y):
          # Check if the sum of digits of the date is equal to the given sum
          if sum_of_digits(d) + sum_of_digits(m) + sum_of_digits(y) == sum:
            # Convert the date to a string in the format of DD MM YYYY
            date = f"{d:02d} {m:02d} {y:04d}"
            # Check if the date has any master number in it
            if d in [11, 22, 33] or m in [11, 22, 33] or y in [11, 22, 33]:
              # Highlight the date with asterisks
              date = f"**{date}**"
            # Append the date to the list
            dates.append(date)
  # Return the list of dates
  return dates

# Ask the user to enter the sum of digits they want to find
sum = int(input("Enter the sum of digits you want to find: "))
# Call the function to find the dates that have the given sum of digits
dates = find_dates(sum)
# Print the number of dates found
print(f"There are {len(dates)} dates that have a sum of {sum} when you add up the digits.")
# Print the dates found
for date in dates:
  print(date)
