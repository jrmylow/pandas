"""
git bisect start
git bisect good X
git bisect bad Y

git bisect run powershell -c "pip uninstall -y pandas; pip uninstall -y unknown; python setup.py develop; py t.py"
git bisect reset
"""
if True:
    import pandas as pd
    from pandas._libs.tslibs import to_offset
    from pandas.core.arrays.datetimes import _generate_range

    start = pd.to_datetime("2021-12-31 00:00:01")
    end = pd.to_datetime("2023-11-01 00:00:00")
    offset = to_offset("Y")

    result = _generate_range(
        start=start,
        end=end,
        periods=None,
        offset=offset,
        unit="s",
    )
    print(list(result))

if False:
    import pandas as pd

    start = pd.to_datetime("2023-10-31 00:00:00")
    end = pd.to_datetime("2021-11-01 00:00:00")

    rng = pd.date_range(start=start, end=end, freq="-1Y")
    print(rng)
