input_list = [str(x) for x in input("Enter the input string: ").split()]

wordDict = {}

for word in input_list:
    if word in wordDict.keys():
        wordDict[word] += 1
    else:
        wordDict[word] = 1

for key in sorted(wordDict.keys()):
    print(f'{key} appears {wordDict[key]} times')