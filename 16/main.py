#!/usr/bin/python3

import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
import seaborn as sns

upor = pnd.read_csv('data/upor_lezaja/converted_0.csv', usecols=[0, 2], dtype=float)

# plt.errorbar(upor['time'], upor['omega'], xerr=0.001, yerr=0, fmt='o') # TODO: assess errors
#
# plt.plot(np.poly1d(np.polyfit(upor['time'], upor['omega'], 1)))
#
# # print(upor['time'])
#
# plt.show()

plt.errorbar(upor['time'], upor['omega'], yerr=0.05, fmt='o', markersize=1, capsize=5)
plt.show()

