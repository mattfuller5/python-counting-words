def remove_special_characters(word):
    for special_character in special_characters:
        word=word.replace(special_character,"")
    return word
    

special_characters=[".",",",":"]
file=open("proxy-clean-text.txt","r+")
wordcount={}
for word in file.read().lower().split():
    word=remove_special_characters(word)
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]=wordcount[word]+1
for item in wordcount.items(): print("{}\t{}".format(*item))



        
        

