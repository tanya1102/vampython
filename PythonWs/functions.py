#function can perform any task and it can be reused anytime.
def printName():
    print("My function name is print ")

#function calling
printName()

#Argument function and parameter function.
def myAge(age):
    print("My age is ", age)

myAge(19)

#Area of square using function.
area = int(input("Enter square side"))

def areaSquare(a):
    print("Area is ",(a*a))
areaSquare(area)

#Area of square
area = int(input("Enter square side"))
def areaSquare(a):
    return a*a
output = areaSquare(area)
print("Area is ", output)


