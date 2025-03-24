"""Anagram is a word or phrase formed by rearranging the letters of another word or phrase.
All the original letters must be used exactly once."""
def anagram(s1, s2):
    #base case - if the lenth of both the strings is not same that means they are not anagram.
    if len(s1) != len(s2):
        return False

    count = {}

    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in s2:
        if ch in count:
            count[ch] -= 1
        else:
            count[ch] = 1

    for k in count:
        if count[k]!=0:
            return False

    return True

print(anagram('dog', 'god'))   #anagram(True)
print(anagram('dog', 'goood'))  #not anagram(False)