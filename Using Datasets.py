import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pylab as plt

# Load the data into a DataFrame
df = pd.read_csv('RBClassics.csv')

#Getting the data from the CSV file
x = df["Popularity"]
y = df["Year"]

#Creating a bar chart
plt.bar(x,y)
plt.title("Testing")
plt.xlabel("Popularity")
plt.ylabel("Year")
plt.style.use("fivethirtyeight")
plt.show()















