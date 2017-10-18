#!/python3

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import datetime

import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15,6

df = pd.read_csv('/u/chsherpa/Desktop/DataSci/stocks-us-adjClose.csv')
df.head()
