Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('This program calculates and displays travel expenses')
This program calculates and displays travel expenses
>>> Budget=input("Enter Budget:")
Enter Budget:1000
>>> Dest=input("Enter your travel destination:")
Enter your travel destination:Fayetteville
>>> Gas=input("How much do you think you will spend on gas?")
How much do you think you will spend on gas?100
>>> Hotel=input("Approximately, how much will you need for accommodation/hotel?")
Approximately, how much will you need for accommodation/hotel?300
>>> Food=input("Last, how much do you need for food?")
Last, how much do you need for food?100
>>> print('------------Travel Expenses------------')
------------Travel Expenses------------
>>> print("Location:" + Dest)
Location:Fayetteville
>>> print("Initial Budget:" + Budget)
Initial Budget:1000
>>> print("Fuel:" + Gas)
Fuel:100
>>> print("Accommodation:" + Hotel)
Accommodation:300
>>> print("Food:" + Food)
Food:100
>>> Remaining = int(Budget)-(int(Gas)+int(Hotel) + int(Food))
>>> print("Remaining Balance:" +  str(Remaining))
Remaining Balance:500
