import one
print("Top Level two.py")

one.func()

if __name__ == '__main__':
    print("two.py being run directly")
else:
    print("two.py is being imported")