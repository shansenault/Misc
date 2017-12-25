# [2017-12-11] Challenge #344 [Easy] Baum-Sweet Sequence
# https://redd.it/7j33iv
# Your challenge today is to write a program that generates the Baum-Sweet sequence from 0 to some number n.
# For example, given "20" your program would emit:
# 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0


def generate_baum_sweet_sequence(n1, n2):

    sequence = []

    for n in range(n1, n2 + 1):
        blocks = list(('{0:b}'.format(n)).split('1'))
        odd_blocks = False

        for block in blocks:
            if len(block) % 2 is not 0:
                odd_blocks = True

        sequence.append(1 if not odd_blocks else 0)
        # 1 if the binary representation of n contains no block of consecutive 0s of odd length; otherwise 0

    if n1 == 0:  # handle the case where the first n in the sequence is 0
        sequence.remove(0), sequence.insert(0, 1)

    return sequence


if __name__ == '__main__':

    n1 = 0
    n2 = 20
    expected_result = [1, 1, 0, 1, 1, 0, 0, 1,
                       0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
    sequence = generate_baum_sweet_sequence(n1, n2)

    if sequence == expected_result:
        print("Baum-Sweet sequence from {n1} to {n2}:\n{0}".format(
            ', '.join(str(x) for x in sequence), n1=n1, n2=n2))
