'''
    https://www.github.com/MahmoudSfn
    file description: lexer | file code analyser, based on a regular expression table (to be edited) | 
	then the code analyse a .txt file line by line, word by word, comparing it to the pattern in the regexp table
    edited at: 22/04/2019    
'''
import re
import sys

#define the regular expression table
regExps = [    
    (r'\=', 'EqualSign'), 
    (r'[a-zA-Z]\w*', 'variable'),
    (r'\d+\.\d+', 'FloatNumber'),
    (r'\d+', 'IntegerNumber') 
]
# open the code file
file = open("test.txt","r") 
LineNumber = 0
WordInLine = 0

for line in file:
    LineNumber = LineNumber + 1
    line = line.strip("\n") # to remove the new line (\n) from the line
    print("\nin line : \" " + line + " \" ")
    WordInLine = 0
    for code in line.split(): # eachcode is a word
        WordInLine = WordInLine + 1 # to get the position of each word in the line to display more detail about the error
        # parcourir le tableau et comparer
        found = False
        for pattern in regExps:
            # regexp, meaning = pattern
            count = 0
            for x in pattern:
                if count == 0:
                    regexp = x
                    count = 1
                else:
                    meanning = x
            if re.search(regexp, code) is not None: # 
                print(code + " match to " + str(meanning)) # displaying the code and signification in regular expression table
                found = not False
                break # stop running the table when its compatible to a reg exp
        if found != True:
            print("error! position: [ line: " + str(LineNumber) + " ; word: \' " + code + " \'; word position" + str(WordInLine) + " ] ")
            found = not True

# print(file.read())




'''
$ python lexer.py

in line : " () "
error! position: [ line: 1 ; word: ' () '; word position1 ]

in line : " a = 12 "
a match to variable
= match to EqualSign
12 match to IntegerNumber

in line : " b = 12.3 "
b match to variable
= match to EqualSign
12.3 match to FloatNumber

in line : " c = 3.4 "
c match to variable
= match to EqualSign
3.4 match to FloatNumber
'''