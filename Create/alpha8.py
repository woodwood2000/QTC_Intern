#------------------------------------------------------------------------------

def run_formula(dv):
    alpha8 = dv.add_formula('alpha8', 'ETP5*FY12P', is_quarterly=False, add_data=True)
    return alpha8