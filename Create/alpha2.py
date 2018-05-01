#------------------------------------------------------------------------------

def run_formula(dv):
    alpha2 = dv.add_formula('alpha2', '-WVAD*VOL60', is_quarterly=False, add_data=True)
    return alpha2