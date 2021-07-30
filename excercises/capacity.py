"""
Returns greatest signed integer based on the
given memories in bytes
"""


def greatest_integer(memories):
    return '\n'.join(str(memory) + " byte(s): " +
                     format(2 ** (memory * 8) - 1, ".3E")
                     for memory in memories)


print(greatest_integer([1, 2, 8]))