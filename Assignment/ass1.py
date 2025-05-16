
#1

print("\nQ.1")

a = int(input("\nEnter a number : "))

if(a%2==0):
 print("Number is Even.")
else:
 print("Number is Odd.")

'''

#2

print("\nQ.2")

a = int(input("\nEnter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

print()

if(a>b and a>c):
 print("A is largest.")
elif(b>a and b>c):
 print("B is largest.")
else:
 print("C is largest.")



#3

print("\nQ.3")

year = int(input("\nEnter a Year : "))

if(year%4==0 and year%100!=0 or year%400==0):
 print(f"{year} is a leap year.")
else:
 print(f"{year} is not a leap year.")



#4

print("\nQ.4")

per = int(input("\nEnter you Percentage : "))

print()

if(per>=90):
 print("Contgrats! You got Grade A.")
elif(per>=80):
 print("You got Grade B.")
elif(per>=70):
 print("You got Grade C.")
elif(per>=60):
 print("You got Grade D.")
else:
 print("You got Grade F.")



#5

print("\nQ.5")

char = input("\nEnter a Letter : ")

print()

if(char=="a" or char=="e" or char=="i" or char=="o" or char=="u"):
 print(f"{char} is a vowel.")
else:
 print(f"{char} is a consonant.")



#6

print("\nQ.6")

a = int(input("\nEnter First Number : "))
b = int(input("Enter Second Number : "))

op = input("\nEnter the Operation Which you ahve to perform : ")

print()

if(op=="+"):
 print(f"The Sum of {a} and {b} is {a+b}.")
elif(op=="-"):
 print(f"The Difference betwwen {a} and {b} is {a-b}.")
elif(op=="*"):
 print(f"The Multiplication of {a} and {b} is {a*b}.")
elif(op=="/"):
 print(f"The Division of {a} and {b} is {a/b}.")
else:
 print("Invalid Operation!!")



#7

print("\nQ.7")

num = int(input("\nEnter a number : "))

print()

if(num>0):
 print("Number is Positive.")
elif(num<0):
 print("Number is Negetive.")
else:
 print("Number is Zero.")



#8

print("\nQ.8")

pre = "admin"
prepass = "1234"

user = input("\nEnter Username : ")
password = input("Enter Password : ")

if(pre==user and prepass==password):
 print("\nLogin Successfull...")
else:
 print("\nLogin Failed!")



#9

print("\nQ.9")

a = int(input("\nEnter the First Side : "))
b = int(input("Enter the Second Side : "))
c = int(input("Enter the Third Side : "))

if(a+b > c and b+c>a and a+c>b):
 print("This is a Perfect Triangle.")
else: 
 print("This is not a Perfect Triangle.")



#10

print("\nQ.10")

weight = float(input("\nEnter your Weight(in kg) : "))
height = float(input("Enter your Height(in m) : "))

height = height%100

bmi = ((weight)/(height**2))

print(f"Your BMI is {bmi}.")

if(bmi > 30):
 print("OBESITY!!!")
elif(bmi >= 25 and bmi < 29.9):
 print("You are Overweight.")
elif(bmi >= 18.5 and bmi < 24.9):
 print("You have Normal Weight.")
else:
 print("You are Underweight.")



#11

print("\nQ.11")

price = int(input("\nEnter the price of Product : "))

if(price > 1000):
 discount = 0.1
elif(price > 500 and price <= 1000):
 discount = 0.05
else:
 discount = 0.0

final = price - (price * discount)

print(f"The Final Price After applying {discount} discount Rs. {final}")



#12

print("\nQ.12")

month = input("\nEnter the Month : ").lower()
year = int(input("Enter the Year : "))

if(month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december"):
 print(f"No. of days in {month} are 31")
elif(month=="april" or month=="june" or month=="september" or month=="november"):
 print(f"No. of days in {month} are 30")
elif(month=="february"):
 if(year%4==0 and year%100!=0 or year%400==0):
  print(f"No. of days in {month} are 29")
 else:
  print(f"No. of days in {month} are 28")
else:
 print("Invalid Month!")



#13

print("\nQ.13")

balance = int(input("\nEnter your Balance : "))

print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n")

choice = int(input("\nEnter your Choice : "))

if(choice == 1):
 print(f"\nYour current balance is {balance}.")
elif(choice == 2):
 deposit = int(input("\nEnter the Amount : "))
 balance += deposit
 print(f"Your amount has been successfully deposited. Current Balance : Rs.{balance}")
elif(choice == 3):
 withdraw = int(input("\nEnter the Amount : "))
 balance -= withdraw
 if(balance < 0):
  balance = 0
  print(f"Account Empty!!. Current Balance : Rs.{balance}.")
 else:
  print(f"Your amount has been successfully withdrawn. Current Balance : Rs.{balance}")	
else:
 print("Invalid choice!")

print("\nThank you for Choosing Us..")



#14

print("\nQ.14")

age = int(input("\nEnter your Age : "))

if(age >= 60):
 print("Senior..")
elif(age >= 20 and age <= 59):
 print("Adult..")
elif(age >= 13 and age <= 19):
 print("Teenager..")
elif(age >=5  and age <= 12):
 print("Child..")
elif(age >= 2 and age <= 4):
 print("Toddler..")
elif(age <= 1):
 print("Infant..")
else:
 print("Invalid Age!!")



#15

print("\nQ.15")

choice = int(input("\nEnter your Choice : "))

if(choice == 1):
 print("Monday..")
elif(choice == 2):
 print("Tuesday..")
elif(choice == 3):
 print("Wednesday..")
elif(choice == 4):
 print("Thursday..")
elif(choice == 5):
 print("Friday..")
elif(choice == 6):
 print("Saturday..")
elif(choice == 7):
 print("Sunday..")
else:
 print("Enter a valid choice..!?!")

'''