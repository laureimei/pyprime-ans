#C0MPOUND INTEREST EXERCISES

def Unit1_compounded_biennially():
    p = 1500 #principal amount
    r = 0.043 # annual interest rate
    t = 6 # years
    n_biennial = 1 / 2  #  compounded biennially

    #  v = total value using the compound interest formula
    V = p * (1 + r / n_biennial) ** (n_biennial * t)

    solution = round(V, 2)     # round to 2dp
    return solution
    raise NotImplementedError()
