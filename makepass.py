import difflib
import string
from random import *

count =0
numberofentries = 1000000
with open('diff.txt', 'w') as result:
    while count < numberofentries:
        print(count)
        count +=1
        min_char=8
        max_char=8
        allchar = string.ascii_lowercase + string.digits
        password = "".join(choice(allchar)for x in range(randint(min_char,max_char)))
        print("this is the pass", password)
        result.write(password+"\n")
