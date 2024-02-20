def is_palindrome(word):
    for i in range(len(word)):
        if word[i] == word[len(word)-(i+1)]:
            x = True and word[i] == word[len(word)-(i+1)]

        else:
            x = True and word[i] == word[len(word)-(i+1)]
    return x

print(is_palindrome('reviver'))
print(is_palindrome('ovo'))
print(is_palindrome('marrocos'))
print(is_palindrome('bolalob'))
print(is_palindrome('sistema'))
print(is_palindrome('vermelhohlemrev'))
