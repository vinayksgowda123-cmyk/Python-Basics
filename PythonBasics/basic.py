# for i in range(10):
#     print(i)

# name="vinay K s"
# name=input("enter ur name")
# print("my name is",name)

# a=int(input("enter value of a"))
# b=int(input("enter value of b"))

# if a>b:
#     print("a is grater")
# elif a<b:
#     print("b is grater")
# else:
#     print("both are equal")        

# for i in range(5):
#     print(i,end=' ')
# print()

# count=0

# while count<5:
#     print(count,end=' ')
#     count+=1

# a=int(input("enter a value of a"))
# b=int(input("enter value of b"))
# def add(a,b):
#     return a+b
# print(add(a,b))

# list=[12,34,34,43,23,43]
# list.append(100)
# list.remove(34)
# list.insert(2,38)
# list.sort(reverse=True)
# list.pop()
# print(len(list))

# for item in list:
#    # if item%2==0:
#         print(item,end=' ')

# for index,item in enumerate(list,2):
#     print(index,item)

# print(list)

# print(list[2:4])
# print(list[::-1])
# print(list[-3:])
# list.reverse()
# print(list)


#t=(2,3232,2323,232,32,3)


# d={"name":"vinay","age":24,"city":"banglore"}

# print(d["age"])
# print(d.get("name"))
# print(d)

# for key in d:
#     print(key,d[key])

s={2,3,4,5,65,4,34,6,8}
s1={100,200,300,1}

print(s)
s.add(100)
print(s)
s.remove(34)
print(s)

s.update({200,300})

print(s)

print("union od s and s1",s.union(s1))
print("Intersection of s and s1",s.intersection(s1))

for item in s:
    print(item,end=' ')


