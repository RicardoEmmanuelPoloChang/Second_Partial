https://replit.com/join/jyuujnaldk-a00573906
def cost():
  x=(miles/mpg)*price
  return x

print("Enter the you are going to travel distance in miles:")
miles=float(input())
print("Enter the car's miles per gallon (MPG):")
mpg=float(input())
print("Enter the current price of gasoline per gallon:")
price=float(input())
input("Enter the number of days you plan to travel:")

print("Cost of the gas for going that distance: $", cost())
