#create frequency distribution containing the given samples
fdist = FreqDist(samples)

#increment the count for this sample
fdist.inc(sample)

#Count the number of times a given sample occurred
fdist['monstrous']

#Frequency of a given sample
fdist.freq('monstrous')

#total number of samples
fdist.N()

#the samples sorted in order of decreasing frequency
fdist.keys()

#iterate over the samples, in order of decreasing frequency
for sample in fdist:

#sample with the greatest count
fdist.max()

#tabulate the frequency distribution
fdist.tabulate()

#Graphical plot of the frequency distribution
fdist.plot(cumulative=True)

#Test if samples in fdist1 occur less frequently than in fdist2
fdist1 < fdist2