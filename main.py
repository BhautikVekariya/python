# a=12
# a=str(a)
# print(a)

# b="12"
# b=int(b)
# print(type(b))

# gen=input("you can enter the male or female M & F :-")

# if gen == "M":
#       print("Good Morning Sir")
# else:
#       print("Good Morning Maam")      

# # while loop

# a=1

# while a <=20:
#       a+=1

#       print(a)


# # seperate the number of the select

# # num =int(input("enter your number"))

# # while num > 0:
# #       print(num%10)
# #       num=num//10

# # reverse the number of the select the number

# # num = int(input("enter your number"))
# # rev=0
# # while num > 0:
# #       rev=rev * 10 + num % 10
# #       num=num // 10
# # print(rev)      
      
# # palindrom the number of the select the number

# # num=int(input("enter your number:-"))
# # copy=num
# # rev=0

# # while num >0:
# #       rev=rev*10+ num%10
# #       num=num//10

# # if copy==num:
# #       print("the number is palindrome")
# # else:
# #       print("the number is not palli")       



# n=int(input("enter your number:-"))
# # fact=1

# # for i in range(1,n+1):
# #       fact=fact*i
# # print(f"factorial of the {fact}")
# fact=1
# i=1

# while i<=n:
#       fact*=i
#       i+=1
# print(fact)

# # function

# def num(a,b=45):
#       print(f"sum of the value {a+b}")

# num(5)

# def palindrome(st):
#       rev=""
#       for i in range(len(st)-1,-1,-1):
#           rev+=st[i]

#       if rev==st:
#             print(f"{st} it is palindrome")
#       else:
#             print(f"{st} it is not palindrome")                  


# palindrome("NAMAN")
# palindrome("CURSOR")

# for row in range(1,6):
#       print("1"* row)

# for row in range(1,6):
#     for star in range(1,row+1):
#         print("*",end=" ")
#     print()   

# row = 1
# while row <= 6:
#     print("*" * row)
#     row += 1

def star():
    for row in range(1,6):
        for star in range(1,row+1):
           print("*",end=" ")
    print()    

star()


      




     
      

