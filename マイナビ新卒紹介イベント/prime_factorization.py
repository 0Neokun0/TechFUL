def get_prime_factors(n):
    i = 2
    prime_factors = []
    while i*i <= n:
        if n%i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    
    if n>1:
        prime_factors.append(n)
    
    return prime_factors

# Read number from user
number = int(input())

# Function call
prime_factors = get_prime_factors(number)

# Displaying prime factors
print( *prime_factors, sep=" ")