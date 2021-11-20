import re

VOWELS = {
    'a': 'ah',
    'e': 'eh',
    'i': 'ee',
    'o': 'oh',
    'u': 'oo'
}

PAIRS = {
    'iw': 'v',
    'ew': 'v',
    'ai': 'eye',
    'ae': 'eye',
    'ao': 'ow',
    'au': 'ow',
    'ei': 'ay',
    'eu': 'eh-oo',
    'iu': 'ew',
    'oi': 'oyo',
    'ou': 'ow',
    'ui': 'ooey',
}

def pronounce():
    STDin = input("Enter a hawaiian word to pronounce: ").strip().lower()
    valid = "aeioupkhlmnw '"
    out = ""
    i = 0
    while i < len(STDin):
        char = STDin[i]
        if re.search(char, valid) == None:
            return "{} is not a valid hawaiian character".format(char.upper())
        
        if char in VOWELS:
            if i < len(STDin) - 1:
                comb = STDin[i] + STDin[i + 1]
                if comb in PAIRS:
                    i += 1
                    if i + 1 < len(STDin):
                        if comb[1] != ' ':
                            out += "{}-".format(PAIRS[comb])
                        else:
                            out += PAIRS[comb]
                    else:
                        out += PAIRS[comb]
                        break
                else:
                    if comb[1] != ' ':
                        out += "{}-".format(VOWELS[char])
                    else:
                        out += VOWELS[char]
            else:
                out += VOWELS[char]
        else:
            out += char
        i += 1
    return "{} is pronounced {}".format(STDin.upper(), out.capitalize())

sw = True
while sw:
    print(pronounce())
    x = input("Do you want to enter another word? (Y/YES/N/NO) ").upper()
    sw = x == 'YES' or x == "Y"