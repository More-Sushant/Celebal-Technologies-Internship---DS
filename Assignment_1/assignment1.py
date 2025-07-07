def upper(n):
    print("Upper Tringular *\n")
    for i in range(n):
        print("  " * i + "* " * (n - i))
    print("\n")


def lower(n):
    print("Lower Tringular *\n")
    for i in range(1, n + 1):
        print("* " * i)
    print("\n")
def pyra(n):
    print("Pyramid * \n")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1) + " " * (n - i))

n = int(input("Enter a number: "))
upper(n)
lower(n)
pyra(n)