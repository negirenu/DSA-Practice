# n=4
# output=4+3+2+1+0=10

def rec_sum(n):
    # base case
    if n == 0:
        return n

    return n + rec_sum(n - 1)


print("the cumulative sum is:", rec_sum(4))
