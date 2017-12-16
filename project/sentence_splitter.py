import sys
s = ''
for line in sys.stdin.readlines():
	s += line
fsplitted = s.split('. ')
for i in fsplitted:
	print(i+'.\n\n')
