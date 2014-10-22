# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
    x = raw_input("enter a #:")
    print x
else:
    print("one.py is being imported into another module")