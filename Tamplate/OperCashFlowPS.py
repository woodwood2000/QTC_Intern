# OperCashFlowPS.py
# 每股指标

def run_formula(dv):
    # OperCashFlowPS = NOCF/TS
    # NOCF -- 经营活动产生的现金呢流量净额(TTM)
    # TS   -- 总股本
    
    # 经营活动产生的现金流量净额
    if 'net_cash_flows_oper_act' not in dv.fields:
        dv.add_field('net_cash_flows_oper_act')
    # 总股本
    if 'capital_stk' not in dv.fields:
        dv.add_field('capital_stk')
        
    OperCashFlowPS = dv.add_formula("OperCashFlowPS", "net_cash_flows_oper_act/capital_stk", is_quarterly=False, add_data=True)
    return OperCashFlowPS