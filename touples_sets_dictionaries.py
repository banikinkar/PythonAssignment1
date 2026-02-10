"""
t1 = ("Java",10,14,1.5,True,[1,2],(10,20,40))
print(type(t1))

t2 = "Python",2,3
print(type(t2))
print(t2)
t3 = [1,2,3,4,5]

t4 = tuple(t3)
print(type(t3),type(t4))

"""
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
