import math



while True:
    int_input = int(input("Number: "))
    sqrt_int = int(math.sqrt(int_input)).__floor__()

    if int_input == 2 or int_input == 3:
        print(str(int_input) + " is prime number")
    elif int_input == 1:
        print(str(int_input) + " is not prime number")

    for i in range(2, sqrt_int + 1):
        if int_input % i == 0:
            print(str(int_input) + " is not prime number")
            break
        else:
            if i == sqrt_int:
                print(str(int_input) + " is prime number")