import pandas as pd

""" 
Data are from a large scale dataset of the Consideration of Future Consequences Scale. from https://openpsychometrics.org/_rawdata/.

About the dataset. 
Q1-Q12: Responses are on a 1-5 likert scale, 1 = extremely UNCHARACTERISTIC .... 5 = extremely CHARACTERISTIC

In general, a high score is future oriented.
These items need to be reverse coded: (Q3, Q4, Q5, Q9, Q11, Q12)
		
We also have these columns:
	Age (integer)
	Gender (1=male, 2=female, 3=other, 0=did not answer)
	Accuracy (how accurate 0-100 were your answers about yourself?)
"""

############################
## Loading data in pandas ##
############################
df = pd.read_csv("cfsc.csv")
df.head() # visualize the first few rows of data.

############################
## More pandas basics ######
############################

# get data from a column, Q1.
df["Q1"].values

# add a new column, gender as a string.
gender_str = []
map = {0 : "did_not_answer", 1 : "male" , 2 : "female", 3 : "other"}
for gender_int in df["gender"]:
	str = map[gender_int]
	gender_str.append(str)
df["gender_str"] = gender_str

############################
## Exercise 1 ##############
############################

"""
Please score the survey for each participant, and write the data to a new column called "score".

Version 1: Just add columns Q1 thru Q12.
Version 2: Columns Q3, Q4, Q5, Q9, Q11, and Q12 should be reverse scored (1-->5, 2-->4, etc.). Please add this feature.
Version 3: There are some missing values (scored as 0). Do something intelligent with these (for example, impute the participant's mean).
"""

#############################
### Slicing in pandas #######
#############################

# you can get a subset of data , meeting some condition, like this:
slc = df[df["gender"] == 1]

##############################
### Exercise 2 ##############
#############################

"""
You wonder if there are age or gender differences in the survey:
1. For males (gender=1) vs. females (gender=2), calculate the mean score. 
	Bonus: t test the groups.  (scipy.stats.ttest_ind)
2. Correlate age with score  : scipy.stats.pearsonr.
"""
