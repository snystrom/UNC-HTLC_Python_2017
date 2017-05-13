#!/usr/bin/python3
import random
random.seed(123) # Set seed for reproducibility.

def randFasta(nSeq = 0, minLen = 10, maxLen = 100):
    # Generates random DNA sequences of random length, outputs with fasta headers
    bases = ['A', 'T', 'G', 'C']
    headers = []
    sequences = []
    
    for i in range(1, nSeq+1):
        
        seqLen = random.randint(minLen, maxLen)
        randSequence = [random.choice(bases) for _ in range(1, seqLen)] # Generate random DNA sequence of random length
        seqString = ''.join(randSequence) # Combine sequence into a string
        header = '>Seq_{0}'.format(i)     # Generate unique header for each sequence
        
        headers.append(header)
        sequences.append(seqString)
        
    output = [] 
    for head, seq in zip(headers, sequences):
        entry = head + '\n' + seq + '\n'
        output.append(entry)
        
    return(output)
   
myDNA = randFasta(nSeq = 100, minLen = 50, maxLen = 250)

with open('myDNA.fa', 'w') as fasta:
    for entry in myDNA:
        fasta.write(entry)
