# set comprehension - prime numbers 

def is_prime(x):
    if x == 1 or not x:
        return False
    ct = 0
    for i in range(1, x+1):
        if x % i == 0:
            ct += 1
    return True if ct == 2 else False

print(set(x for x in range(1, 51) if is_prime(x)))