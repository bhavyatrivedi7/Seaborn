import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(16,9))
df=sns.load_dataset("titanic")
sns.scatterplot(x="who",y="fare",data=df,hue="alive",style="alive",size="who",sizes=(100,40))
plt.show()
