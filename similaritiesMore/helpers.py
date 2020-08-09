from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""

    cost = [[]]
    c = 0
    while a != b:

        if c < len(a) and c < len(b):
            if a[c] == b[c]:
                print(a.upper())
                c += 1
                
            elif a[c] != b[c]:
                print(a, a[c].upper(), '/ substituted', a[c], 'with', b[c], c)
                a = a[:c] + b[c] + a[c + 1:]
                c += 1
                cost.append((3, Operation.SUBSTITUTED))

        elif len(a) < len(b):
            a = a[:c] + b[c] + a[c:]
            print(a, a[c].upper(), '/ inserted', b[c], c)
            c += 1
            cost.append((2, Operation.INSERTED))

        else:
            print(a, a[c].upper(), '/ deleted', a[c], c)
            a = a[:c] + a[c + 1:]
            cost.append((1, Operation.DELETED))

    print(cost)
    return cost
