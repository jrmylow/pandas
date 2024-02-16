"""
git bisect start
git bisect good X
git bisect bad Y

git bisect run powershell -c "pip uninstall -y pandas; pip uninstall -y unknown; python setup.py develop; py t.py"
git bisect reset
"""

import pandas as pd

data = [123, 234, 343, 134, 546, 383, 785, 820, 909, 111]
data_pd = pd.Series(data)
a = data_pd.rolling(window=3)
print(a)
print(a.std())


def rolling_std_dev(data, window_size):
    if window_size > len(data):
        raise ValueError("Window size larger than data length")

    def std_dev(slice_data):
        mean = sum(slice_data) / len(slice_data)
        variance = sum((x - mean) ** 2 for x in slice_data) / (len(slice_data) - 1)
        return variance**0.5

    rolling_std = [
        std_dev(data[i : i + window_size]) for i in range(len(data) - window_size + 1)
    ]
    return rolling_std


print(rolling_std_dev(data, 3))
