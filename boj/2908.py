word = input().split()
word1 = int(word[0][2] + word[0][1] + word[0][0])
word2 = int(word[1][2] + word[1][1] + word[1][0])
if word1 > word2:
    print(word1)
else: print(word2)