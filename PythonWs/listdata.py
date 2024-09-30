#list is used to store multiple data.
#It stores differernt type of data like int, string, float.
#It can also store duplicate value.
#Square braces are used.

#Create list and store your friends' name.
friendsName = ["Tanya", "Anushka", "Agastya", "Priya", 19, 20, 18, 17]

#To access the data from list.
#To get the single data from list -> listVariableName[index].
print(friendsName[3])

#To print the complete list.
for details in friendsName:
    print(details)

#Operation on list.
#append will add the data at the end of the list.
friendsName.append("Mukul")
#To print the complete list.
for details in friendsName:
    print(details)

#insert will add the data based on the index number.
friendsName.insert(0, "Dhruv")
for details in friendsName:
    print(details)
#If the index number does not exist then it will add it at the end of the list.
friendsName.insert(20,"Aryan")
for details in friendsName:
    print(details)

#To remove the data from the list.
#Cannot use index number to remove.
friendsName.remove("Agastya")
for details in friendsName:
    print(details)

#To remove using pop.
#pop removes the end value in list.
#We can provide index value to pop and remove it.
friendsName.pop() #pop(0)
for details in friendsName:
    print(details)

#To reverse the data in list.
friendsName.reverse()
for details in friendsName:
    print(details)

#To remove the complete list use clear.
#friendsName.clear()
#for details in friendsName:
#    print(details)

#To print specific data from list.
for details in friendsName[1:3]: # 1 is the starting index and (3-1) ending index.
    print(details)
print(friendsName)
for details in friendsName[-4:-1]:
    print(details)
for details in friendsName[-4:]:
    print(details)
for details in friendsName[:-1]:
    print(details)
for details in friendsName[:]:
    print(details)

#To add 10 student names in list, remove last value, reverse the list and sort the list.

myList=["Manan","Harsh","Yash"]
type(myList)



  