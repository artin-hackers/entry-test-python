print("Yo Cholo! Gimme numba: ", end="")
number = input()
while True:
    try:
        if int(number) > 0:
            the_sum = 0
            for i in range(1, int(number)+1):
                the_sum += i
            print("Da sum is %d, mon." % the_sum)
            break
        else:
            print("No negatives or zeroes. Try again: ", end="")
            number = input()
    except ValueError:
        print("Wut is dat?! Again: ", end="")
        number = input()
