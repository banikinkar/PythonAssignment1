"""
Principal, Rate of Interest and Tenure must be known to calculate simple interest s =prt/100
compound interest = A - p OR C.I = P[(1+R/100)^T-1]
"""
p = float(input("Enter the principal amount :"))
r = float(input("Enter the rate of interest :"))
t=float(input("Enter the tenure :"))

simple_interest = (p * r * t) /100
compound_interest = p * ((1+(r/100)) ** t - 1)

print("Simple Interest is :" , round(simple_interest,2))
print("Compound Interest is :" , round(compound_interest,2))