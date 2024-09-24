#We have to use if-else condition for decision making in python.
#To check whether you are eligible for voting or not.
#Get the age from user.
userAge = int(input("Enter your age "))
#To be eligible for voting then age must be above 18.

if userAge > 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

#Check whether the user is eligible for vote or super vote.
#Super voter age should be greater than 55.
#Normal voter age should be more than 18 and less than 55.
if userAge > 18 and userAge < 55:
    print("You are eligible for voting")
elif userAge > 55:
    print("You are eligible to super vote")
else:
    print("You are not eligible to vote")