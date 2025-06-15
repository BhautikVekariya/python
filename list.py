# print positive and negative number are the separate

a=[2,3,4,5,-2,-3,-4,-5]

print("positive element are")

for i in a:
    if i>=0:
        print(i)

print("negative element are:-")

for i in a:
    if i<=0:
        print(i)

# mean value print

b=[1,2,3,4,5,6,7]
sum=0
for i in b:
    sum=sum+i

print(sum/len(b))  
