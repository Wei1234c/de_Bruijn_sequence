# https://en.wikipedia.org/wiki/De_Bruijn_sequence

class dbs:
    # https://zh.wikipedia.org/wiki/ASCII
    PUNCTUATIONS_1 = ''.join(map(chr, range(32, 48)))
    PUNCTUATIONS_2 = ''.join(map(chr, range(58, 65)))
    PUNCTUATIONS_3 = ''.join(map(chr, range(123, 127)))
    PUNCTUATIONS = PUNCTUATIONS_1 + PUNCTUATIONS_2 + PUNCTUATIONS_3
    DIGITS = ''.join(map(chr, range(48, 58)))
    ALPHABETS_UPPER = ''.join(map(chr, range(65, 91)))
    ALPHABETS_LOWER = ''.join(map(chr, range(97, 123)))
    ALPHABETS = ALPHABETS_UPPER + ALPHABETS_LOWER


    @classmethod
    def _gen_sequence(cls, collection, n):

        k = len(collection)
        a = [0] * k * n
        sequence = []


        def db(t, p):
            if t > n:
                if n % p == 0:
                    sequence.extend(a[1:p + 1])
            else:
                a[t] = a[t - p]
                db(t + 1, p)

                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    db(t + 1, t)


        db(1, 1)

        return [collection[i] for i in sequence]


    @classmethod
    def alphabets(cls, n = 2, alphabets = ALPHABETS):
        return "".join(cls._gen_sequence(alphabets, n))


    @classmethod
    def digits(cls, n = 2, digits = DIGITS):
        return "".join(cls._gen_sequence(digits, n))


    @classmethod
    def binary(cls, n = 2):
        return "".join(cls._gen_sequence('01', n))


    @classmethod
    def numbers(cls, n = 2, numbers = (0, 1)):
        return cls._gen_sequence(numbers, n)
