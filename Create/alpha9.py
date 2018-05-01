#------------------------------------------------------------------------------

def run_formula(dv):
    alpha9 = dv.add_formula('alpha9', '-KDJ_D*MTM', is_quarterly=False, add_data=True)
    return alpha9