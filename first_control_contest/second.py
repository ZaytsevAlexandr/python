def max_pal(s):
    words = s.split()
    max_length = 0
    for word in words:
        w = word.lower()

        if w == w[::-1]:
            max_length = max(max_length, len(word))

    return max_length

a = input()
print(max_pal(a))
