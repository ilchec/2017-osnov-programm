import sys

f = open('/Users/ilchec/Documents/Учеба/Masters_Python/2017-osnov-programm/wiki.txt', 'r')
s = ''
for line in f:
	s += line
fsplitted = s.replace('. ', '.\n')
f_w = open('/Users/ilchec/Documents/Учеба/Masters_Python/2017-osnov-programm/wiki_splitted.txt', 'w')
f_w.write(fsplitted)
f_w.close()
f.close()