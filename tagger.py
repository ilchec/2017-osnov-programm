import sys

wordst = []
text = []
most_frequent_tag = ""
current_max = 0
current_max_dict = {}
token_tag = {}
tagged_wiki = {}	
fmodel = open(sys.argv[1], 'r')

for l in fmodel:
	line = l.strip('\n')
	if line == 'P\tcount\ttag\tform':
		continue
	line_arr = line.split('\t')
	if line_arr[3] == '—' and line_arr[3] != 'PUNCT':
		if float(line_arr[0]) > current_max:
			current_max = float(line_arr[0])
			most_frequent_tag = line_arr[2]
	else:
		if line_arr[3] not in token_tag:
			token_tag[line_arr[3]] = line_arr[2]
			current_max_dict[line_arr[3]] = float(line_arr[0])
		else:
			if float(line_arr[0]) > current_max_dict[line_arr[3]]:
				token_tag[line_arr[3]] = line_arr[2]
				current_max_dict[line_arr[3]] = float(line_arr[0])
			else: 
				continue
			
fmodel.close()

#print(most_frequent_tag)
#print(token_tag)

wiki = []
for line in sys.stdin.readlines():
	text.append(line) 
	# if there is no tab character, skip the line
	if len(line.split('\t')) == 10:
		wordst.append(line)
		wiki.append(line.split('\t')[1])

for word in wiki:
	if word in token_tag:
		tagged_wiki[word] = token_tag[word]
	else:
		tagged_wiki[word] = most_frequent_tag

for i in range(len(text)):
	if text[i] in wordst:
			word = text[i].split('\t')[1] 
			if word in tagged_wiki: 	
				text[i] = text[i].replace('\t_\t_\t_\t_\t_\t_\t_\t_','\t_\t'+tagged_wiki[word]+'\t_\t_\t_\t_\t_\t_') 
				#print(text[i])
	#else:
		#print(text[i])
s_text = ''
for line in text:
	s_text+=line
	print(line)