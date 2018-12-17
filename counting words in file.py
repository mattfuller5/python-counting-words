
def remove_special_characters(word):
    new_word=""
    for character in word:
        ascii_code=ord(character)
        if ascii_code>=ord("a") and ascii_code<=ord("z"):
            new_word=new_word+character
    return new_word
    
file=open("proxy-clean-text.txt","r+")
wordcount={}
for word in file.read().lower().split():
    word=remove_special_characters(word)
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]=wordcount[word]+1
for item in wordcount.items(): print("{}:\n{}".format(*item))



        
        

