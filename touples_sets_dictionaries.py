"""
t1 = ("Java",10,14,1.5,True,[1,2],(10,20,40))
print(type(t1))

t2 = "Python",2,3
print(type(t2))
print(t2)
t3 = [1,2,3,4,5]

t4 = tuple(t3)
print(type(t3),type(t4))


##concatenition repetition membership in tuple

t1 = 100,20,10,10
t2 = 7,100,90
smallest = min(t1,t2)
biggest = max(t1,t2)
total = sum (smallest)
#print(smallest)
#print(biggest)
#print(total)
#print(t1*2+t2*3)
#print(40 in t1)
print(t1.count(1),t1.index(10),t1[2]) ## count check, index check and element in index check


##mutability & immutability
t1 = 100,20,10,10

fruits = ['apple', 'banana', 'orange']
#print(id(fruits))
fruits.append([1,2,3])
#print(id(fruits),id(t1))
#print(fruits)

## add(), remove() discard()
s1 = {2,3,4,8.0,10,11}
s1.add(11)
#print(s1)
s1.remove(3)
#print(s1)
s1.discard(50)
#print(s1)

## mathematical operations

student1 = {"English","Math","Physics","Chemistry"}
student2 = {"Oriya","English","Chemistry","Math"}

common_suject = student1.intersection(student2)
print(common_suject)
common_subject= student1 & student2
print(common_subject)

extra_subject = student2.difference(student1)
print(extra_subject)
#extra_subject = student1.difference(student2)
extra_subject = student1 - student2
print(extra_subject)

"""


###Frozen sets
s1 = {2,3,4,8.0,10.0,11}
fs1 =frozenset({10,20,30})
#print(fs1, type(fs1))
fs2 = frozenset({20,10.0,30.0,30})
fs3 = fs1  & s1 & fs2
print(fs3)

fs1.add(5)
print(fs1)


















