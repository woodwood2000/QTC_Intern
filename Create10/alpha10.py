# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字

def run_formula(dv):
    '''
    -ASI*Elder
    '''
    
    alpha10 = dv.add_formula('alpha10', '-ASI*Elder', is_quarterly=False, add_data=True)
    return alpha10