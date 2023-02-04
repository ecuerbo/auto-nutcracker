def announce(f):
    def wrapper():
        print("About to run athe function...")
        f()
        print("Done with the Function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()