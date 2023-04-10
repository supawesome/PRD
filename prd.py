import math
import random

import numpy as np


def get_prob_from_c(c: float) -> float:
    """Straightforward computes expected value using C and returns probability"""
    # 1st iteration:
    expected_value = c
    prob = c
    cumulative_product = 1

    # from 2nd to (n-1)th iteration:
    n = int(np.ceil(1 / c))

    for i in range(2, n):
        cumulative_product *= 1 - (i - 1) * c
        prob_i = cumulative_product * (i * c)
        prob += prob_i
        expected_value += i * prob_i

    # nth (last) iteration:
    prob_i = 1 - prob
    expected_value += n * prob_i

    return 1 / expected_value



def get_c_from_prob(p: float) -> float:
    """Returns С from given probability"""
    upper_bound = p
    lower_bound = 0.0
    c = 0.0
    prev_prob = 0
    curr_prob = 1.0

    while math.fabs(prev_prob - curr_prob) >= 0:
        c = (upper_bound + lower_bound) / 2.0
        prev_prob = get_prob_from_c(c)

        if math.fabs(prev_prob - curr_prob) <= 0:
            break

        if prev_prob > p:
            upper_bound = c
        else:
            lower_bound = c

        curr_prob = prev_prob

    return c


def test_prob_from_c(c: float, iterations: int) -> float:
    """Returns experimental probability for a given C with a given number of iterations"""
    sum_of_trials = 0

    for _ in range(iterations):
        n = 1

        while (c * n) < 1.0 and random.random() > (c * n):
            n += 1

        sum_of_trials += n
    
    av_iters = float(sum_of_trials) / iterations

    return 1 / av_iters


def generate_pr_sample(p: float, size: int) -> np.ndarray:
    """Generates sample out of pseudo-random distribution,
    where 1 means success (or Proc), and 0 means opposite (absence of Proc)
    """
    c = get_c_from_prob(p) 
    n = 0
    sample = []

    for i in range(size):
        n += 1
        if c * n <= random.random():
            sample.append(0)
        else:
            sample.append(1)
            n = 0

    return np.asarray(sample, dtype=int)


def generate_sequence_sample(sample: np.ndarray) -> np.ndarray:
    """Generates sample of sequences, i.e. number of trials before success (Proc), 
    including the one with a Proc
    """
    trials_before_success = 0
    result = []

    for observation in sample:
        trials_before_success += 1
        if observation == 1:
            result.append(trials_before_success)
            trials_before_success = 0

    return np.asarray(result, dtype=int)
