special_characters=[".",",",":"]
file=open("proxy-clean-text.txt","r+")
wordcount={}
for word in file.read().split():
    for special_character in special_characters:
        word=word.replace(special_character,"")
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]=wordcount[word]+1
for item in wordcount.items(): print("{}\t{}".format(*item))

        
        

