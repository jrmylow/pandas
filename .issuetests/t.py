"""
git bisect start
git bisect good X
git bisect bad Y

git bisect run powershell -c "pip uninstall -y pandas; pip uninstall -y unknown; python setup.py develop; py t.py"
git bisect reset
"""
import pandas as pd

df = pd.DataFrame(
    [1577840521123543000, 1577934062321654000, 1578027849987321000],
    dtype="Int64",
    columns=["col1"],
)

df.to_numpy(dtype="int64", na_value=float("nan"))
