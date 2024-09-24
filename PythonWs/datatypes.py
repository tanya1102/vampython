#Data type is used to defined the data is in which form.

#int datatype is used to store numeric data type.
#Note- In python we don't need to declare the datatype.
#We just assign the value in variable.
#Variable can store any type of value.
age = 19
name = "Tanya Bhardwaj"
salary = 2599.89

#How to pass the variables inside print statement 
#We have three ways to pass the variable in print statement.
#print("My name is " + name + " and salary is ", + salary + " and age is " + age)
#It generates the type error as string only concatenates with string and not int.
#Solution 1:- Replace + by , when data type is not string.
print("My name is " + name + " ,salary is ", salary, " and age is ", age)
#Solution 2:- Pass the variable in print statement with f{}.
print(f"My name is {name} ,salary is {salary} and age is {age}")
#Solution 3:- Typecast the data type into string
salaryString = str(salary)
ageString = str(age)
print("My name is "+ name + " and salary "+ salaryString+ " and age "+ ageString)

#To find the type of data we need to use type() function.
print(type(name))
print(type(age))
print(type(salary))