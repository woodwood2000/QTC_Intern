#------------------------------------------------------------------------------
#alpha45 = (RANK(DELTA((((CLOSE \* 0.6) + (OPEN \* 0.4))), 1)) * RANK(CORR(VWAP, MEAN(VOLUME,150), 15)))

def run_formula(dv):
    alpha45 = dv.add_formula('alpha45', 'Rank(Delta(((close*0.6)+(open*0.4)),1)) *  Rank(Correlation(vwap, Ts_Mean(volume, 150), 15))', is_quarterly=False, add_data=True)
    return alpha45