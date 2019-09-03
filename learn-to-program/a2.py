def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)

def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''

    return dna.count(nucleotide,)

def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    
    return dna2 in dna1

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence is valid.
    Lowercase characters are not valid. 
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('BTCGGC')
    False
    '''
    validity = True
    for char in dna:
        if not char in 'ATCG':
            validity = False
    return validity

def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str
    
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index
    
    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('ATGC', 'CG', 4)
    ATGCCG
    '''
    return dna1[0:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    ''' (str) -> str

    Return the nucleotide's complement
    
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    >>> get_complement('T')
    'A'
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'T':
        return 'A'

def get_complementary_sequence(dna):
    ''' (str) -> str

    Return the DNA sequency that is complementary to the given DNA sequency
    
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('ATCGGC')
    'TAGCCG'
    '''
    result=''
    for nucleotide in dna:
        result += get_complement(nucleotide)
    return result
    
