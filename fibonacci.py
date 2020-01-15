def load_positive_number(minimum=1):
    while True:
        text = input()
        try:
            number = int(text)
        except ValueError:
            print("Error: Value must be a number.")
        else:
            if number >= minimum:
                return number
            else:
                print("Error: Value must be at least %d." % minimum)
        print("Try again: ", end="")


def main():
    print("Please enter from-index: ", end="")
    from_index = load_positive_number()
    print("Please enter to-index: ", end="")
    to_index = load_positive_number(from_index)

    fibonacci = [0, 1]
    for i in range(3, to_index+1):
        current = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(current)
    print(fibonacci[from_index-1:to_index])


if __name__ == "__main__":
    main()
