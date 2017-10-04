import sys

wordst = []
text = []
for line in sys.stdin.readlines():
	text.append(line) 
	# if there is no tab character, skip the line
	if '\t_\t_\t_\t_\t_\t_\t_' not in line:
		continue
	wordst.append(line)


alphabet = {}
fa = open('alphabet.txt', 'r')
for line in fa.readlines():
	line = line.strip('\n')
	(letter, translit) = line.split('\t')
	alphabet[letter] = translit
fa.close()

bigraphs = {}
fb = open('bigraphs.txt', 'r')
for line in fb.readlines():
	line = line.strip('\n')
	(bigraph, translit) = line.split('\t')
	bigraphs[bigraph] = translit
fb.close()

chdz = {}
fc = open('chdz.txt', 'r')
for line in fc.readlines():
	line = line.strip('\n')
	(bigraph, translit) = line.split('\t')
	chdz[bigraph] = translit
fb.close()


for i in range(len(text)):
	if text[i] in wordst:
			word = text[i].split('\t')[1] 
			translit = word
			for letter in chdz:
				if letter in word:
					translit = translit.replace(letter,chdz[letter])
			for letter in alphabet:
				if letter in word:
					translit = translit.replace(letter,alphabet[letter])
			for bigraph in bigraphs:
				if bigraph in translit:
					translit = translit.replace(bigraph,bigraphs[bigraph])	
			text[i] = text[i][0:len(text[i])-2] 
			text[i] += "Translit=" + translit
			#print(word + ' ' + translit)
s_text = ''
for line in text:
	s_text+=line
fw = open('transliterated.txt', 'w', 'utf-8')
fw.write(s_text)
fw.close()
#print(s_text)