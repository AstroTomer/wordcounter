try:
    file=open("text.text", "r")
    words = []
except Exception as e:
    print(e)
for line in file:
    words.extend(line.split())
file.close()
words2=[]
for word in words:
    if word not in words2:
        words2.append(word)
words3: dict={}
temp={}
for word in words2:
    temp={(word,words.count(word))}
    words3.update(temp)
words4=sorted(words3.items(), key=lambda x: x[1], reverse=True)
N=input("enter the number of words you want sorted")
N=int(N)
for i in range (N):
    word=str(words4[i][0])
    amount=str(words4[i][1])
    print("word "+word+" "+amount+" times")

