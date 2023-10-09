https://replit.com/join/iqhirqqlra-a00573906

import random

print("Choose your character:")
print("1. Hunter")
print("2. Warlock")
print("3. Titan")

type=int(input())

if type == 1:
  print("You are now a Hunter")
elif type == 2:
  print("You are now a Warlock")
elif type == 3: 
  print("You are now a Titan")

print("You encounter a dragon. Roll a 20-sided dice to determine your success")

print("You roll the dice")

number=int(random.randint(1,20))
print("You rolled", number)
if number<16:
  print("you failed, the dragon burned you to a crisp")
else:
  print("congrats, you slayed the dragon")
