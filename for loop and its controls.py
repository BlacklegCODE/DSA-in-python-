#  break statement practice:
 for i in range(1,10):
     if i == 5:
         break
     print(i)

#Continue statement practice:

for i in range(1,11):
    if i == 5 or i == 3:
        continue
    print(i)

#pass usage practice:

 for i in range(1,11):
     if i == 2 or i == 6:
         pass
     else:
         print(i)
