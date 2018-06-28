
"""
Matplotlib/Plotting Basics: 6/25/18

"""

from matplotlib import pyplot as plt
import numpy as np
import random

plt.style.use('seaborn-poster')


""""
FIGURE 1: Bar Graphs.
- Plotting data.
- Formatting plots:
     creating labels that are strings

Given this code, we'll learn to plot the data.
"""

# # # # --- Bar Graphs
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
amount_of_milk =  [6, 9, 4, 0, 9, 0]
error = [0.5, 0.4, 0.9, 0, 0.3, 0] # note! The error bar is + and - this value, e.g. error of 0.5 = error bar spans total of 1.

plt.figure(1) 

# # # Plot the bar graph here
plt.bar(range(len(drinks)), amount_of_milk, yerr=error, capsize=5)

axes1=plt.subplot()
axes1.set_xticks(range(len(drinks)))
axes1.set_xticklabels(drinks)
plt.show()


""""
FIGURE 2: Line plots.
- Plotting data.
- Formatting plots:
     linestyle  /   color     /    markersize.

Given this code, we'll learn to plot another line --- how funny I actually am.
"""

num_xkcd_ive_read = [2, 4, 5, 7, 12]
how_funny_i_think_i_am = [2, 6, 7, 8, 7]
how_funny_i_am = [0, 0, 0, 1, 1]

plt.figure(2)

plt.plot(num_xkcd_ive_read, how_funny_i_think_i_am, linestyle='--', color='green', marker='o')

plt.plot(num_xkcd_ive_read, how_funny_i_am, linestyle=':', color='blue', marker='s')


#other options: marker='*' for star; marker = 's' for square markers
#linestyle=':' for dotted lines; linestyle='' if you're weird and don't actually want a line; 
#'o' to make scatterplot 

#default: if you call pyplot more than once, it will pick different colors for each instance

plt.legend(['How Funny I think I am', 'How funny I am'])     
    
y_lower = [.9*i for i in how_funny_i_think_i_am]
y_lower = [1.1*i for i in how_funny_i_think_i_am]

plt.fill_between(num_xkcd_ive_read, y_lower, y_upper, alpha=.2)  # you can use this for confidence intervals!

plt.axis([0, 14, 0, 10]) # order of x_min, x_max, y_min, y_max

plt.xlabel('Number of xkcd comics I have read')
plt.ylabel('Funny-ness')
plt.title('Effect of xkcd Comics on my funniness')

plt.show() #plot is not actually outputted until this command

""""
FIGURE 3: Histogram.
- Plotting data.
- Formatting plots:
     creating labels that are strings

Given this code, we'll learn to plot two histograms and deal with common histogram problems.
"""

# # # # --- Histograms
plt.figure(3)

norm_vals1 = np.random.normal(loc=5, scale=.5, size=(100,1))
norm_vals2 = np.random.poisson(lam=15, size=(10,1))

#############
#############
# what is the difference between running A and B?
#A
#plt.hist(norm_vals1, alpha=.5,)
#plt.hist(norm_vals2, alpha=.5,)
#
#B
#plt.hist(norm_vals1, alpha=.5, normed=True)
#plt.hist(norm_vals2, alpha=.5, normed=True)
#

#############
#############

plt.show()


""""
FIGURE 4: Complex Bar Graphs.
- Plotting data.

Given this code, we'll look at how to graph data side-by-side
"""

# # # # --- Complex Bar Graphs-side by side bars

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
amount_of_milk =  [6, 9, 4, 0, 9, 0]
amount_of_regret = [7, 10, 3, 1, 10, 2]

plt.figure(4) 
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = .8 # Width of each bar
x_vals1 = [t*element + w*n for element
             in range(d)]
axes4 = plt.subplot()
axes4.set_xticks(x_vals1)
axes4.set_xticklabels(drinks)
plt.bar(x_vals1, amount_of_milk)

n = 2 # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = .8 # Width of each bar
x_vals2 = [t*element + w*n for element
             in range(d)]

# # # plot the second set of x_values and the data for amount_of_regret
plt.title("Lactose Intolerance")
plt.xlabel('Coffee Drink')
plt.legend(['Milk', 'Regret'])

plt.show()


"""
FIGURE 5: Multiple plots in the same figure ("subplots").
You can make more than one plot in the same figure.
Here we'll learn to:

--- Make a figure with multiple plots : called subplots.
---- Adjust these subplots (especially when they overlap with each other

"""


plt.figure(5), figsize=(8,8))
hours_i_am_awake = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
happiness = [1, 1, 2, 5, 6, 6, 7, 6, 7, 4, 5, 7, 8] 
number_of_cookies_eaten = [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 3, 4]
number_of_spiders_seen = [0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]

"""
Here we create 3 separate subplots.
Each time we cut up the graph in different ways:
    - in axes1   : we cut it horizontally in 2 .
    - in axes2 and 3 : we cut it into a 2 X 2 grid.
"""
axes1 = plt.subplot(2,1,1)
plt.plot(hours_i_am_awake, happiness)
plt.xlabel('hours awake')
plt.ylabel('happpiness(self reported)')

axes2 = plt.subplot(2,2,3)
plt.plot(hours_i_am_awake, number_of_cookies_eaten)
plt.xlabel('hours awake')
plt.ylabel('number of cookies eaten (self reported)')

axes3 = plt.subplot(2,2,4)
plt.plot(hours_i_am_awake, number_of_spiders_seen)

plt.xlabel('hours awake')
plt.ylabel('number of spiders seen (self reported)')
# if you plot this now, the labels overlap
plt.subplots_adjust(wspace=.3)
#using the axes object you can edit aspects of a certain subplot
#some important arguments: left/right ==> left/right-side margin; 
#bottom/top ==> bottom/top margin, 
#wspace ==> horizontal space between subplots
#hspace ==> vertical space

plt.show()

#plt.savefig(filename) saves out a png or pdf

#plt.close('all') #close all figures


# # # # --- Download the data from Psychiatric Genomics Consortium
# https://www.med.unc.edu/pgc/results-and-downloads
# download the dataset called "BIP"
# move it to your current directory and import data with: 

filename = 'Bipolar_2010.txt' # I renamed my file because I was lazy
raw_data = np.loadtxt(filename, dtype='str')
print(raw_data.shape)
print(raw_data[0]) # this lists all of your labels for your data; look at these
# look at your data's spread using histograms

# create one line graph with error measurements
# create one side by side bar graph 

