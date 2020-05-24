# -*- coding: utf-8 -*-
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt

from scipy.special import factorial
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import statsmodels.api as sm
from statsmodels.api import Poisson
from scipy import stats
from scipy.stats import norm
from statsmodels.iolib.summary2 import summary_col

poisson_pmf = lambda y, myu: myu**y / factorial(y) * exp(-myu)
y_values = range(0, 25)

fig, ax = plt.subplots(figsize=(12, 8))

for myu in [1, 5, 10]:
    distribution = []
    for y_i in y_values:
        distribution.append(poisson_pmf(y_i, myu))
    ax.plot(y_values,
            distribution,
            #label=f"$\mu$={myu}",
            alpha=0.5,
            marker='o',
            markersize=8)

ax.grid()
ax.set_xlabel('$y$', fontsize=14)
ax.set_ylabel('$f(y \mid \mu)$', fontsize=14)
ax.axis(xmin=0, ymin=0)
ax.legend(fontsize=14)

plt.show()