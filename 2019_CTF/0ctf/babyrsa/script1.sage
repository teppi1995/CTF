#!/usr/bin/env sage
# coding=utf-8

from pubkey import P, n, e
from secret import flag
from os import urandom

R.<a> = GF(2^2049)

p_poly, q_poly = factor(n)

p_poly = P(p_poly)
q_poly = P(q_poly)
p_int = R(p_poly).integer_representation()
q_int = R(q_poly).integer_representation()
n_int = R(n).integer_representation()

print(p_int)
print(q_int)

print(factor(n))