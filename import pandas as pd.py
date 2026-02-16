import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\playlist_analysis.csv")
print(df.head())

x = df.groupby("Artist")
plt.bar(x)
plt.show()