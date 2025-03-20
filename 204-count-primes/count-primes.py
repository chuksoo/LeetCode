class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Apply Sieve of Eratosthenes
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                # Mark all multiples of p as non-prime
                for multiple in range(p*p, n, p):
                    is_prime[multiple] = False

        return sum(is_prime)

        