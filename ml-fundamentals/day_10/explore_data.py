from ucimlrepo import fetch_ucirepo

adult = fetch_ucirepo(id=2)   # id=2 is the "Adult" dataset specifically
X = adult.data.features        # DataFrame of all input columns
y = adult.data.targets         # DataFrame with the income label

df = X.copy()
df["income"] = y

# print(df.info())
# print(df.describe())


df = df.dropna() #picked dropna because there are str values also
print(f"NUll Count{df.isnull().sum()}")