# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字
default_params = {"t1": 5, "t2": 3, "t3": 3} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1": "", "t2": "", "t3": ""} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    '''
    alpha156 = (MAX(RANK(DECAYLINEAR(DELTA(VWAP, t1), t2)), RANK(DECAYLINEAR(((DELTA(((OPEN * 0.15) + (LOW *0.85)),2) / ((OPEN * 0.15) + (LOW * 0.85))) * -1), t3))) * -1)
    '''
    if not params:
        params = defult_params    
    t1 = params['t1']
    t2 = params['t2']
    t3 = params['t3']

    alpha156 = dv.add_formula("alpha156","(Max(Rank(Decay_linear(Delta(vwap, %s), %s)), \
        Rank(Decay_linear(((Delta(((open * 0.15) + (low *0.85)),2) / ((open * 0.15) + (low * 0.85))) * -1), %s))) * -1)"%(t1,t2,t3), is_quarterly=False, add_data=True)
    return alpha156