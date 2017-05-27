#!/usr/bin/python3
import random
import numpy as np

def randFasta(nSeq = 0, minLen = 10, maxLen = 100):
    # Generates random DNA sequences of random length, outputs with fasta headers
    bases = ['A', 'T', 'G', 'C']
    headers = []
    sequences = []

    for i in range(1, nSeq+1):

        seqLen = random.randint(minLen, maxLen)
        randSequence = [random.choice(bases) for _ in range(0, seqLen)] # Generate random DNA sequence of random length
        seqString = ''.join(randSequence) # Combine sequence into a string
        header = '>Seq_{0}'.format(i)     # Generate unique header for each sequence

        headers.append(header)
        sequences.append(seqString)

    output = []
    for head, seq in zip(headers, sequences):
        entry = head + '\n' + seq + '\n'
        output.append(entry)

    return(output)

def makeRandomFastaFromPWM(pssm, nSeq = 1):
    # Takes position weight matrix as input, generates given number of Fasta format sequences according to PWM
    bases = ['A', 'T', 'G', 'C']
    sequences = []
    headers = []

    for i in range(1, nSeq+1):
        seq = []

        for position in range(0, len(pssm)):
            pBase = pssm[position]
            base = np.random.choice(bases, p = pBase)
            seq.append(base)

        sequence = ''.join(seq)
        header = '>Seq_{0}'.format(i)

        sequences.append(sequence)
        headers.append(header)

    output = []
    for head, seq in zip(headers, sequences):
        entry = head + '\n' + seq + '\n'
        output.append(entry)

    return(output)

def writeArrayToFile(array, fileName):
    with open(fileName, 'w') as outfile:
        for entry in array:
            outfile.write(entry)

if __name__ == "__main__":

    random.seed(123) # Set seed for reproducibility.

    # Generate random fasta file
    myDNA = randFasta(nSeq = 100, minLen = 50, maxLen = 250)
    writeArrayToFile(myDNA, '../Data/myDNA.fa')


    # PWM to generate sequences from:
    # Each array is probability of occurrance of each basepair at a given position (Position-specific scoring matrix [PSSM])
    #         'A', 'T', 'G', 'C'
    pBase1 = [0.8, 0.2, 0, 0]
    pBase2 = [0.1, 0.1, 0.7, 0.1]
    pBase3 = [0.1, 0.8, 0.05, 0.05]
    pBase4 = [0.8, 0.1, 0.05, 0.05]
    pBase5 = [0.1, 0.1, 0.1, 0.7]
    pBase6 = [0.2, 0.8, 0, 0]

    # Actual weight matrix
    pssm = [pBase1, pBase2, pBase3, pBase4, pBase5, pBase6]

    PWMset = makeRandomFastaFromPWM(pssm, nSeq = 100)
    writeArrayToFile(PWMset, '../Data/PWM.fa')

