#!/usr/bin/env python3

from functools import reduce
import operator
from math import inf

def prod(xs):
    """
    Return the product of iterable `xs`
    """
    return reduce(operator.mul, xs, 1)

def p_of_no_card(copies=4, deck_size=60, draw=7):
    """
    Compute the probability that a given card `copies` times  isn't seen in a
    draw of size `draw` from a deck of size `deck_size`.

    >>> p_of_no_card(copies=4, deck_size=60, draw=7)
    0.6005003742553344
    >>> p_of_no_card(copies=1, deck_size=60, draw=7)
    0.8833333333333332
    >>> p_of_no_card(copies=0, deck_size=60, draw=7)
    1.0
    """
    base_num_misses = deck_size - copies
    return prod([ms / cds for (ms, cds) in
        zip(range(base_num_misses, base_num_misses - draw, -1),
            range(deck_size, deck_size - draw, -1))])

def p_of_card(copies=4, deck_size=60, draw=7):
    """
    Compute the probability that a given card `copies` times  is seen in a draw
    of size `draw` from a deck of size `deck_size`.
    """
    return 1 - p_of_no_card(copies, deck_size, draw)

def expected_first_draw(copies=4, deck_size=60):
    """
    Compute the expected number of draws until a card is seen.
    """

    if copies < 1:
        return inf

    def Y(n):
        """
        Compute the probability that Y_n = 1, where Y_n is the random variable
        indicating if the first n variables are not the sought card.
        """
        return p_of_no_card(copies=copies, deck_size=deck_size, draw=n)

    def X(n):
        """
        Compute the probability of X_n = 1, where X_n is the random variable
        indicating that the first time the sought card is seen is on draw n
        """
        m = n - 1
        return Y(m) * copies / (deck_size - m)

    xs = [X(n) * n for n in range(1, deck_size + 1)]

    if copies is 1:
        return sum(xs)
    else:
        return sum(xs[:1 - copies])

def expected_card_num(copies=4, deck_size=60, draw=7):
    return draw * copies / deck_size

