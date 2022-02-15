

def getSetFromWord(word):

    s = set()

    for i in word:

        s.add(i)

    return s



def getLongestWordFromSentence(sentence):

    longest = 0

    longest_w = ""

    for j in range(len(sentence)):

        if(len(sentence[j]) > longest):

            longest_w = sentence[j]

            longest = len(longest_w)

    return longest_w





filename = "test.txt"

sentences = []

counter = 1



with open(filename, "r") as file:

    for line in file:

        if(counter%2 == 0):

            sentences.append(line)

        counter += 1



words = [sentences[0].split(), sentences[1].split()]



longest_word = []

for i in range(len(words)):

    longest_word.append(getLongestWordFromSentence(words[i]))

print("Longest word in each line: ", longest_word)



for i in range(len(longest_word)):

    longest_word[i] = longest_word[i][3:]



set_1 = getSetFromWord(longest_word[0])

set_2 = getSetFromWord(longest_word[1])

print("Symmetric difference: ", set_1.symmetric_difference(set_2))