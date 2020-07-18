import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
df=sns.load_dataset("tips")
sns.lineplot(x="total_bill",y="tip",data=df,hue="day",style="day",markers=["o","<",">","^"])
plt.title("Tips LineGraph")
plt.xlabel("number of days")
plt.ylabel("number of Tips")
plt.show()
