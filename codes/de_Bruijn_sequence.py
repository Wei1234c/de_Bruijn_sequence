class dbs:
    # https://zh.wikipedia.org/wiki/ASCII
    PUNTUATIONS_1 = ''.join(map(chr, range(32, 48)))
    PUNTUATIONS_2 = ''.join(map(chr, range(58, 65)))
    PUNTUATIONS_3 = ''.join(map(chr, range(123, 127)))
    PUNTUATIONS = PUNTUATIONS_1 + PUNTUATIONS_2 + PUNTUATIONS_3
    DIGITS = ''.join(map(chr, range(48, 58)))
    ALPHABETS_UPPER = ''.join(map(chr, range(65, 91)))
    ALPHABETS_LOWER = ''.join(map(chr, range(97, 123)))
    ALPHABETS = ALPHABETS_UPPER + ALPHABETS_LOWER


    @classmethod
    def _gen_sequence(cls, k, n):
        """
        de Bruijn sequence for alphabet k
        and subsequences of length n.
        """

        try:
            # let's see if k can be cast to an integer;
            # if so, make our alphabet a list
            _ = int(k)
            alphabet = list(map(str, range(k)))

        except (ValueError, TypeError):
            alphabet = k
            k = len(k)

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

        return "".join(alphabet[i] for i in sequence)


    @classmethod
    def alphabets(cls, n = 2, alphabets = ALPHABETS):
        return cls._gen_sequence(alphabets, n)


    @classmethod
    def digits(cls, n = 2, digits = DIGITS):
        return cls._gen_sequence(digits, n)


    @classmethod
    def binary(cls, n = 2):
        return cls._gen_sequence('01', n)
