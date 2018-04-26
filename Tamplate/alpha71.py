#------------------------------------------------------------------------------
#alpha71 = (CLOSE-MEAN(CLOSE,24))/MEAN(CLOSE,24)*100

def run_formula(dv):
    alpha71 = dv.add_formula('alpha71', '(close-Ts_Mean(close, 24))/Ts_Mean(close, 24)*100', is_quarterly=False, add_data=True)
    return alpha71