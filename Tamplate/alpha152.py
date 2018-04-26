#------------------------------------------------------------------------------
#alpha152 = SMA(MEAN(DELAY(SMA(DELAY(CLOSE/DELAY(CLOSE,9),1),9,1),1),12)-MEAN(DELAY(SMA(DELAY(CLOSE/DELAY(CLOSE,9),1),9,1),1),26),9,1)
# 定义指数平均计算函数-传入一个时间为索引,股票为columns的Dataframe,计算其指数平均序列
# SMAtoday=m/n * Pricetoday + ( n-m )/n * SMAyesterday;

def sma(df, n, m):
    a = n / m - 1
    r = df.ewm(com=a, axis=0, adjust=False)
    return r.mean()

def run_formula(dv):    
    alpha152 = dv.add_formula("alpha152","SMA(Ts_Mean(Delay(SMA(Delay(close/Delay(close,9),1),9,1),1),12)-Ts_Mean(Delay(SMA(Delay(close/Delay(close,9),1),9,1),1),26),9,1)", is_quarterly=False, add_data=True, register_funcs={"SMA":sma})
    return alpha152