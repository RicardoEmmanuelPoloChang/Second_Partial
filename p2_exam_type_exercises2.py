https://replit.com/join/kedkskzsmu-a00573906

def discount1():
  x=price*0.90
  return x
def discount2():
  x=price*0.95
  return x
def discount3():
  x=price*0.98
  return x

def extra1():
  x=discount1()*0.95
  return x

def extra2():
  x=discount2()*0.95
  return x

def extra3():
  x=discount3()*0.95
  return x

print("What category of product are you buying?1,2 or 3?")
category=float(input())
print("give me the total price:")
price=float(input())
print("And how many units did you buy?")
units=int(input())

if category== 1:
  print("then you´ll price be of", discount1(), "dollars")
  if units>10:
    print("Great you bought more than 10 units, you´ll have an extra 5% discount")
    print("and now your price is:",extra1())
  
elif category== 2:
  print("then you´ll price be of", discount2(), "dollars")
  if units>10:
    print("Great you bought more than 10 units, you´ll have an extra 5% discount")
    print("and now your price is:",extra2())
  
elif category== 3:
  print("then your price will be of", discount3(), "dollars")
  if units>10:
    print("Great you bought more than 10 units, you´ll have an extra 5% discount")
    print("and now your price is:",extra3())
