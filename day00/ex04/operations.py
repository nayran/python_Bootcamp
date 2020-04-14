import sys


if (len(sys.argv) < 3):
    print("InputError: too few arguments")
    print("Usage: python operations.py <number1> <number2>")
    print("\nExample:\n\tpython operations.py 10 3")
elif (len(sys.argv) > 3):
    print("InputError: too many arguments")
    print("Usage: python operations.py <number1> <number2>")
    print("\nExample:\n\tpython operations.py 10 3")
elif sys.argv[1].isdigit() is False:
    print("InputError: only numbers")
    print("Usage: python operations.py <number1> <number2>")
    print("\nExample:\n\tpython operations.py 10 3")
elif sys.argv[2].isdigit() is False:
    print("InputError: only numbers")
    print("Usage: python operations.py <number1> <number2>")
    print("\nExample:\n\tpython operations.py 10 3")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum:     ", a + b)
    print("Diff:    ", a - b)
    print("Prod:    ", a * b)
    if (b == 0):
        print("Quot:    ERROR (div by zero)")
        print("Remain:  ERROR (modulo by zero)")
    else:
        print("Quot:    ", a / b)
        print("Remain:  ", a % b)
