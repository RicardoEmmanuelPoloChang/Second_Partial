https://replit.com/join/kvneldqnea-a00573906

print("What day is today? write it with lower case")
day = str(input())
#temperature
temperature = int(input("Tell me the ambient temperature:"))
if temperature >= 20 and temperature <= 25:
  print("Those are good conditions")
elif temperature < 20:
  print("Bring it inside the house")
elif temperature > 25:
  print("Bring it inside the house and turn on the fan")

#watering

if day== "tuesday" or day== "thursday" or day== "saturday":
  print ("Today is", day, ",Water Ruby")
else:
  print("Today is not necesary to water Ruby, unless humidity is low")

#Humidity

print("Tell me the humidity percentage of Ruby:")
humid= int(input())
if humid < 20:
  print("You shoud water Ruby")
elif humid >= 20 and humid <= 22:
  print("Suitable humidity")
elif humid > 25 and day== "tuesday" or day== "thursday" or day== "saturday":
  print("It is not necesary to water Ruby")

print("Thank you for taking care of Ruby")
