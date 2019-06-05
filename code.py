# 1. Prime flag function

def is_prime(num):
    """
    Flags whether the number (num) is prime
    """
    if num > 1:
        if num == 2:
            return True
        elif num % 2 == 0:
            return False
        for divisor in range(3, int(num**(1/2)+1), 2):
            if num % divisor == 0:
                return False
        return True
    return False


# 2. Generate the next prime

def gen_prime():
    """
    Generates the next prime number
    """
    yield 2
    num = 3
    while True:
        if is_prime(num):
            yield num

        num += 2


# 3. Ask for input

def main():
    """
    Asks the user for input
    """
    generator = gen_prime()
    
    while True:
        answer = input("Would you like to see the next prime? (Y/N): ")
        
        if answer.upper().startswith("Y"):
            print("{} is the next prime number.".format(next(generator)))
        elif answer.upper().startswith("N"):
            break
        else:
            continue
        
if __name__ == '__main__':
    main()
