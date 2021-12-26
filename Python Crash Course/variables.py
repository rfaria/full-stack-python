def main():  
    name = "John Doe"
    age = 40

    print("The user's name is", name, "and his/her age is", age, end=".\n")
    print("Next year he/she will be", age+1, "years old.", end="\n\n")

    print("The characters of the user's name are:")
    for i in range(len(name)):
        print(name[i].upper(), end=" ")

    print("\nand the squared age is", age**2)

    print("\nIf we replace the user's character O by A we get", name.upper().replace("O","A"))


if __name__ == '__main__':
    main()