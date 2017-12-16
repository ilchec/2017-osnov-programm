import sys
i=1
for line in sys.stdin.readlines():
	if line.strip()=='':
		continue
	source_line = line.replace('\n','')
	print('#sent_id = %d\n#text = %s' % (i, source_line))
	for p in '.,?()!:\"\'':
		if p == '(':
			line = line.replace(p, p+' ')
		else:
			line = line.replace(p, ' '+p)
	tokens = line.split(' ')
	counter = 1
	for token in tokens:
		if token.strip() == '':
			continue
		for ch in '\r\n':
			token = token.replace(ch,'')
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (counter, token))
		counter+=1
	i+=1
	print('')
