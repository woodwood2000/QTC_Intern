#------------------------------------------------------------------------------

def run_formula(dv):
    alpha6 = dv.add_formula('alpha6', '-BackwardADJ*SRMI', is_quarterly=False, add_data=True)
    return alpha6