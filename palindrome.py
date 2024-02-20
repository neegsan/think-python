def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print(first('reviver'))
print(last('reviver'))
print(middle('reviver'))
print(first(middle('reviver')))
print(middle(middle('reviver')))