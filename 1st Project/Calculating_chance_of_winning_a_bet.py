#To calculate the chance of reaching on step 60 or more of the empire state building, based on the outcomes of the roll of a dice. 
#Import libraries and sub packages
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulation of random walk 500 times
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Created and plotted np_aw_t(transpose of all_walks to obtain the end points of all the random walks)
np_aw_t = np.transpose(np.array(all_walks))
print(np.array(all_walks))
print(all_walks)
print(np_aw_t)
# Selected last row from np_aw_t: ends
ends = np_aw_t[-1]
print(ends)

# Plotted histogram of ends
plt.hist(ends)
plt.show()

# chance that the end point is greater than or equal to 60
count = 0
for x in range(500):
    if ends[x] >= 60:
        count = count + 1 
    else:
        count = count 
print(count)
chance = count/500
print(chance)
