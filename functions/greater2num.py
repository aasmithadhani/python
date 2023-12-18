a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
maximum = lambda a, b: a if a > b else b
print(f"Maximum of {a} and {b} is {maximum(a, b)}.")
