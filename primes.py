counter = 0
for number in range(2, 21):
    divisible = False
    for divisor in range(2, number):
        if number % divisor == 0:
            divisible = True
    if divisible == False:
        counter += 1
        if counter == 6:
            print(number)
