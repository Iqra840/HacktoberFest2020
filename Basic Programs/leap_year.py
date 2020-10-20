# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
#If a year is multiple of 400, then it is a leap year
    if (year % 100) == 0:
    #If a year is muliple of 100, then it is a leap year
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
           #If a year is multiple of 400, then it is a leap year
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
