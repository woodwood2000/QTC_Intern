#------------------------------------------------------------------------------
#alpha156 = (MAX(RANK(DECAYLINEAR(DELTA(VWAP, 5), 3)), RANK(DECAYLINEAR(((DELTA(((OPEN * 0.15) + (LOW *0.85)),2) / ((OPEN * 0.15) + (LOW * 0.85))) * -1), 3))) * -1)

def run_formula(dv):
    alpha156 = dv.add_formula("alpha156","(Max(Rank(Decay_linear(Delta(vwap, 5), 3)), Rank(Decay_linear(((Delta(((open * 0.15) + (low *0.85)),2) / ((open * 0.15) + (low * 0.85))) * -1), 3))) * -1)", is_quarterly=False, add_data=True)
    return alpha156