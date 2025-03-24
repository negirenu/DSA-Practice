def reverse(s):
    #Base case
    if len(s) == 1:
        return s

    return reverse(s[1:]) + s[0]

print(reverse('dog'))
print(reverse('abcdef'))
