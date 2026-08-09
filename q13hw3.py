import numpy as np

'''
    The code simulates what would happen if you repeatedly sampled from a Gamma distribution
    and tried to estimate its parameters without knowing the true values. It does this 10,000 
    times — each time drawing 50 random numbers, computing the sample mean and variance, 
    and plugging them into the Method of Moments formulas to get estimates for alpha and beta. 
    At the end, it averages all 10,000 estimates and compares them to the true parameters. 
    If the averages are close to the true values, the estimators are unbiased; 
    if they're consistently off in one direction, they're biased.

    result:
        True alpha: 3.0,  Mean estimate: 3.1838
        True beta:  2.0,  Mean estimate: 1.9851
    
    The results confirm that alpha is biased and beta is approximately unbiased.
'''

true_alpha = 3.0
true_beta  = 2.0
n          = 50
num_trials = 10000

alpha_estimates = []
beta_estimates  = []

for _ in range(num_trials):
    sample    = np.random.gamma(shape=true_alpha, scale=true_beta, size=n)
    xbar      = np.mean(sample)
    s2        = np.var(sample, ddof=1)
    alpha_hat = xbar**2 / s2
    beta_hat  = s2 / xbar
    alpha_estimates.append(alpha_hat)
    beta_estimates.append(beta_hat)

print(f"True alpha: {true_alpha},  Mean estimate: {np.mean(alpha_estimates):.4f}")
print(f"True beta:  {true_beta},  Mean estimate: {np.mean(beta_estimates):.4f}")