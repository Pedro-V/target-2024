def my_reversed(s):
    n = len(s)
    chars = []
    for i in range(n - 1, -1, -1):
        chars.append(s[i])
    return ''.join(chars)

word = "C'thullu"
print(my_reversed(word))
