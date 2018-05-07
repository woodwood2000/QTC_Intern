# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "罗晓牧" # 这里填下你的名字

def run_formula(dv):
    '''
    -HBETA*DDNSR
    '''
    alpha5 = dv.add_formula('alpha5', '-HBETA*DDNSR', is_quarterly=False, add_data=True)
    return alpha5