#for loop is used to complete the iteration or repeating the task.
name = input("Enter your name ")
#Iterate my name using for loop.
#e.g. in C for(int i = 0; i< 10; i++)
for i in name:
    print(i) 

#Print the number 1 to 10
for x in range(1, 11):
    print(x)    

#Print this pattern using for loop 1 3 5 7 9 11 solve by size.
for x in range(1, 12, 2): #2 is step size
    print(x)

#Print this pattern using for loop 1 3 5 7 9 11 solve.
for x in range(1, 12): 
    if x % 2 !=0:
        print(x)
    
#Print the even and odd numbers using for loop from 1 to 20
for x in range(1, 21):
    if x % 2 !=0:
        print("Odd number: ",x)
    else:
        print("Even number: ",x) 
        
