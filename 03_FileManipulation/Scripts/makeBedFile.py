#!/usr/bin/python
import random
import numpy as np

random.seed(123)
np.random.seed(123)

chrNames = ['chrX', 'chr2L', 'chr2R', 'chr3R', 'chr3L']
chrStart = 1
chrEnd = 120000000
behavior = ['opening', 'closing', 'static']
pBehavior_unbound = [0.2, 0.2, 0.6]
pBehavior_bound = [0.8, 0.1, 0.1]
binding = ['bound', 'unbound']
pBinding = [0.25, 0.75]

def randomPeakType(chrNames, chrStart, chrEnd, behavior, binding):
    ChIP_type = np.random.choice(binding, p = pBinding)
    
    if ChIP_type == 'bound':
        peakType = np.random.choice(behavior, p = pBehavior_bound) 
    else:
        peakType = np.random.choice(behavior, p = pBehavior_unbound)
    
    chromosome = random.choice(chrNames)
    start = random.randint(chrStart, chrEnd)
    
    if ChIP_type == 'bound':
        width = random.randint(20, 100)
    else:
        width = random.randint(550, 1000)
        
    end = start + width

    if end > chrEnd:
        end = chrEnd


    peak = [chromosome, str(start), str(end), peakType, ChIP_type]
    return(peak)

peaks = []
for i in range(0,500):
    peak = randomPeakType(chrNames, chrStart, chrEnd, behavior, binding)
    line = '\t'.join(peak)
    peaks.append(line)

with open('../Data/chip-seq.bed', 'w') as outfile:
    for peak in peaks:
        line = peak + '\n'
        outfile.write(line)
