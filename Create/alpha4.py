#------------------------------------------------------------------------------

def run_formula(dv):
    alpha4 = dv.add_formula('alpha4', '-ACD20*AR', is_quarterly=False, add_data=True)
    return alpha4