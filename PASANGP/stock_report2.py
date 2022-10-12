import pandas as pd
import requests

def get_stock(code):
    df = pd.DataFrame()
    for page in range(1,21):
        # 일별 시세 url 
        url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code) 
        url = '{url}&page={page}'.format(url=url, page=page)
        print(url)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'} ## 참고) 7.3.1 User-Agent 확인하기 
        res = requests.get(url,headers=header)
        current_df = pd.read_html(res.text, header=0)[0]
        df = df.append(current_df, ignore_index=True)
    
    return df

code = '005930'
df = get_stock(code)
print(df.head())
