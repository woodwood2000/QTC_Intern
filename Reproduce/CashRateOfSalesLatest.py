# 经营活动产生的现金流量净额与营业收入之比（Cash rate of sales）。
# 计算方法：经营活动产生的现金流量净额与营业收入之比=经营活动产生的现金流量净额（TTM）/营业收入（TTM）。属于质量类因子。数据更新时间：T日21点30分。

def run_formula(dv):
    # CashRateOfSalesLatest = NOCF/OR
    # NOCF -- 经营活动产生的现金呢流量净额(TTM)
    # OR   -- 营业收入(TTM)

    # 营业收入(TTM)
    if 'oper_rev' not in dv.fields:
        dv.add_field('oper_rev')
    # 经营活动产生的现金流量净额
    if 'net_cash_flows_oper_act' not in dv.fields:
        dv.add_field('net_cash_flows_oper_act')
    
    CashRateOfSalesLatest = dv.add_formula("CashRateOfSalesLatest","net_cash_flows_oper_act/oper_rev", is_quarterly=False, add_data=True)
    return CashRateOfSalesLatest