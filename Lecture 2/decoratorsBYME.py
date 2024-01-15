def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")
# hello funcn is wrapped around the announce decorator

hello()

# So again, why did that work? It's because our Hello function that just printed 'hello, world" is wrapped inside of this Announce decorator,
# where what the Announce decorator does, is it takes our Hello function of input and gets us a new function that first prints an alert warning that we're
# about to run the function, actually runs the function, and then prints another message. So, a bit of a simple example here.