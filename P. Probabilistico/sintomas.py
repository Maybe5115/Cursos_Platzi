
def calc_bayes(prior_A, pBdadoA, pB):
    return (prior_A*pBdadoA/pB)

if __name__ == "__main__":
    p_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10/99999
    prob_no_cancer = 1-p_cancer

    prob_sintoma = (prob_sintoma_dado_cancer * p_cancer) + (prob_sintoma_dado_no_cancer*prob_no_cancer)

    p_cancer_dado_sintoma = calc_bayes(p_cancer, prob_sintoma_dado_cancer, prob_sintoma)

    print(p_cancer_dado_sintoma)

