# write a python script to merge two python dictionaries.

d1={10:100,20:200,30:300}
d2={40:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i]

print(d1) 

# write a python program to sum all values in a dictionary.

a={10:100,30:300,40:400}
sum=0

for i in a:
    sum=sum+a[i]

print(sum)    

# count the frequency of each element

a=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]

count={}

for i in a:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1

print(count)            

# write a python pogram to combine two dictionary by values for common keys.

d1={10:100,20:200,30:400}
d2={40:400,50:500,60:600}

for i in d2:
    if i in d1.keys():
         d1[i]+=d2[i]
    else:
        d1[i]=d2[i]

print(d1)             