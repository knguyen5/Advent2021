import pandas as pd

def get_common_bit(array, method, tie_break=None):
    ratio = array.sum() / array.count()

    if tie_break is not None and ratio == 0.5:
        return tie_break
    if method == "most":
        return round(ratio)
    else:
        return int(not bool(round(ratio)))


def binary_to_decimal(lst):
    return int("".join(lst), 2)


df = pd.read_clipboard(header=None, dtype=str)
df["parsed"] = df[0].apply(lambda x: [d for d in x])

df_parsed = pd.DataFrame(df["parsed"].to_list())
df_parsed = df_parsed.astype(int)
df_gamma = df_parsed.apply(get_common_bit, args=("most", ), axis=0)
df_eps = df_parsed.apply(get_common_bit, args=("least", ), axis=0)

gamma = binary_to_decimal(df_gamma.astype(str).to_list())
eps = binary_to_decimal(df_eps.astype(str).to_list())

power = gamma * eps

df_o2 = df_parsed.copy()
idx = 0
while len(df_o2) > 1:
    df_o2 = df_o2[df_o2[idx] == get_common_bit(df_o2[idx], method="most", tie_break=1)]
    idx += 1


df_co2 = df_parsed.copy()
idx = 0
while len(df_co2) > 1:
    df_co2 = df_co2[df_co2[idx] == get_common_bit(df_co2[idx], method="least", tie_break=0)]
    idx += 1

o2 = int("".join(df_o2.astype(str).iloc[0].to_list()), 2)
co2 = int("".join(df_co2.astype(str).iloc[0].to_list()), 2)

o2 * co2