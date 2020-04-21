#!/usr/bin/env sage
# coding=utf-8

from pubkey import P, n, e
from secret import flag
from os import urandom

R.<a> = GF(2^2049)

def private_key(e, l):
    counter = 1
    while True:
        if e * P(R.fetch_int(counter)) % l == 1:
            return P(R.fetch_int(counter))
            

def lcm(p, q):
    return p * q / gcd(p, q)

def encrypt(m):
    global n
    assert len(m) <= 256
    m_int = Integer(m.encode('hex'), 16)
    m_poly = P(R.fetch_int(m_int))
    c_poly = pow(m_poly, e, n)
    c_int = R(c_poly).integer_representation()
    c = format(c_int, '0256x').decode('hex')

    p_poly, q_poly = factor(n)

    p_poly = P(p_poly)
    q_poly = P(q_poly)
    e_poly = P(R.fetch_int(e))
    l_poly = P((p_poly - 1) * (q_poly - 1))
    d_poly = private_key(e_poly, l_poly)

    print(d_poly)

    d_int = R(d_poly).integer_representation()

    print(d_int)

    return c

if __name__ == '__main__':
    ptext = flag + os.urandom(256-len(flag))
    ctext = encrypt(ptext)
    with open('flag2.enc', 'wb') as f:
        f.write(ctext)
