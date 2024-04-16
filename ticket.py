# ticket distribution among persion based on height 

#if height is less then 120 cm then they are eligible

#if age is <12,12=~18 ,or above 18

#if <12 then $5 if 12-18 then $7 if above 18 then $12

#if the want photos then add $3

#return full bill and name



"""class ride:
    def ticket(self,height,age,p):
        co=0
        if height<1200:
            print("you can ride ")
        else:
            return "You'r Nor Eligble"
        if age<12:
            co=5
            return f"Your bill: $5"
        elif age>12:
            co=7
            return f"Your bill :$7"
        elif age>18:
            co=12
            return f"Your bill :$12"
    
        if p=="Y":
            co +=3
   

re=ride()

height=int(input("Enter Your Height:"))
age=int(input("\nEnter Your Age:"))
p=str(input("\nYou want picture's ( Y or N):"))

ya=re.ticket(height,age,p)"""

height=int(input("Enter Your Height:"))
if height<1200:
    print("you can ride ")
else:
    
    print("You'r Nor Eligble")
    break


age=int(input("\nEnter Your Age:"))
co=0

if age<12:
    co=5
    print( f"Your bill: $5")
elif age>12:
    co=7
    print("Your bill :$7")
elif age>18:
    co=12
    print("Your bill :$12")
else:
    print("Your age is not")
p=input("\nYou want picture's ( Y or N):")
if p=="Y":
    co +=3

print(f"Your bill :${co}")
   



