b=0

try:
    a=10/b
    print(a)
    print("try completed")
except ZeroDivisionError:
    print("can't divide by zero")
print("prg completed")