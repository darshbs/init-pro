MOD = 10**9 + 7

class Solution:
    def countSubsequence(self, arr):
        max_val = max(arr)
        beautiful_numbers = self.get_beautiful_numbers(max_val)
        
        # Count frequency of each number in arr
        freq = {}
        for num in arr:
            if num in beautiful_numbers:
                freq[num] = freq.get(num, 0) + 1
        
        # Generate all subsets of valid beautiful numbers
        valid_nums = list(freq.keys())
        total_subsequences = 0
        
        # Use bitmasking to find all non-empty subsets
        num_valid = len(valid_nums)
        for mask in range(1, 1 << num_valid):  # from 1 to 2^num_valid - 1
            subset_count = 1
            for j in range(num_valid):
                if (mask >> j) & 1:
                    subset_count = (subset_count * (pow(2, freq[valid_nums[j]], MOD) - 1)) % MOD
            total_subsequences = (total_subsequences + subset_count) % MOD
        
        return total_subsequences

    def get_beautiful_numbers(self, limit):
        """Finds all numbers that are prime or semi-prime up to 'limit'."""
        primes, is_prime = self.sieve(limit)
        beautiful_numbers = set(primes)  # Add prime numbers

        # Find all semi-prime numbers (product of at most two primes)
        for i in range(len(primes)):
            for j in range(i, len(primes)):
                semi_prime = primes[i] * primes[j]
                if semi_prime > limit:
                    break
                beautiful_numbers.add(semi_prime)

        return beautiful_numbers

    def sieve(self, limit):
        """Finds all prime numbers up to 'limit' using the Sieve of Eratosthenes."""
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
                    
        primes = [i for i in range(limit + 1) if is_prime[i]]
        return primes, is_prime

# Example Test Cases
sol = Solution()
print(sol.countSubsequence([2, 3]))  # Output: 3
print(sol.countSubsequence([3]))     # Output: 1