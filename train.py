import sys

wordst = []
text = []
tokens = 0
annotated_wiki = open("corpus/wiki_annotated.txt", "r")
for line in annotated_wiki:
	text.append(line) 
	# if there is no tab character, skip the line
	if '\t_\t_\t_' in line:
		wordst.append(line)
		tokens += 1
annotated_wiki.close()

def word_freq(text):
	freq = {}
	for line in text: 
	# if there is no tab character, skip the line
		form = line.split('\t')[1]
		if form not in freq:
			freq[form] = 0
		freq[form] += 1
	return freq

def tag_matrix(text):
	tag_matrix = {}
	tags = []
	words = []
	for line in text:
		if line.split("\t")[1] not in words:
			words.append(line.split("\t")[1])
	for line in text:
		if line.split("\t")[3] not in tags:
			tags.append(line.split("\t")[3])
	for tag in tags:
		word_tag_counter = 0
		for word in words:
			if word not in tag_matrix:
				tag_matrix[word] = {}
			word_tag_counter = 0
			for line in text:
				if "\t"+word+"\t" in line and  "\t"+tag+"\t" in line:
						word_tag_counter += 1
				if word_tag_counter != 0:
					tag_matrix[word][tag] = word_tag_counter
	del tag_matrix['']
	return tag_matrix

def tag_freq(text):
	tag_matrix = {}
	tags = []
	#counter = 0
	for line in text:
	#	counter += 1
		if line.split("\t")[3] not in tags:
			tags.append(line.split("\t")[3])
	#	print(str(counter)+" "+line.split("\t")[3])
	tag_matrix['—'] = {}
	for tag in tags:
		tag_counter = 0
		for line in text:
			if tag in line:
				tag_counter += 1
			tag_matrix["—"][tag] = tag_counter
	return tag_matrix

word_frequency = word_freq(wordst)
#print(word_frequency)
probability = ""
tm = tag_matrix(wordst)
tf = tag_freq(wordst)
#print(tm)
#print(tf)
for key in tf:
	for j in tf[key]:
		probability += str(round(tf[key][j]/tokens, 2))+"\t"+str(tf[key][j])+"\t"+j+"\t"+key+"\n"
probability.strip("\n")
for key in tm:
	for j in tm[key]:
		probability += str(round(tm[key][j]/word_frequency[key], 2))+"\t"+str(tm[key][j])+"\t"+j+"\t"+key+"\n"
probability = "P\tcount\ttag\tform\n" + probability
#print(probability)
	
filename = 	sys.argv[1]
fw = open(filename, 'w')
fw.write(probability)
fw.close()
