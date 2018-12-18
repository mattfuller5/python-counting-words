file=open("proxy-clean-text.txt","r+")
wordcount={}
for word in file.read().split():
    
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]=wordcount[word]+1
for item in wordcount.items(): print("{}\t{}".format(*item))

        
        

