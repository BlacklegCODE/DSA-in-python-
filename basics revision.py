name = input("Enter the name here:")

if "Mr" in name:
    print("You are a man, married man !")

elif "Mrs" in name:
    print("You are a woman, married woman !")
else:
    print("You need to have at least one initial like mr or mrs!")


#for loop revision:

for i in range(5,50):
    if i %2 == 0:
        print(i)
    elif i % 2 == 1:
        print(i)
#range usage:
print(list(range(5,50,5)))

for i in range(1,20,1):
    if i > 18:
        print("Digits after 18")
    elif i < 18:
        print("digits before 18")
        print(i)
        
        
