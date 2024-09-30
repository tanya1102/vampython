#Dictionary: It can store data in key-value pair.
#It is ordered, no duplicate and changeable. 
#Curly braces and collon are used.

myInfo= {  "Name" : "Tanya Bhardwaj" ,
          "Email" : "tanu@gmail.com" ,
          "Mobile": "7045673240" ,
          "Age" : 25,
          "Name" : "Anushka" #Anushka will overwrite Tanya as no duplicate is allowed.
        }
print(type(myInfo))
print(myInfo["Mobile"])
print(f"My name is {myInfo["Name"]}, I'm {myInfo["Age"]} years old, my mobile number is {myInfo["Mobile"]}, and my email id is {myInfo["Email"]}") #better option
print("My name is ",myInfo["Name"], ",my email id is ",myInfo["Email"], ",my mobile number is",myInfo["Mobile"], "and my age is ",myInfo["Age"])

#Access the complete dictionary key value.
for value in myInfo.values():
    print(value)
for value in myInfo.keys():
    print(value)

#If I want to change the name.
myInfo["Name"]="Tanu"
for value in myInfo.values():
    print(value)

#Update
myInfo.update({"Gender":"Female"})
for value in myInfo.values():
    print(value)

#To delete
myInfo.pop("Name")
for value in myInfo.values():
    print(value)
del myInfo["Email"]
print(myInfo)

