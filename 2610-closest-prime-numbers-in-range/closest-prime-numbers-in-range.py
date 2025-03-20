class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = self.sieve_of_eratosthenes(right)
        
        primes = [num for num in range(left, right + 1) if is_prime[num]]

        if len(primes) < 2:
            return [-1, -1]

        min_gap = float('inf')
        best_pair = [-1, -1]

        for i in range(len(primes) - 1):
            gap = primes[i+1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                best_pair = [primes[i], primes[i+1]]
        return best_pair

    def sieve_of_eratosthenes(self, n):
        """Return a list `is_prime` where is_prime[i] is True if i is prime."""
        is_prime = [True]*(n+1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p*p <= n:
            if is_prime[p]:
                for multiple in range(p*p, n+1, p):
                    is_prime[multiple] = False
            p += 1
        return is_prime


        
      
        
        