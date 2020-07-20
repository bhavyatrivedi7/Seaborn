import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
sns.pairplot(df,hue="sex",palette="hot",height=2)
plt.show()
