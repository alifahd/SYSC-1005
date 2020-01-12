import string

def build_concordance(filename):
    """ (str) -> dict of str, list pairs
    Return a dictionary in which the keys are the words in the
    specified file. The value associated with each key is a list
    containing the line numbers of all the lines in which each word
    occurs.
    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    
    infile = open(filename, "r")
    hist = {}
    lineNumber = 0
    for line in infile:
        lineNumber = lineNumber + 1
        # Split each line into a list of words.
        # The split method removes the whitespace from around each word.
        
        word_list = line.split()

        # For each word, remove any punctuation marks immediately
        # before and after the word, then convert it to lower case.
        
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            
            # or, 
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Don't count any empty strings created when the punctuation marks
            # are removed. For example, if word is bound to a hyphen, '-',
            # word.strip(string.punctuation) yields the empty string, ''.
            
            if word != '':
                if word not in hist:
                    hist[word] = []
                if lineNumber not in hist[word]:                        
                    hist[word].append(lineNumber)

            # or simply,
            # hist[word] = hist.get(word, 0) + 1 
            
    return hist