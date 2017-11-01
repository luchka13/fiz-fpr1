#!/usr/bin/python3

import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt

upor = pnd.read_csv('data/upor_lezaja/0.csv', usecols=[0, 3], dtype=float)

print(upor)