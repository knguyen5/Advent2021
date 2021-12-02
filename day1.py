import pandas as pd

df = pd.read_clipboard(header=None)
diffs = df.diff()
diffs_inc_count = sum(diffs[0] > 0)

print(diffs_inc_count)

windowed_sum = df[0].rolling(3).sum()
windowed_sum_diff = windowed_sum.diff()
print(sum(windowed_sum_diff > 0))