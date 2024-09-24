import pandas as pd
import matplotlib.pyplot as plt

car = ["Tata","Maruti","suzuki","BMW"]
weight = [2.1,2.5,2.9,3.6]
data = {"Car" : car, "Weight" : weight}
df = pd.DataFrame(data)
print(df)
df.plot(x="Car",y="Weight",kind="line", marker="o")
plt.xlabel("CAR")
plt.ylabel("WEight")
plt.title("Car and weight")
plt.show()
