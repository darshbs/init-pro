class Solution:
    def findNthKPalindrome(self, k, n):
        length = 1
        count = k  # Start with k single-letter palindromes

        # Step 1: Determine the length of the n-th palindrome
        while n > count:
            n -= count  # Reduce n by the number of palindromes of the current length
            length += 1
            half_length = (length + 1) // 2  # Half-length for mirroring
            count = k ** half_length  # Number of palindromes for this new length

        # Step 2: Convert n into a k-based number for the first half
        n -= 1  # Convert n to 0-based index
        first_half = []
        
        for i in range((length + 1) // 2):
            first_half.append(chr(ord('a') + (n % k)))  # Convert digit to letter
            n //= k

        # Step 3: Construct full palindrome by mirroring
        if length % 2 == 0:
            full_palindrome = ''.join(first_half + first_half[::-1])
        else:
            full_palindrome = ''.join(first_half + first_half[-2::-1])

        return full_palindrome


# Example test cases
solution = Solution()
print(solution.findNthKPalindrome(3, 5))  # Output: "bb"
print(solution.findNthKPalindrome(2, 7))  # Output: "bab"
