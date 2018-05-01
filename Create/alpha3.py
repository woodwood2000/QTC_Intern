#------------------------------------------------------------------------------

def run_formula(dv):
    alpha3 = dv.add_formula('alpha3', '-STM*TVSTD20', is_quarterly=False, add_data=True)
    return alpha3