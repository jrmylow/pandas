Summary of thoughts re: proposed .pipe(func) function:

```python
pd.Series().pipe(func)

def pipe(self, func):
    return func(self)
```

Do we assume that the user will pass in valid functions e.g. not trying to call .pow() on a series that doesn't support it?