def totalCount(n: int) -> int:
    total_sum = (n * (n + 1)) // 2  # Compute sum of first 'n' numbers

    # Find valid x values based on bitwise properties
    valid_x_sum = 0
    for x in range(n + 1):
        if (n & x) == 0:  # Valid x follows specific bitwise conditions
            valid_x_sum += x

    return valid_x_sum


# Example Test Cases
test_cases = [3, 6, 7, 11, 15]
for n in test_cases:
    print(f"n = {n}, Sum of valid x values: {totalCount(n)}")