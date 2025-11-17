list1=[1,2,3,4,5,6,7,5,34]
d=set()
s=set()
for item in list1:
    if item in s:
        d.add(item)
    else:
        s.add(item)

result=[item for item in list1 if item not in d]
print(result)
