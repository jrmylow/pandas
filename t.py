import pandas as pd

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    s = scores.drop_duplicates('score').sort_values(by='score',ascending=False, inplace=False)
    s['ind'] = s.reset_index().index + 1
    r = scores.sort_values(by='score', ascending=False, inplace=False)\
            .set_index('score')\
            .join(other=s.set_index('score'), on='score', lsuffix='_l', rsuffix='_r')
    return pd.DataFrame({'score':r.index, 'rank':r['ind']})
    
if __name__ == '__main__':
    print(order_scores(scores))