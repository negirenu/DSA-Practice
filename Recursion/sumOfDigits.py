#n=4321
#output=4+3+2+1=10
def sum_digit(n):
    if n == 0:
        return n

    return (n%10) + sum_digit(n//10)

print("sum of all the digits is:", sum_digit(12346))