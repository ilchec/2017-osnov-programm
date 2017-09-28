import sys

f = open('/Users/ilchec/Documents/Учеба/Masters_Python/2017-osnov-programm/wiki.txt', 'r')
s = ''
for line in f:
	s += line
fsplitted = s.split('. ')
f_w = open('/Users/ilchec/Documents/Учеба/Masters_Python/2017-osnov-programm/wiki_splitted.txt', 'w')
for i in fsplitted:
	f_w.write(i+'.\n\n')
f_w.close()
f.close()