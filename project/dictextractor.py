import sys

wordst = []
f = sys.stdin.readlines()
for line in f:
	# if there is no tab character, skip the line
	if len(line.split('\t')) == 10 and 'NOUN' in line:
		wordst.append(line.lower())

def lemma_extractor(text):
	lemmas = []
	slemmas = ''
	for line in text:
		lemma = line.split("\t")[2].lower()
		if lemma not in lemmas:
			lemmas.append(lemma)
	for element in lemmas:
		if len(element)>2:
			slemmas += element+'\n'
	return slemmas

#print(lemma_extractor(wordst))
fn = 	sys.argv[1]
fw = open(fn, 'w')
fw.write(lemma_extractor(wordst))
fw.close()