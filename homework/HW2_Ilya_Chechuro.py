import sys

#f = open('/Users/ilchec/Documents/Учеба/Masters_Python/2017-osnov-programm/wiki.txt', 'r')
#s = ''
#for line in f:
#	s += line
lines = 0
words = 0
characters = 0
s = ""
for i in sys.stdin.read():
	s+= i
	if i == '\n':
		lines += 1
		words += 1
	if i == ' ':
		words += 1
	characters += 1
words += 1

#count ".\n" as well because sentences in the ends of paragraphs are not counted by ". "
avg = (len(s.split(". "))+len(s.split(".\n")))/len(s.split("\n"))

print ('lines: ' + str(lines) + ', words: ' + str(words) + ', characters: ' + str(characters) + ', average: ' + str(avg) + " sent/par.")