#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""prime numbers"""

from math import floor, sqrt

def main() -> None:
    """main function"""
    num = 30
    print("Following are the prime numbers smaller"),
    print("than or equal to", num)
    print(sieve_or_erasthostanes(num))
    print(is_prime(4))
    print(check_numbers_are_prime([1,2,3,4,5,6,7,8,9]))
    NUMBERS = [17977, 10619863, 106198, 6620830889, 80630964769, 228204732751,
    1171432692373, 1398341745571, 10963707205259, 15285151248481,
    99999199999, 304250263527209, 30425026352720, 10657331232548839,
    10657331232548830,  44560482149, 1746860020068409]
    print(check_numbers_are_prime(NUMBERS))
    return None

def sieve_or_erasthostanes(num):
    """Print all Primes Smaller than or equal to N using Sieve of Eratosthenes"""
    prime = [True for i in range(num+1)]
    # boolean array
    p = 2
    while (p * p <= num):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1 
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(p)

def is_prime(number) -> bool:
    """return true if number is prime, otherwise false"""
    # 1 is a special case of not prime
    if number <= 1:
        return False
    # 2 is a special case of a prime
    if number == 2:
        return True
    # check if the number divides by 2 with no remainder
    if number % 2 == 0:
        return False
    # limit on divisors we test, sqrt of n, +1 so range() will reach it
    limit = floor(sqrt(number)) + 1
    # check for evenly divisible for odd numbers between 3 and sqrt(n)
    for i in range(3, limit, 2):
        # check if number is divisible with no remainder
        if number % i == 0:
            # number is divisible and is not a prime
            return False
    # number is probably prime
    return True

def check_numbers_are_prime(numbers) -> None:
    """chekc if a series of numbers are prime or not"""
    # check each number in turn
    for number in numbers:
        if is_prime(number):
            print(f'{number} is prime')
    return None

if __name__ == "__main__":
    main()
