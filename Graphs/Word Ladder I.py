begin = input("Enter the Begin Word : ")
end = input("Enter the End Word : ")
wordlist = eval(input("Enter the Word List : "))
wordlist = set(wordlist)
from collections import deque 
Queue = deque()
Queue.append((begin,1))
while(len(Queue) != 0):
    word,step = Queue.popleft()
    for i in range(len(word)):
        left = word[:i]
        right = word[i+1:]
        for i in range(97,123):
            check = left+chr(i)+right
            if check in wordlist:
                if check == end:
                    ans = step + 1
                else:
                    wordlist.remove(check)
                    Queue.append((check,step+1))

if len(Queue) == 0:
    print("Minimum Number of Steps from ",begin," -> ",end, " : ",ans)
else:
    print("Word Combination not Possible !!")
