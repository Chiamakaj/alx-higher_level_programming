#!/usr/bin/python3
for alphabet in range(97, 123):
    alph_conv = chr(alphabet)
    if alph_conv not in 'qe':
        print(alph_conv, end='')
