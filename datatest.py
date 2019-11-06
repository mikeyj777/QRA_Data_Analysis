import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#number of scenarios to generate data for.
n=100

#get random frequencies of loss of containment scenarios (bet 1e-12 and 5e-7)
frequencies = np.random.randint(low=1, high=500000, size=n)/1e12


#get a normal distribution of probabilities of injury to associate with a loss of containment.  project between 0 and 1.
injuryprob=np.random.normal(loc=0.5,scale=1.0,size=n)
minval = min(injuryprob)
maxval = max(injuryprob)
injuryprob -= minval
injuryprob /= (maxval-minval)

#scale probability by occupancy -> estimate number of injuries
b280WestOccupancy=533/3
numinjuries=np.around(b280WestOccupancy * injuryprob)
print(numinjuries)

#load to dataframe and generate a cumulative sum of frequencies.
df = pd.DataFrame({'f':frequencies, 'n':numinjuries})

#the code below should work in power bi for this dataset, but doesn't.
df = df.sort_values(['n', 'f'], ascending=[False, True])

print(df.head)

df['fcum'] = df['f'].cumsum()

print(df)

#plot exceedence on log-log scale

fig = plt.figure()
ax = plt.gca()
ax.plot(df['n'] ,df['fcum'], 'o', c='blue', alpha=0.5, markeredgecolor='none')
ax.plot([1, 10, 1000], [0.01, 0.001, 0.00001], c = 'red')
ax.plot([1, 10, 1000], [0.0001, 0.00001, 0.0000001], c = 'green')
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel('N or More Injuries')
plt.ylabel('Cumulative Frequency')

plt.show()

a=2
