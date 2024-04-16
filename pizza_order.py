print ("-----Welcome to pizza DELIVERY-----\n")

bill=0
size_of_p=input("What size of pizza you need : 'S','M','L'--> ")

if size_of_p=="S":
    bill=15

if size_of_p=="M":
    bill=20

if size_of_p=="L":
    bill=25

Add_pep=input("Do you want to have Peporoni:Y or N :")

if Add_pep=="Y":
    bill +=2

extra_ch=input("Do you want extra chess:Y or N:")
if extra_ch=="Y":
    bill+=3

print(f"You'r Total bill is:${bill} ")
                    