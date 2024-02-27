#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:39:57 2022

@author: andreluizrodriguesdasilva
"""

x = 4.5
print(x.real, "+", x.imag, "i")

type(x.is_integer)
''' Bitwise Operations '''
            # ~a     Bitwise NOT Bitwise negation of a
bin(4)      # a & b  Bitwise AND Bits defined in both a and b
            # a | b  Bitwise OR Bits defined in a or b or both
4 | 10      # a ^ b  Bitwise XOR Bits defined in a or b but not both
            # a << b Bit shift left Shift bits of a left by b units
4 or 10     # a >> b Bit shift right Shift bits of a right by b units

bin(10)
bin(4)


# Boolean Operations: True , False
# and, or , not
'''
One sometimes confusing thing about the language is when to use
Boolean operators (and, or, not), and when to use bitwise opera‐
tions (&, |, ~). The answer lies in their names: Boolean operators
should be used when you want to compute Boolean values (i.e.,
truth or falsehood) of entire statements. Bitwise operations should
be used when you want to operate on individual bits or components
of the objects in question.
'''

# Identity and Membership Operators
'''
a is b          True if a and b are identical objects
a is not b      True if a and b are not identical objects
a in be         True if a is a member of b
a not in b      True if a is not a member of b
'''

# Identity operators: is and is not
# The identity operators, is and is not, check for object identity.

a = [1, 2, 3]
b = [1, 2, 3]

a == b      # True
a is b      # False
a is not b  # True

'''Membership operators'''
# Membership operators check for membership within compound objects

1 in [1, 2, 3]      # True
2 not in [1, 2, 3]  # False

x = 0.000005
y = 5e-6
print(x == y)

""" Floating-point precision """
0.1 + 0.2 == 0.3
'''Why is this the case? It turns out that it is not a behavior unique to
Python, but is due to the fixed-precision format of the binary
floating-point storage used by most, if not all, scientific computing
platforms. All programming languages using floating-point num‐
bers store them in a fixed number of bits, and this leads some num‐
bers to be represented only approximately.
'''

print("0.1 = {0:.17f}".format(0.1))
print("0.2 = {0:.17f}".format(0.2))
print("0.3 = {0:.17f}".format(0.3))


# Complex Number
'''
Complex numbers are numbers with real and imaginary (floating-
point) parts. We’ve seen integers and real numbers before; we can
use these to construct a complex number
'''
complex(1, 2)
'''
Complex numbers are numbers with real and imaginary (floating-
point) parts. We’ve seen integers and real numbers before; we can
use these to construct a complex number
'''
1 + 2j

c = 3 + 4j
c.real
c.imag
c.conjugate()
abs(c)  # magnitude--that is, sqrt(c.real ** 2 + c.imag ** 2)

# String Type
message = "what do you like?"
response = 'spam'
response.upper()
message.capitalize()
len(response)
message + response  # concatena string
5 * response        # concatenação múltipla


# None Type
'''
Python includes a special type, the NoneType, which has only a sin‐
gle possible value: None. For example:
'''
type(None)
'''
You’ll see None used in many places, but perhaps most commonly it
is used as the default return value of a function. For example, the
print() function in Python 3 does not return anything, but we can
still catch its value:
'''
return_value = print('abc')
print(return_value)

'''Likewise, any function in Python with no return value is, in reality,
returning None.'''


# Boolean Type
bool(0)
bool(3.1415)
bool('')
bool('abc')
bool([])
