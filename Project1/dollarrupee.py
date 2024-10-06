#Create a python program to convert dollar into rupees and vice versa.

#To convert rupees in USD:-

rupeeCurrency = float(input("Enter value in rupees: "))
USDCurrency = rupeeCurrency / 84
print("In Usd: ", USDCurrency) 

#To convert USD in rupees:-

USDCurrency = float(input("Enter value in USD: "))
rupeeCurrency = USDCurrency * 84
print("In Rupees: ", rupeeCurrency)