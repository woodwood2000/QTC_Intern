# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字
default_params = {"t1": 150, "t2": 50} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1": "成交量的均值", "t2": "相关系数"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    alpah45 = (RANK(DELTA((((CLOSE * 0.6) + (OPEN * 0.4))), 1)) * RANK(CORR(VWAP, MEAN(VOLUME,150), 15)))
    """
    if not params:
        params = defult_params    
    t1 = params['t1']
    t2 = params['t2']

    alpha45 = dv.add_formula('alpha45', 'Rank(Delta(((close*0.6)+(open*0.4)),1)) *  \
        Rank(Correlation(vwap, Ts_Mean(volume, %s), %s))'%(t1,t2), is_quarterly=False, add_data=True)
    return alpha45

