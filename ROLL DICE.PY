r=[(1,1), (1,2), (1,3), (1,4), (1,5), (1,6),(2,1), (2,2), (2,3), (2,4), (2,5), (2,6),(3,1), (3,2), (3,3), (3,4), (3,5), (3,6),(4,1), (4,2), (4,3), (4,4), (4,5), (4,6),(5,1), (5,2), (5,3), (5,4), (5,5), (5,6),(6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
for i in r:
    a=input("Roll the dice (y/n)? ").upper()
    import random
    i=random.choice(r)
    if  a=="Y" :   
     print(i)
    elif a=="N" :
       print("Thanks for playing ")
       break 
    else:
       print("Invalid Choice")


       
