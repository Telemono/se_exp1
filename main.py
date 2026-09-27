from calc import add, sub


def main():
    print("mini calculator")
    print("1 add")
    print("2 sub")
    x = float(input("a = "))
    y = float(input("b = "))
    op = input("op = ")

    if op == "1":
        print(add(x, y))
    elif op == "2":
        print(sub(x, y))
    else:
        print("unsupported")


if __name__ == "__main__":
    main()