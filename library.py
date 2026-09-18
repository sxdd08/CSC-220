from math import sqrt

def exclude_nonprimes(n):
    if n < 2: 
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return True

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
           
def get_integer(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("You cannot leave this space blank.")   
        elif value[0] in "+-":
            if value[1:].isdigit():
                return int(value)
        elif value.isdigit():
            return int(value)
        else:
            print("Please enter an integer.")

def confirm_input(start, end):
    if start < 1 or end < 1:
        print("Please enter a positive number greater than 0.")
        return False
    if start > end:
        print("The starting number must be less than or equal to the ending number.")
        return False
    else:
        return True

def count_primes(start, end):
    count = 0
    for num in range(start, end +1):
        if is_prime(num):
            count += 1
        else:
            continue
    return count


def count_gaps(start, end):
    gaps = 0
    for num in range(start, end +1):
        if is_prime(num):
            gaps += 1
        else:
            continue
    return gaps - 1 if gaps > 0 else 0

def determine_largest_prime_gap(start, end):
    previous_prime = None
    largest_gap = 0
    first_prime = None
    second_prime = None
    for num in range(start, end +1):
        if is_prime(num):
            if previous_prime is not None:
                gap = num - previous_prime
                if gap > largest_gap:
                    largest_gap = gap
                    first_prime = previous_prime
                    second_prime = num
            previous_prime = num
    return largest_gap, first_prime, second_prime



if __name__ == "__main__":
    print("")
