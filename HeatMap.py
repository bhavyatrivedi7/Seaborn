import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("d:\\sale_record.csv",nrows=1000)
df=df.drop(columns=["Region","Order ID","Item Type","Sales Channel","Order Priority","Order Date","Ship Date"])
df=df.set_index("Country")
df=df.head()
df1=df.corr()
sns.heatmap(df1,annot=True,linewidth=3,linecolor="k")
plt.title("global warming")
