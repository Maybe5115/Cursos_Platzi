import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("income_db_gorg.csv")

def pred(x):
    beta = np.array([744.83, -82.45])
    v = 30980.48
    return x@beta + v

X = df[["Lat", "Lon"]].values

Y_hat = pred(X)

Y = df["Mean"].values

fig, ax = plt.subplots(1,1, figsize = (7,7), dpi = 120)
ax.scatter(Y_hat, Y, marker = "o", color = "red")
ax.plot(Y, Y, ls = "--")
plt.show()