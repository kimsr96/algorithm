sentence = input()
remove_space = sentence.strip()
word = remove_space.split(" ")
count = [i for i in word if i != '']
print(len(count))