e = None
# datatype = NoneType of the above variable

name = input("Enter your name: ")
print("Hello, " + name)

# fstring
print(f"Hello, {name}")

# n = input("Number: ")
# input function always gives back a string
# therefore we have to convert it to a integer
n = int(input("Number: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")


