#------------------------------------------------------------------------------

def run_formula(dv):
    alpha10 = dv.add_formula('alpha10', '-ASI*Elder', is_quarterly=False, add_data=True)
    return alpha10