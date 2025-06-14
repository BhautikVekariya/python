course="   Python full stack";
print(course);
print(len(course));
print(course[0]);
print(course[-1]);
print(course[0:4]);
print(course[:]);

# format expressions 

# First="john";
# Last="wick";

# Full= f"{(First)} {Last}"

# print(Full.upper());
# print(Full.lower());
# print(Full.title());
# print(Full.find("w"));
# print(course.strip());
# print(Full.replace("j","a"));
# print("full" in course);
# print("program" not in course)

command=" "
while command.lower()!="quit":
    command=input(">")
    print("ECHO",command)

# print the even number
count=0;
for number in range(1,10):
    if number%2==0:
        count +=1
        print(number)
print(f"we have {count} even number")