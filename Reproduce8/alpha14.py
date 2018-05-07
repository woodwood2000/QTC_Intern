# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字
default_params = {"t": 5} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t": "DELAY 的参数"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    alpha14 = CLOSE-DELAY(CLOSE,5)
    """
    if not params:
        params = defult_params    
    t = params['t']

    alpha14 = dv.add_formula('alpha14', 'close-Delay(close,%s)'%(t), is_quarterly=False, add_data=True)
    return alpha14
