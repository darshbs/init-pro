def totalCount(n: int) -> int:
    """
    Finds the sum of all valid x values where:
    sum(n) = xorSum(n, x)
    """
    total_sum = (n * (n + 1)) // 2  # Compute sum of first 'n' numbers

    valid_x_sum = 0

    for x in range(n + 1):  # Check all x values
        xor_sum = sum(i ^ x for i in range(n + 1))  # Compute XOR sum
        
        if xor_sum == total_sum:  # If condition is met, add x
            valid_x_sum += x
    
    return valid_x_sum


# Example Test Cases
test_cases = [3, 6, 7, 11, 15]
for n in test_cases:
    print(f"n = {n}, Sum of valid x values: {totalCount(n)}")
