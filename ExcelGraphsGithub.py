import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use("ggplot")

df2 = pd.read_csv("E:\\Padhai\\Programming\\QShore\\Pandas\\GitHubProject\\DailyData.csv")
x1 = df2.Date[-25:]
y1 = df2.Sales[-25:]
y2 = df2.Employee[-25:]
y3 = df2.FootFall[-25:]
y4 = df2.Profit[-25:]
y5 = df2.Acquizitions[-25:]

plt.subplot(321)
plt.plot(x1,y1,label='Sales',color="Orange")
plt.title("Sales Graph for Last 25 days")
plt.legend()

plt.subplot(323)
plt.bar(x1,y2,label='Employees',color="blue")
plt.legend()

plt.subplot(325)
plt.scatter(x1,y3,label='Footfall',color="black")
plt.xlabel("Footfall")
plt.legend()

plt.subplot(222)
plt.plot(x1,y4,label='Profit',color="Green")
plt.xlabel("Profit")
plt.legend()

plt.subplot(224)
plt.bar(x1,y5,label='Acquizitions',color="purple")
plt.xlabel("Acquizitions")
plt.legend()

plt.show()



