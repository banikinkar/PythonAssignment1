"""
for i in range(1,6):
    for j in range(1,i+5):
        print('*', end="  ")
    print()

"""

rows = int(input("Enter number of rows: "))

# Outer loop to handle the number of rows
for i in range(rows, 0, -1):
    # Inner loop to print leading spaces
    for j in range(0, rows - i):
        print(end=" ")

    # Inner loop to print stars (2*i - 1 for a centered pyramid)
    for k in range(0, 2 * i - 1):
        print("*", end="")

    # Ending line after each row
    print()