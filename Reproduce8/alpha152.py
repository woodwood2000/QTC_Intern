# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字
default_params = {"t1": 9, "t2": 9, "t3": 12, "t4": 9, "t5": 9, "t6": 26, "t7": 9} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1": "看公式中的位置", "t2": "看公式中的位置", "t3": "看公式中的位置", \
"t4": "看公式中的位置", "t5": "看公式中的位置", "t6": "看公式中的位置", "t7": "看公式中的位置"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    '''
    alpha152 = SMA(MEAN(DELAY(SMA(DELAY(CLOSE/DELAY(CLOSE,t1),1),t2,1),1),t3)-MEAN(DELAY(SMA(DELAY(CLOSE/DELAY(CLOSE,t4),1),t5,1),1),t6),t7,1)
    '''
    if not params:
        params = defult_params    
    t1 = params['t1']
    t2 = params['t2']
    t3 = params['t3']
    t4 = params['t4']
    t5 = params['t5']
    t6 = params['t6']
    t7 = params['t7']
  
    alpha152 = dv.add_formula("alpha152","Sma(Ts_Mean(Delay(Sma(Delay(close/Delay(close,%s),1),%s,1),1),%s)-\
        Ts_Mean(Delay(Sma(Delay(close/Delay(close,%s),1),%s,1),1),%s),%s,1)"%(t1,t2,t3,t4,t5,t6,t7), is_quarterly=False, add_data=True)
    return alpha152