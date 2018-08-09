# A Python program to print all
# permutations of given length
from itertools import permutations

# Get all permutations of length 2
# and length 2
perm = permutations(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',1,2,3,4,5,6,7,8,9], 8)

# Print the obtained permutations
count = 0
with open('diff.txt', 'w') as result:
    for i in perm:
        # print(i)
        count = count + 1
        passthis = str(i).replace('(',"").replace(')',"").replace(',',"").replace(" ", "").replace("'","")
        print(count)
        result.write(passthis+"\n")


