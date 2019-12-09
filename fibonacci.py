print("Hello, World!")

# Pocatek Fibonacciho rady: 1, 1, 2, 3, 5, 8, 13, ...

lastlast = 1  # Cislo na 1. pozici
last = 1  # Cislo na 2. pozici

for i in range(3, 25):  # Vypocet zahajime na 3. pozici, protoze 1. a 2. jiz zname
    new = lastlast + last  # Nove cislo se vypocte jako soucet dvou predchozich
    print(new)  # Vytiskneme nove cislo
    lastlast = last  # Ulozime posledni cislo na predposledni pozici
    last = new  # Ulozime nove vypoctene cislo na posledni pozici
