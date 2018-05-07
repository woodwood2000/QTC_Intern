# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字

from sklearn.linear_model import LinearRegression
from jaqs_fxdayu.data.dataservice import RemoteDataService
import pandas as pd

default_params = {"t1": 20, "t2": 5, "t3": 0} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1": "横截面回归的窗口宽度", "t2": "回归的阶数", "t3": "无风险利率"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    '''
    超额流动（Liquidity-turnover beta）。属于收益和风险类因子。数据更新时间：T日17点00分。
    TOBT: 市场组合日收益绝对值的五阶和自身五阶的回归
    '''
    if not params:
        params = defult_params    
    win = params['t1']
    lag_num = params['t2']
    rf_t = params['t3']

    linreg = LinearRegression()

    # r_{M,t} 市场组合每日收益(沪深300)
    # data_config = {
    #     "timeout": 180,
    #     "remote.data.address": "tcp://data.tushare.org:8910",
    #     "remote.data.username": "13570389403",
    #     "remote.data.password":
    # "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MjI0MjI5ODcwNDYiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTM1NzAzODk0MDMifQ.1uY80OkA6JgmJIi0DbZmVmf-aKeDqYn4ImRZov4J0Bo"
    #     }
    # ds = RemoteDataService()
    # ds.init_from_config(data_config)
    #hs300 = ds.daily('000300.SH', dv.start_date, dv.end_date)[0]
    hs300 = dv.data_api.daily('000300.SH', dv.start_date, dv.end_date)[0]
    hs300.set_index(['trade_date'], inplace=True)
    hs300_pct = hs300['close'].pct_change()

    # r_{i,t} 股票的每日收益
    stocks_pct = dv.get_ts('close_adj').pct_change()

    if 'turnover_ratio' not in dv.fields:
        dv.add_field('turnover_ratio')
    TORate = dv.get_ts('turnover_ratio')

    TOBT_df = pd.DataFrame(columns = stocks_pct.columns, index = stocks_pct.index)

    print("Total %s stocks:" % len(stocks_pct.columns))

    n = 0
    for stock in stocks_pct.columns:
        n = n+1
        if n%50 == 0:
            print(n)

        e_i = abs(stocks_pct[stock]-rf_t) # Stock_return
        e_i.name = 'e'
        data_TOBT = pd.DataFrame(e_i)

        data_TOBT['M'] = abs(hs300_pct-rf_t) # Market_return
        data_TOBT['ToRate'] = TORate[stock] # Turnover_ratio
        
        for lag in range(1, lag_num+1):
            col_e = 'e_'+str(lag)
            data_TOBT[col_e] = data_TOBT['e'].shift(lag)   
            col_M = 'M_'+str(lag)
            data_TOBT[col_M] = data_TOBT['M'].shift(lag)
            
        data_TOBT = data_TOBT.dropna()
        
        if len(data_TOBT) < 180:
            continue
            
        feature = ['ToRate', 'e_1', 'e_2', 'e_3', 'e_4', 'e_5', 'M_1', 'M_2', 'M_3', 'M_4', 'M_5']
        X = data_TOBT[feature]
        y = data_TOBT[['e']]

        beta = pd.Series(index = data_TOBT.index)

        for d in range(win, len(data_TOBT)+1):
            d_beg = d-win
            d_end = d-1
            #print(d, d_beg, d_end)
            X_train = data_TOBT.iloc[d_beg:d_end][feature]
            y_train = data_TOBT.iloc[d_beg:d_end]['e']
            linreg.fit(X_train, y_train)
            beta.iloc[d_end] = linreg.coef_[0]

        data_TOBT['beta'] = beta
        TOBT_df[stock] = beta

    dv.append_df(TOBT_df, 'TOBT')

    return dv.get_ts('TOBT')