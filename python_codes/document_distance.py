import sys,string,math
transtable=str.maketrans(string.punctuation+string.ascii_uppercase,' '*len(string.punctuation)+string.ascii_lowercase)
def dotProduct(list1,list2):
    Sum=0
    for word in list1:
        if word in list2:
            Sum+=list1[word]*list2[word]
    return Sum
def calculateDistance(wordlist1,wordlist2):
    numerator=dotProduct(wordlist1,wordlist2)
    denominator=math.sqrt(dotProduct(wordlist1,wordlist1)*dotProduct(wordlist2,wordlist2))
    return math.acos(numerator/denominator)
def countWords(text):
    words={}
    for word in text:
        if word in words:
            words[word]=words[word]+1
        else:
            words[word]=1
    return words
def getWords(file):
    try:
        with open(file,'r') as f:
            data=f.read()
            data=data.translate(transtable)
            words=data.split()
            return words
    except IOError:
        print("Error opening file")
        sys.exit()
def distance(file1,file2):
    text1=getWords(file1)
    text2=getWords(file2)
    wordcount1=countWords(text1)
    wordcount2=countWords(text2)
    result=calculateDistance(wordcount1,wordcount2)
    return result
print(distance('demo.txt','dmeo2.txt'))
