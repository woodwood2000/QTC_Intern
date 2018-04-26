#------------------------------------------------------------------------------
#alpha14 = CLOSE-DELAY(CLOSE,5)

def run_formula(dv):
    alpha14 = dv.add_formula('alpha14', 'close-Delay(close,5)', is_quarterly=False, add_data=True)
    return alpha14