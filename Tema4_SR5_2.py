#Tema4_SR5_2

import math

def heron_s(a, b, c):
    pp = (a + b + c) / 2
    s = math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))

    return s