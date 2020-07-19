import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=sns.load_dataset("tips")
plt.figure(figsize=(16,9))
sns.set(style="darkgrid")
sns.barplot(x="day",y="total_bill",hue_order=["Female","Male"],hue="sex",data=df,order=["Sun","Thur","Fri","Sat"],estimator=np.max )
plt.xlabel("days")
plt.ylabel("total_billl")
plt.title("BarPlot")
plt.show()
