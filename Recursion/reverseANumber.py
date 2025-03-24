def reverse_number(n, rev=0):
    #Base case
    if n == 0:
        return rev
    rev = (rev * 10) + (n % 10)  # Append last digit to rev
    return reverse_number(n // 10, rev)  # Remove last digit & recurse

# Example
num = 12345
reversed_num = reverse_number(num)
print(f"Reversed Number: {reversed_num}")  # Output: 54321