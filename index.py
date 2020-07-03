## read a file and push every word to a list

# text = open("Shakespeare.txt", "r")

# text = " This is the 100th Etext file presented by Project Gutenberg, and is presented in cooperation with World Library, Inc., from their Library of the Future and Shakespeare CDROMS.  Project Gutenberg often releases Etexts that are NOT placed in the Public Domain!! "
import re
with open('test.txt', 'r') as myfile:
  text = myfile.read()

# re.sub(r'[^\w\s]','',text)
# print(text)

# x = text.split()

 

x = re.split(' |\n|:|"|;|\.|\'|!|\?|,|>|<', text)

# print(x)

newstr = []

for word in x:
    if word not in newstr:
        newstr.append(word)

for word in range(0, len(newstr)):
    print(newstr[word], text.count(newstr[word]))
