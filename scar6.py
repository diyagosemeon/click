a=float(input())
try:
    print("yes")
except (ValueError, TypeError):
    print("No")
