# input string1 = "alogorithms", string2 = "alchemist"
# return 5 "alhms"

def longestCommonSubsequence (string1, string2):
    result = 0
    table = [[0 for x in range(len(string2)+1)] for x in range(len(string1)+1)]