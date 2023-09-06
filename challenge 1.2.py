import calendar
def leap_year(y):
  if calendar.isleap(y):
    print(y,"is a leap year")
  else:
    print(y,"is not a leap year")
y=int(input("Enter a year:"))
z= leap_year(y)
print(z)
        