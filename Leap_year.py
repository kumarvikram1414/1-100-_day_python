
#Find Leap Year project

class solution:
    def leap(self,n):
        if(n%4==0):
            if(n%100==0):
                if(n%400==0):
                    return f"year is {n} leap yaer"
                else:
                    return f"year {n} is not leap year"
            else:
                return f"year {n} is leap year"
        else:
            return f"year {n} is not leap year"


    
n=int(input("inter year:"))
y=solution()
m=y.leap(n)
print(m)

        




