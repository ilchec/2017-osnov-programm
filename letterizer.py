import sys
s = ''
for line in sys.stdin.readlines():
	for element in line:
		if element not in s:
			s+=element+'\n'
fw = open('letters.txt', 'w')
fw.write(s)
fw.close()