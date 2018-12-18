
#Input: The list in a random order
#Output: The list in descending order
def bubble_sort(list):   
    length=len(list)
    switched=True
    while switched == True:
        switched=False
        for x in range (1,length):
            if list[x-1][1]<list[x][1]:
                temp=list[x-1]
                list[x-1]=list[x]
                list[x]=temp
                switched=True
            
    return list

def remove_special_characters(word):
    new_word=""
    for character in word:
        ascii_code=ord(character)
        if ascii_code>=ord("a") and ascii_code<=ord("z"):
            new_word=new_word+character
    return new_word

file_name=input("please enter the file name you would like to be scanned")
file=open(file_name,"r+")
wordcount={}

for word in file.read().lower().split():
    word=remove_special_characters(word)
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]=wordcount[word]+1
sort=bubble_sort(list(wordcount.items()))

for item in sort: print(item[0] + ": " + str(item[1]))

    


        
        

