sieve = [True] * 101
for i in range(2, 100):
    if sieve[i]:
        print(f"{i} is prime")
        for j in range(i*i, 100, i):
            sieve[j] = False