import pandas as pd
from scipy.stats import pearsonr 
import numpy as np

## helper functions ##
def reverse_score(v):
	map = {1:5, 2:4, 3:3, 4:2, 5:1, 0:0, -1:-1}
	return map[v]

def score(responses, reverse_indices = [2,3,4,8,10,11]):
	out = 0
	for idx, response in enumerate(responses):
		if idx in reverse_indices:
			response = reverse_score(response)
		out += response
	
	return out

# load the data
df = pd.read_csv("cfsc.csv")

### score the survey ###
scores = []
q_columns = ["Q{}".format(_) for _ in range(1, 13)]
for row in df.iterrows():
	responses = row[1][q_columns].values
	scored_responses = score(responses)
	scores.append(scored_responses)
df["score"] = scores

### scores by gender ###
men = np.mean(df[df.gender==1].score)
women = np.mean(df[df.gender==2].score)
	
### correlate age with score ###
r, p = pearsonr(df.age, df.score)

