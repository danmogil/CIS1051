import re

def main():
   stdIn = input("Word: ")
   while stdIn != "done":
      print(convertToPigLatin(stdIn).lower())
      stdIn = input("Word: ")

def convertToPigLatin(s):
   i = findFirstVowel(s)
   if i == 0:
      return (s[1:] + s[0] + "way")
   return (s[i:] + s[:i] + "ay")

def findFirstVowel(s):
   res = re.search('[aeiouAEIOU]', s)
   return res.start() if res != None else len(s) - 1

def reverse():
   stdIn = input("Word: ")
   while stdIn != "done":
      print(stdIn[::-1].lower())
      stdIn = input("Word: ")

#init

main()
# reverse()