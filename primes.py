import math


def load_positive_number():
    while True:
        text = input()
        try:
            number = int(text)
        except ValueError:
            print("Error: Value must be a number.")
        else:
            if number > 0:
                return number
            else:
                print("Error: Value cannot be negative or zero.")
        print("Please, try again: ", end="")


def main():
    print("Please enter position of a prime that you would like to see: ",
          end="")
    position = load_positive_number()

    primes = [2, 3]
    number = 3
    while len(primes) < position:
        number += 2
        for divisor in range(2, int(math.sqrt(number))+1):
            if number % divisor == 0:
                break
        else:
            primes.append(number)
    print("Your prime is", primes[position-1])


if __name__ == "__main__":
    main()
