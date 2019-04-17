'''
github: MahmoudSfn

file description: lexer | file code analyser
'''
import re
import sys

#define the regular expression table
regExps = [
        (r'[ \n\t]+', None), (r'#[^\n]*', None), (r'for\b', 'FOR'), (r'if\b', 'IF'), (r'else\b', 'ELSE'), (r'break\b', 'BREAK'), (r'while\b', 'WHILE'), 
        (r'return\b', 'RETURN'), (r'struct\b', 'STRUCT'), (r'typedef\b', 'TYPEDEF'), (r'sizeof\b', 'SIZEOF'), (r'switch\b', 'SWITCH'), (r'case\b', 'CASE'), 
        (r'default\b', 'DEFAULT'), (r'do\b', 'DO'), (r'void\b', 'VOID'), (r'goto\b', 'GOTO'), (r'int\b', 'INT'), (r'char\b', 'CHAR'), (r'short\b', 'SHORT'), 
        (r'long\b', 'LONG'), (r'float\b', 'FLOAT'), (r'double\b', 'DOUBLE'), (r'signed\b', 'SIGNED'), (r'unsigned\b', 'UNSIGNED'), 
        (r'\(', 'LPAREN'), (r'\)', 'RPAREN'), (r'\{', 'LBRACE'), (r'\}', 'RBRACE'), (r'\[', 'LBRACKET'), (r'\]', 'RBRACKET'), (r'\;', 'SEMICOLON'), 
        (r'\:', 'COLON'), (r'\,', 'COMMA'), (r'\/\*', 'LCOMMENT'), (r'\*\/', 'RCOMMENT'), (r'\/\/(.*)', 'COMMENT'), (r'\.', 'DOT'), (r'\=\=', 'EQ'), 
        (r'\=', 'ASSIGN'), (r'\+\+', 'ADDADD'), (r'\+\=', 'ADDEQ'), (r'\+', 'ADD'), (r'\-\-', 'SUBSUB'), (r'\-\=', 'SUBEQ'), (r'\-', 'SUB'), (r'\*', 'MUL'), 
        (r'\/', 'DIV'), (r'\!\=', 'NEQ'), (r'\|\|', 'DBAR'), (r'\<', 'LT'), (r'\<\=', 'LTE'), (r'\>', 'GT'), (r'\>\=', 'GTE'), (r'\&', 'AMPERSAND'), 
        (r'\&\&', 'DAMPERSAND'), (r'\#', 'SHARP'), (r'[a-zA-Z]\w*', 'IDENTIFIER'), (r'\d+\.\d+', 'FLOAT_LIT'), (r'\d+', 'INTEGER_LIT'),
        (r'\"[^\"]*\"', 'STRING_LIT'), (r'\'[^\"]*\'', 'CHAR_LIT'), (r'\w+(\.\w+)+', 'SELECTED_NAME') 
]
# open the text file
file = open("test.txt","r") 

for line in file:
    line = line.strip("\n") # to remove the new line (\n) from the line
    print("\nin line : \" " + line + " \" ")
    for code in line.split():
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
            if re.search(regexp, code):
                print(code + " match to " + meanning)
                found = True
                break
        if found != True:
            print("No match!")
            found = False

# print(file.read())
