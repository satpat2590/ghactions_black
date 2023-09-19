import timeit 
import dis

class Loops():
    def __init__(self):
        pass

    def prime_summation(self, x):
        # Loop through from 2 to x - 1
        for i in range(2, (x // 2) + 1):
            if self.is_prime(i) and self.is_prime(x - i):
                print(
                    f"{i} + {x - i} = {x} ; Where both numbers in the summation are primes.\n"
                )

    def is_prime(self, x):
        if x < 2:
            return False
        # Loop through from 2 to x - 1. If x is divisible by any number in that range, return False (not prime)
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                return False
        # None of the numbers in the range are factors. x is therefore prime.
        return True


loop = Loops()

#loop.prime_summation(10)


# Taking average time to complete list comprehension vs vanilla loop 

def comprehensive_loop():
    return [x for x in range(2, 100) if loop.is_prime(x)]

def vanilla_loop():
    prime_list2 = []
    for x in range(2, 100):
        if loop.is_prime(x): 
            prime_list2.append(x)
    return prime_list2

def average_time(stringfunc): 
    sum = 0
    for x in range(20):
        sum += timeit.timeit(stringfunc, globals=globals(), number=1000)
    return sum / 20

comp = "comprehensive_loop()"
van = "vanilla_loop()"


print(f"Average time taken for comprehensive_loop: {average_time(comp)} seconds")
print(f"Average time taken for vanilla_loop: {average_time(van)} seconds")
print(f"Average time taken for standalone: {average_time('[x for x in range(2, 100) if loop.is_prime(x)]')} seconds", "\n\n")

# Disassemble function to bytecode

dis.dis(comprehensive_loop)
print("\n\n\n\n")
dis.dis(vanilla_loop)