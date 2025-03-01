#first case :

print("welcome to paython pizza deliveries")
size=input("enter size of your pizza: S ,M,L :").upper()
price={"S":15 ,"M":20,"L":25 }
total_bill=price.get(size,0)
add_peproni=input("do you want peproni? (Y/N):").upper()
extra_cheese=input("do you want cheese? (Y/N):").upper()
if add_peproni=="Y":
    if size=="S":
        total_bill+=2
    else:
        total_bill+=3
if extra_cheese=="Y":
    total_bill+=1
print("thank you for choosing paython pizza deliveries ")
print("your total bill is:$ ",total_bill)
#########################################################################################################################
# Second case :
points=int(input("please Enter your points:"))
if 1<=points>=50:
    prize="wooden rabbit"
elif 51<=points>=150:
    prize=None
elif 151<=points>=180:
    prize="wafer_thin mint"
elif 181<=points>=200:
    prize="penguin"
else:
    prize=None
if prize:
    result=f"congratulations : you won a {prize}"
    print(result)
else:
    print(" oh dear, no prize this time ")
 ############################################################################################
 #third case:
number=int(input("please enter the number:"))
if number %2==0:
    print(number,"is even")
else:
    print(number,"is odd")




