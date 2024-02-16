"""
git bisect start
git bisect good X
git bisect bad Y

git bisect run powershell -c "pip uninstall -y pandas; pip uninstall -y unknown; python setup.py develop; py t.py"
git bisect reset
"""

# import pandas as pd
import datetime as dt
import dateutil

start = dt.datetime(2020, 1, 1)
offset_1 = dt.timedelta(days=1.5)
# offset_2 = pd.DateOffset(days=1.5)
offset_3 = dateutil.relativedelta.relativedelta(days=1.5)
# out1 = pd.Timestamp(year=2020, month=1, day=2, hour=12)
