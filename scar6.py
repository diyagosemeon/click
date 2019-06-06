a=float(input("enter the element"))
try:
    print("yes")
except (ValueError, TypeError):
    print("No")
