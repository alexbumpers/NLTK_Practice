##create a conditional frequency distribution from a list of pairs
cfdist = ConditionalFreqDist(pairs)

##Alphabetically sorted list of conditions
cfdist.conditions()

##Frequency distribution for this condition
cfdist[condition]

##Frequency for given sample for this condition
cfdist[condition][sample]

##Tabulate conditional frequency distribution
cfdist.tabulate()

##Tabulation limited to specified examples and conditions
cfdist.tabulate(samples, conditions)

##Graphical plot of the conditional frequency distribution
cfdist.plot()

##Graphical plot limited to the specified samples and conditions
cfdist.plot(samples, conditions)

##Test if samples in cfdist1 occur less frequently than in cfdist2
cfdist1 < cfdist2
