from de_Bruijn_sequence import dbs, combination_with_replacement


print(dbs.alphabets(alphabets = 'ABC'))

print(dbs.alphabets(n = 2, alphabets = dbs.ALPHABETS))

print(dbs.digits(n = 2, digits = dbs.DIGITS))

print(dbs.binary(n = 2))
print(combination_with_replacement.binary(n = 2))

print(dbs.numbers(n = 2, numbers = (0, 1)))

print(dbs.numbers(n = 2, numbers = range(9, 12)))

keys = dbs.numbers(n = 3, numbers = range(256))
# print(keys)
print(len(keys))
