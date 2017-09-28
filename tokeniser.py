import sys
i=1
for line in sys.stdin.readlines():
	source_line = line
	for p in '.,?()!':
		line = line.replace(p, ' '+p)
	tokens = line.split(' ')
	print('sent_id = %d\ntext = %s' % (i, source_line))
	counter = 1
	for token in tokens:
		for ch in '\r\n':
			token = token.replace(ch,'')
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (counter, token))
		counter+=1
	print('\n')
	i+=1