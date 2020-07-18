bins=np.arange(0,51,5)
bins
import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
df=sns.load_dataset("tips")
sns.distplot(df["total_bill"])
plt.xticks(bins)
plt.show()
