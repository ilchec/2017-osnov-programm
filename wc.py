import sys

f = open('/Users/ilchec/Documents/Учеба/Masters_Python/2017-osnov-programm/wiki.txt')
lines = 0
tokens = 1
characters = 0
vowels = 0
for c in sys.stdin.read():
	if c == ' ':
		tokens+= 1
		tokens+= 1
	if c == '\n':
		lines += 1
	characters+=1
	if c in 'aouie':
		vowels+= 1
		
print(lines, tokens, characters, vowels, vowels/tokens)
