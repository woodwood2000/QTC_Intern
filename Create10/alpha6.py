# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字

def run_formula(dv):
    '''
    -BackwardADJ*SRMI
    '''
    alpha6 = dv.add_formula('alpha6', '-BackwardADJ*SRMI', is_quarterly=False, add_data=True)
    return alpha6