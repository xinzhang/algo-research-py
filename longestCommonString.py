# input string1 = "alogorithm", string2 = "alchemist"
# return 2 "al"

# input "abcdxyz", "xyzabcd"
# return 4 "abcd"

# use + 1 to add a 0 data outerside
def longestCommonString(string1, string2):
    result = 0
    table = [[0 for x in range(len(string2)+1)] for x in range(len(string1)+1)]

    for x in range(1, len(string1)+1):
        for y in range(1, len(string2)+1):
            if string1[x-1] != string2[y-1]:
                table[x][y] = 0
            else:
                table[x][y] = table[x-1][y-1] + 1
                result = max(result, table[x][y])

    # for x in range(len(string1)):
    #     print(table[x])

    return result

print(longestCommonString("alogorithm", "alche"))
print(longestCommonString("abcdxyz", "xyzabcd"))



