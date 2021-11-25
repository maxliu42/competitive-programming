# The core idea is that of the Pisano period, a period with which the Fibonacci sequence modulo n repeats.
# The Pisano period of 10^9 + 7 can be calculated to be 2*10^9 + 16, therefore input can be taken mod 2*10^9 + 16.
# Then calculate the remainder using a fast method: Fast doubling.
# Fast doubling is an improvement of the matrix exponentiation method using the same identities.

def fibonacci(n):
    if(n == 0):
        return (0, 1)
    else:
        a, b = fibonacci(n // 2) 
        c = a * (b * 2 - a) % 1000000007 
        d = a * a + b * b % 1000000007 
        if(n % 2 == 0):
            return (c, d)
        else:
            return (d, c + d)
n = int(input()) % 2000000016
print(fibonacci(n)[0] % 1000000007)
