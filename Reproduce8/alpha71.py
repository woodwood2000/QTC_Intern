# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字
default_params = {"t1": 24, "t2": 24} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1": "收盘价的均值", "t2": "收盘价的均值"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    '''
    alpha71 = (CLOSE-MEAN(CLOSE,24))/MEAN(CLOSE,24)*100
    '''
    if not params:
        params = defult_params    
    t1 = params['t1']
    t2 = params['t2']

    alpha71 = dv.add_formula('alpha71', '(close-Ts_Mean(close, %s))/Ts_Mean(close, %s)*100'%(t1,t2), is_quarterly=False, add_data=True)
    return alpha71