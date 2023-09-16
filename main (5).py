# Get the year from the users
year= int (input("Enter a year:"))
# check if it's a leap year
if (year%4==0 and year%100!=0):
  print(f"{year}is a leap year.")
else:
    print(f"{year} is not a leap year.")