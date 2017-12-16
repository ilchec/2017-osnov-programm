import sys

lemmas = {}
f = open('proj_corpus/wiki.txt', 'r')
for line in f:
	if len(line.split('\t')) == 2:
		s = line.strip('\n')
		lemmas[s.split('\t')[0]] = s.split('\t')[1]
f.close()
f = sys.stdin.readlines()
for line in f:
	# if there is no tab character, skip the line
	if len(line.split('\t')) == 10 and 'NOUN' in line:
		wordst.append(line)
f.close()