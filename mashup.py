#Kay Savetz November 28 2022. Code and book are in the public domain.

import re
import random

def num_sort(test_string):
	#sort lines of BASIC code by their line numbers
    return list(map(int, re.findall(r'\d+', test_string)))[0]

#pick two victims
choice1 = random.randint(1, 102)
choice2 = random.randint(1, 102)

#get both program filenames
x1 = open("_proglist.txt", "r")
content_list = x1.readlines()
name1=content_list[choice1].strip()
name2=content_list[choice2].strip()

#get both program titles
x1 = open("_prognames.txt", "r")
content_list = x1.readlines()
title1=content_list[choice1].strip()
title2=content_list[choice2].strip()

#title of the program is a mashup of words from the two original program names
print("0 PRINT \"### " + random.choice(title1.split()) + " " + random.choice(title2.split()) + "\"")

#40 lines of code from each program seems about right?
prog=(random.sample(list(open(name1)),40))
prog2=(random.sample(list(open(name2)),40))
prog = prog + prog2

#remove BASIC keywords pretty much guaranteed to keep the program from running in this context
prog = [ x for x in prog if "GOTO" not in x and "FOR" not in x and "NEXT" not in x and "THEN" not in x  and "IF" not in x and "GOSUB" not in x and "RETURN" not in x and "DEF " not in x and "READ " not in x]

#put program lines in order. if I had more time/was less lazy I'd remove duplicate line numbers, leaving only the last one
prog.sort(key=num_sort)

#list to string
prog= (''.join(prog))

#voila
print(prog)

