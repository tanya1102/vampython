#Typecasting convert one data type to another data Typecasting

price = 90.59
print(price)
print(type(price))

#Convert to integer
payPrice = int(price)
print(payPrice)
print(type(payPrice))

#Convert int to string
amount = 2599
stringAmount = str(amount) 
print(stringAmount, "and datatype is ", type(stringAmount))

#Convert string to int
#gender = "Male"
# Ctrl+/ is used to comment 
#genderIntoInt = int(gender)
#Conversion not possible because string does not have ascii number
# print(gender, " data type is ", genderIntoInt)

#To take the input from user C language scanf
myName = input("Enter your name")
# Input function has default return type as string
myAge = int(input("Enter your age")) 
print("My name is ", myName ,"and age is ", myAge)

#Find the age in years when bornYear and currentYear given by user
currentYear = int(input("Enter year "))
bornYear = int(input("Enter born year "))
myAge = bornYear - currentYear
print("Age", myAge)

#Currency convertor ruppee to USD:- 1 usd = 84 rs
