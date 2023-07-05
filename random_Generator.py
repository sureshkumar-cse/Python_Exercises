# Random Generator
# Generate a random integer and a List of integers has length upto that random integer

import random

def generate_input():
    n = random.randint(1, 10)
    a = [random.randint(1, 10) for _ in range(n)]
    a.sort()
    x = a[random.randint(0, n - 1)]
    return a, x
    
# output = generate_input()
# print(output)
