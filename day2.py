import pandas as pd

df = pd.read_clipboard(header=None)

df_agg = df.groupby(0)[1].sum()
forward = df_agg.loc["forward"]
depth = df_agg.loc["down"] - df_agg.loc["up"]

forward * depth

aim = 0
forward = 0
depth = 0
for _, row in df.iterrows():
    if row[0] == "down":
        aim += row[1]
    if row[0] == "up":
        aim -= row[1]
    if row[0] == "forward":
        forward += row[1]
        depth += row[1] * aim
        
forward * depth