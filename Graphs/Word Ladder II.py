begin = input("Enter the Begin Word : ")
end = input("Enter the End Word : ")
wordlist = eval(input("Enter the Word List : "))
wordlist = set(wordlist)
from collections import deque
Queue = deque()
Queue.append([begin])
result = []
min_length = float("inf")
used_words = []
used_words.append(begin)
while(len(Queue) != 0):
    levelsize = len(Queue)
    for i in range(levelsize):
        words = Queue.popleft()
        word = words[-1]
        if word != end:
            for i in range(len(word)):
                left = word[:i]
                right = word[i+1:]
                for j in range(97,123):
                    check = left + chr(j) + right
                    if check in wordlist:
                        used_words.append(check)
                        words.append(check)
                        Queue.append(list(words))
                        words.pop()
        elif word == end:
            if len(words) < min_length:
                result = []
                result.append(words)
                min_length = len(words)
            elif len(words) == min_length:
                result.append(words)
    for i in used_words:
        if i in wordlist:
            wordlist.remove(i)
if len(result) == 0 :
    print("No POssible Combinations Available !!")
else:
    print("Minimum Number of Steps from ",begin," to ",end," : ",len(result[0]))
    print("All Possible Combinations are : ")
    for i in result:
        for j in i:
            print(j,end = " ")
        print()