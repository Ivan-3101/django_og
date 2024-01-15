from functions import square
# if we want to use a function that is inside another file
# then we need to import the file

for i in range(10):
    print(f"The square of {i} is {square(i)}")



# if only "import functions" was used
# then the function call would be: "functions.square(i)"