
"""
Sets are sequential amd do not store duplicates
it is written within {} and are mutable in nature
trying to create a set with duplicate items ,still set would be created with distinct elements
"""

l1 = [1,2,3,3,2,2,1,4]
#print(set(l1))
#print(l1)
s1 = {2,1.5,"Java"}
num1 = {3,5}
print(2 in s1)
s2= s1.union(num1)
s3=num1.union(s1)
print(s2)
print(s3)