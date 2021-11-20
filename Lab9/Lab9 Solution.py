import re
import random

fl = open('words.txt')
text = fl.read()
fl.close()


#answers

#1.1 
re.findall(r'dog|cat', text, re.IGNORECASE) #428
#1.2 
re.findall(r'\b[a-z]{4}\b', text, re.IGNORECASE) #2243
#1.3
re.findall(r'hun', text, re.IGNORECASE) #49
#1.4
re.findall(r'ing\b', text, re.IGNORECASE) #3702
#1.5
re.findall(r'q[^u]', text, re.IGNORECASE) #5
#1.6
re.findall(r'\b[^aeiou\s]+\b', text, re.IGNORECASE) #58
#1.7
re.findall(r'\b[aeiou]+\b', text, re.IGNORECASE) #13
#1.8
re.findall(r'nt\b', text, re.IGNORECASE) #731
#1.9
re.findall(r'[aeiou]{2}', text, re.IGNORECASE) #15645
#1.10
#?

#2.1
# .* selects everything until a newline. ? makes the * not greedy, thereby matching the fewest character possible (none).
#2.2
pattern = r'[A-Z][a-zA-Z]+ Nakamoto'
#2.3
pattern2 = r'twenty|thirty|fourty|fifty|sixty|seventy|eighty|ninety(-(one|two|three|four|five|six|seven|eight|nine))?'
#2.4
pattern3 = r'\$([0-9]{1,3},?)+(\.[0-9]{2})?'

#3
#assumed number/letter characters only
def strongPasswordDetection(password : str) -> bool:
    return True if (re.search(r'\w{8,}', password) and re.search(r'[a-z]', password) 
    and re.search(r'[A-Z]', password) and re.search(r'\d', password)) else False

# print(strongPasswordDetection('abcDE123'))

#4
def passwordGenerator() -> str:
    with open('words.txt') as f:
        text = f.read()
        words : list = re.findall(r'[a-z]{4,}', text)
        random.shuffle(words)
        return f'{words[0]}{words[1]}{words[2]}{words[3]}'

# print(passwordGenerator())