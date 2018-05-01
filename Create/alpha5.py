#------------------------------------------------------------------------------

def run_formula(dv):
    alpha5 = dv.add_formula('alpha5', '-HBETA*DDNSR', is_quarterly=False, add_data=True)
    return alpha5