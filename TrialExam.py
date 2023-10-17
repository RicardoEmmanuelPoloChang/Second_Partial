number= input("how many students do you have?")
print("You have to input the following data per student")
for i in range(int(number)):
  grade=int(input("Give me their average grade:"))
  participation= str(input("Do they have participation?(lower case yes/no)"))
  prjtscore= int(input("What is their project score?"))
  if grade >= 75 and participation == "yes":
    print("This student is in good academic standing")
  if prjtscore > 90:
    print("This student has a distinction for their project")
  if grade < 60 or participation == "no":
    print("This student needs to improve in their average score or participation")

