'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    testWord= word
    fragment='th'
    testWordLength = len(word)
    fragmentLength = len("th")

    if (testWordLength == 0 or testWordLength < fragmentLength):
        return 0

    if (testWord[0: fragmentLength] == fragment):
        return 1 + count_th(testWord[fragmentLength -1:])

   
    return count_th(testWord[fragmentLength -1:])
    
    # TBC
    
print(count_th('thththhththt'))
