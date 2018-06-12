import numpy as np
from scipy import stats

def score(arr):

    score = 0
    for i in arr:
        score = score + arr[i]
    return score


def cohens_d(arr1, arr2):

    M1 = np.mean(arr1)
    M2 = np.mean(arr2)
    N1 = len(arr1)
    N2 = len(arr2)
    TOTAL_N = N1+N2
    SD1 = np.std(arr1)
    SD2 = np.std(arr2)

    numerator = M1 - M2
    denominator = (SD1 * (N1/TOTAL_N)) + (SD2 * (N2/TOTAL_N))
    return numerator / denominator


def bootstrapped_ci(arr, n_bootstraps=10000):

    Ms = []
    N = len(arr)
    for _ in range(n_bootstraps):
        sample = np.random.choice(arr, N, replace=True)
        Ms.append(np.mean(sample))

    ci =(np.percentile(Ms, 2.5), np.percentile(Ms, 97.5))
    return ci

def remove_missing(arr):
    return [v for v in arr if str(v) != '.']
