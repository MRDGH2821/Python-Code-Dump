import pandas as pd
from matplotlib import pyplot as plt

dataset = pd.read_csv("titanic_train.csv")

# %% Histogram
plt.hist(dataset['Age'].values)
plt.xlabel('Age')
plt.ylabel('No. of people')
plt.show()

# %% Pie Chart
print(dataset['Sex'].value_counts())
plt.pie(dataset['Sex'].value_counts(), labels=dataset['Sex'].unique())
plt.legend()
plt.show()

# %% Bar Graph
plt.bar(dataset['Parch'].unique(), dataset['Parch'].value_counts(), width=0.4)
plt.xlabel('Parch')
plt.ylabel('No. of people')
plt.show()

# %% Histogram
plt.hist(dataset['Fare'].values)
plt.xlabel('Fare')
plt.ylabel('No. of people')
plt.show()

# %% Pie chart
plt.pie(dataset['Pclass'].value_counts(), labels=dataset['Pclass'].unique())
plt.xlabel("Passenger Class")
plt.legend()
plt.show()
