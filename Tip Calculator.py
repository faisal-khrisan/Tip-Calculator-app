k="y"
while k=="y" or k== "Y" :
    print("Welcome to the tip calculator!")
    total= float (input ("What was the total bill?\n$ "))
    Tip= float (input ("How much tip would you like to give ? 10, 12 or 15 "))
    people= int (input ("How many people to split the bill? "))
    Tip_percentage =Tip/100
    amount_should_pay= round((total/people)*(1+Tip_percentage),2)
    if people ==1 :
        print (f"The amount you should pay is : ${amount_should_pay}")
    else:
        print(f"Each person should pay : ${amount_should_pay}")
    k=input("Would you like to continue? y / n")
print("Thank you for using our tip calculator")


