import sys

lemmas = []
for line in sys.stdin.readlines():
	if line.strip('\n') != '':
		s = line.strip('\n')
		lemmas.append(s)

stems = []
sstems = '#lemma\tstem\n'
for lemma in lemmas:
	if lemma[-1] in 'aoey':
		s = lemma[:len(lemma)-1]
		stems.append(lemma+'\t'+s)
	else: stems.append(lemma+'\t'+lemma)
	
for element in stems:
	sstems += element+'\n'

fn = 	sys.argv[1]
fw = open(fn, 'w')
fw.write(sstems)
fw.close()