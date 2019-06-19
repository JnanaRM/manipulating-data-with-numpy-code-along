# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
data = np.genfromtxt(path,dtype='U',delimiter=',')

# Number of unique matches 
data_noheader = data[1:,]
matches = data_noheader[:,0]
print('Number of unique matches : ',np.unique(matches).size)

 # How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.

# Number of unique teams
team1 = np.unique(data_noheader[:,3])
team2 = np.unique(data_noheader[:,4])
team = np.concatenate((team1,team2))

 # this exercise deals with you getting to know that which are all those six teams that   played in the tournament.
print('all unique teams that played in the matches - ',np.unique(team))
# Sum of all extras
print('Sum of all extras : ',np.sum(data_noheader[:,17].astype(np.int)))
 # An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out

 # Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
out = data_noheader[:,21] != ''
print('Delivery number when a given player got out : ',data_noheader[out][:,11], 
'& wicket type  :',data_noheader[out][:,21])
# Number of times Mumbai Indians won the toss
print('Number of matchess Mumbai Indians have won the toss :',np.unique(data_noheader[data_noheader[:,5] == 'Mumbai Indians'][:,0]).size)
 # this exercise will help you get the statistics on one particular team

# Filter record where batsman scored six and player with most number of sixex

 # An exercise to know who is the most aggresive player or maybe the scoring player 
six = data_noheader[:,16].astype(np.int) == 6
d1 = dict(Counter(data_noheader[six][:,13]))
highest=max(d1.values())
print('Batsmen who scored max number of sixes: ',[k for k, v in d1.items() if v == highest])







