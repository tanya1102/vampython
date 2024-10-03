#try:
#     error
#catch:
#     type of error

#print(x):- Name error
try:
    print(x)
except NameError:
    print("x not defined")

# y=1/0
# print(y):- Zero division error
try:
    y=1/0
    print(y)
except ZeroDivisionError:
    print("Zero division error")

# a="Tanya"
# b=int(a):- Value error
# print(b)
try:
    a="Tanya"
    b=int(a)
    print(b)
except ValueError:
    print("String not cast in int")

# import os
# os.remove("myfile.txt"):- File not found error
import os
try:
    os.remove("myfile.txt")
except FileNotFoundError:
    print("File does not exist")

# mylist=["Pawan", "Manan", "Kanak"]
# print(mylist[4]):- Index error
mylist=["Pawan", "Manan", "Kanak"]
try:
    print(mylist[4])
except IndexError:
    print("Index out of range")

x=5
if x>5: #Indentation error cannot be solved using try so correct the error by correcting the indentation.
   print(x)
else:
   print(x)
# x=5
# try:
    # if x>5:
    # print(x)
    # else:
    # print(x)
# except IndentationError:
    # print("Indentation error")

# x="Pawan"
# y=4
# c= x+y:-Type error
# print(c)
x="Pawan"
y=4
try:
    c=x+y
    print(c)
except TypeError:
    print("Concatenate only str")
finally: #The code in this will run even if there is error or not.
    print("Always run")


