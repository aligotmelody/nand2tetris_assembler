
import re


with open("ass_test.txt", "r") as F:
    source = F.readlines()

address = re.compile(r'\@[0-9]+')
def compare(s):
    return bool(address.match(s))

counter = 0
for line in source:
    print(line)
    if compare(line):
        counter +=1

print(counter)