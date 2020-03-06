def isAnagram(s, t):
    return len(s) == len(t) and sorted(s) == sorted(t)
    # anagram = dict.fromkeys(''.join([chr(i) for i in range(97, 123)]), 0)
    # for letter in s:
    #     anagram[letter] += 1
    # for letter in t:
    #     anagram[letter] -= 1
    # return not any(anagram.values())


a = 'aaaab'
b = 'aaaab'
print(isAnagram(a, b))
