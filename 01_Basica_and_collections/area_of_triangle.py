"""
Area of a normal triangle : square root of (s*(s-a)*(s-b)*(s-c))
Area of a right angle triangle 1/2 ab
"""
a = float(input("Enter first side :"))
b = float(input("Enter second side :"))
c = float(input("Enter third side :"))

# semiperimeter
s= (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
area_rat = 0.5 *a*b
print("Area of Triangle is : ",round(area,2))
print("area of right angled triangle is : ",round(area_rat,2))