import numpy as np

import pandas as pd

df = pd.DataFrame({
    "name":["Alice","Bob","Charlie","Rakesh","Ram"],
    "score":[10,20,np.nan,40,np.nan]
})

print(df.isnull().sum())

df_clean = df.dropna(ignore_index=True)
df_clean_values = df.fillna(df["score"].median())
print(df_clean_values)