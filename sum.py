print("Gimme numba:")
number = input()
if int(number) > 0:
    my_sum = 0
    for i in range(1, int(number)+1):
        my_sum += i;
    print(my_sum)
else:
    print("We do not like negatives or zeroes")
