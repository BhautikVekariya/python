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


# find the largest element in the list

c=[34,23,56,89,23,98]
largest=0
index=0

for i in range(len(c)):
    if c[i] > largest:
        largest=c[i]
        index=i
    

print(f"your largest nubmer is {largest} at index {index}")


# find the second largest element in the list

d=[12,34,5,12,53,35]

largest=d[0]
sec_larg=d[0]

for i in d:
    if i > largest:
        sec_larg=largest
        largest=i
    elif i > sec_larg:
        sec_larg=i

print(largest,sec_larg)

# find the element the sorted or not

e=[12,13,14,15]

for i in range(len(e)-1):
    if e[i] < e[i+1]:
        continue
    else:
         print("Your list is not sorted")

else:
    print("Your list is sorted")         