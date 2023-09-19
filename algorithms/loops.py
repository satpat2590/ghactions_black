class Loops():
    def __init__(self):
        pass

    def prime_summation(self, x):
        # Loop through from 2 to x - 1
        for i in range(2, (x // 2) + 1):
            if self.is_prime(i) and self.is_prime(x - i):
                print(f"{i} + {x - i} = {x} ; Where both numbers in the summation are primes.\n")


    def is_prime(self, x):
        # Loop through from 2 to x - 1. If x is divisible by any number in that range, return False (not prime)
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                return False
        # None of the numbers in the range are factors. x is therefore prime. 
        return True
    

loop = Loops()

loop.prime_summation(10)
