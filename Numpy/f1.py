import numpy as np


def function():
    x = np.arange(1,11)
    def abc(x):
        return x*2+3-2

    return abc(x)#Write your Code here


print(function())