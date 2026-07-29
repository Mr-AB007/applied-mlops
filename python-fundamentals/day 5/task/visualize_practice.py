import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("../../day 4/updated_score.csv")
# print(df.head())
sns.histplot(df["score"])
# plt.show()
plt.savefig("score_distribution.png")

sns.boxplot(df["score"])
# plt.show()