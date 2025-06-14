# prime number using for loop
num =int(input("Enter a number:-"))

for i in range(2,num//2+1):
     if num %i ==0:
        print("not prime")
        break
else:
     print("prime")   

#prime number using while loop
num = int(input("Enter a number: "))
i=2
while i<=num//2:
        if num %i==0:
            print("not prime")
            break
        i+=1
else:
      print("prime")            

                
