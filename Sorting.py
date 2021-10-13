from os import terminal_size
import pandas as pd

df = pd.read_csv("dwarf_stars.csv")

print(df.dtypes)
df = df.dropna()

df["Mass"] = df["Mass"].apply(lambda x: x.replace('$', '').replace(',', '')).astype("float")

df["Radius"] = 0.102763*df["Radius"]
df["Mass"] = 0.000954588*df["Mass"]


df.drop(["Unnamed: 0"], axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.head())

df.to_csv("Clean_dwarf_stars.csv")