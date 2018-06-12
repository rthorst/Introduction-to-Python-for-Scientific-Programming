# The basic syntax of a function.
def double(i):
    """ input a number i and return i*2 """


    two_i = i * 2
    return two_i


# Functions can take multiple arguments
def multiply(i, factor):
    """ input numbers i and factor, and return (i*factor)"""

    output = i * factor
    return output


# You can make an argument optional by specifying a default value.
def multiply(i, factor=2):
    """ return i*factor, with default factor=2"""

    output = i * factor
    return output


if __name__ == "__main__":

    # initial i.
    i = 2
    print("i = " + str(i))

    # double i.
    doubled = double(i)
    print("double(i) = " + str(doubled))

    # multiply by factor.
    factor = 5
    multiplied = multiply(i, factor)
    print("multiply(i, 5) = " + str(multiplied))
    print("multiply(i) = %s" % multiply(i))


"""
Problem 1: Score a survey.
Your participants took the CRT, which contains 3 items. For each item, 
the participant scores 1 if correct, otherwise 0. Thus, the data for a 
participant looks like:

    scores = [1, 0, 1]     # got questions 0 and 2 right.

Create a function to take the list of scores for a participant, and output
the total score.  (summeed)
"""

"""
Problem 2 : Cohen's d.

A common measure of effect size in psychology is Cohen's d. For 2 arrays, 
Cohen's d is the standardized mean difference. 

    D = (M1 - M2) / (pooled standard deviation).
    
    Assuming equal size , pooled SD = (sd1 + sd2) / 2.
    
Write a function to return cohen's d for 2 arrays.
HINT: 
    np.mean(arr)  : mean of array.
    np.std(arr) : std deviation of array.
    
Challenge: extend to case with unequal size arrays.  (thus pooled SD is weighted average of SD1, SD2).

"""

"""
Bootstrapped confidence interval.

A strong way to compute confidence intervals is called bootstrapping. Say 
your data look this:

    [5, 4.5, 4, 3]
    
    (1) Draw 1,000 samples with replacement from the data (N=4 / sample).
    (2) Record the mean of each sample.
    (3) Compute the 2.5 and 97.5 percentile of the resulting means.
    (4) This is a bootstrapped confidence interval.
    
Write a function to compute a boostrapped confidence interval.

    np.random.choice(a, 4, replace = True):  draw 4 items w/ replacement from a.
    np.mean(arr):  return mean of array.
    np.percentile(a, 50): return 50th percentile of a.
    
Write a helper function to return half the magnitude of the bootstrapped CI
(for plotting).

"""

"""
Done with that?
Pick some statistics from your research that are not available in standard libraries.
Write functions to compute them.
Use this as start of a personal toolbox.
"""

"""
Problem 4: remove missing values.

You have some data, real data are numbers, missing values are denoted by "."
Return the array, with missing values removed.

    Example --- 
    Input: [1, 3, ".", 2]
    Output: [1, 3, 2]
"""
