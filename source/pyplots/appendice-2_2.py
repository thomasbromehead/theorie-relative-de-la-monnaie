# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def cm2inch(value):
    return value/2.54

data = {
    0: 0,
    1: 0.96,
    2: 1.83,
    3: 2.62,
    4: 3.35,
    5: 4.01,
    6: 4.61,
    7: 5.16,
    8: 5.66,
    9: 6.12,
    10: 6.53,
    11: 6.91,
    12: 7.26,
    13: 7.57,
    14: 7.86,
    15: 8.13,
    16: 8.37,
    17: 8.58,
    18: 8.78,
    19: 8.96,
    20: 9.13,
    21: 9.28,
    22: 9.42,
    23: 9.54,
    24: 9.66,
    25: 9.76,
    26: 9.86,
    27: 9.95,
    28: 10.03,
    29: 10.10,
    30: 10.16,
    31: 10.22,
    32: 10.28,
    33: 10.33,
    34: 10.37,
    35: 10.42,
    36: 10.45,
    37: 10.49,
    38: 10.52,
    39: 10.55,
    40: 10.57,
    41: 10.60,
    42: 10.62,
    43: 10.64,
    44: 10.66,
    45: 10.67,
    46: 10.69,
    47: 10.70,
    48: 10.72,
    49: 10.73,
    50: 10.74,
    51: 10.75,
    52: 10.76,
    53: 10.76,
    54: 10.77,
    55: 10.78,
    56: 10.78,
    57: 10.79,
    58: 10.79,
    59: 10.80,
    60: 10.80,
    61: 10.81,
    62: 10.81,
    63: 10.81,
    64: 10.82,
    65: 10.82,
    66: 10.82,
    67: 10.82,
    68: 10.83,
    69: 10.83,
    70: 10.83,
    71: 10.83,
    72: 10.83,
    73: 10.83,
    74: 10.83,
    75: 10.84,
    76: 10.84,
    77: 10.84,
    78: 10.84,
    79: 10.84,
    80: 10.84
}

# image size in cm, and dpi
fig = plt.figure(figsize=(cm2inch(15), cm2inch(7)), dpi=200)
# position of axes in fraction of image (l,b,w,h)
ax = fig.add_axes([0.1, 0.2, .85, .75])
line, = ax.plot(data.keys(), data.values(), color='red')
ax.fill_between(data.keys(), 0, data.values(), facecolor='red')
ax.set_xlim(0, 80)
ax.grid(False)
plt.xlabel(u"Année")
plt.ylabel(u"$R(t-t_{0})=\\frac{1}{c}(1-e^{-c(t-t_{0})})$")
plt.legend([line], [u"$R(t-t_{0})=\\frac{1}{c}(1-e^{-c(t-t_{0})})$"], loc=4)
plt.show()
