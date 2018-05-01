#------------------------------------------------------------------------------

def run_formula(dv):
    alpha1 = dv.add_formula('alpha1', '-BBI*TEMA10', is_quarterly=False, add_data=True)
    return alpha1