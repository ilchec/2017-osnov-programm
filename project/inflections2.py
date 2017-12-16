import sys

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

stems = {}
f = open('corpus/stems_cz.txt', 'r')
for line in f:
	if len(line.split('\t')) == 2 and "#" not in line:
		s = line.strip('\n')
		stems[s.split('\t')[0]] = s.split('\t')[1]
f.close()

text = []
wordst = []
wiki = []
for line in sys.stdin.readlines():
	text.append(line) 
	# if there is no tab character, skip the line
	if len(line.split('\t')) == 10:
		wordst.append(line)
		wiki.append(line.split('\t')[1].lower())


endings = ['', 'a', 'ej', 'om', 'je', 'o', 'u', 'y', 'i', 'e', 'aj', 'ow', 'omaj', 'ojo', 'ja', 'am', 'ami', 'emi', 'ach']
#endings = []
#fendings = open('corpus/endings.txt', 'r')
#for ending in fendings:
#	if ending.strip('\n') == '0':
#		endings.append('')
#	elif ending.strip('\n') == '':
#		continue
#	else:
#		endings.append(ending.strip('\n'))
#fendings.close()
#print(endings)

forms = {}
for lemma in stems:
	forms[lemma] = []
	for word in wiki:
		if stems[lemma] in word[:len(stems[lemma])]:
			if word not in forms[lemma]:
				for ending in endings:
					if stems[lemma]+ending == word:
						forms[lemma].append(word)
res_forms = {}
for lemma in forms:	
	if 	forms[lemma] != []:
		res_forms[lemma] = forms[lemma]
forms = res_forms
		
#for element in forms:
#	if forms[element] != []:
		#forms[element] = tuple(forms[element])
#		print(element, forms[element])

#reading the file with declensions, note that gender is not about agreement, it is an inflection label
declensions = {}
fd = open('corpus/inflections-new.txt', 'r')
for line in fd:
	s = line.strip('\n')
	gender = s.split('\t')[0]
	case = s.split('\t')[1]
	markers = s.split('\t')[2].split(',')
	if gender not in declensions:
		declensions[gender] = []
		d = {}
		d[case] = markers
		declensions[gender].append(d)
	else:
		d = {}
		d[case] = markers
		declensions[gender].append(d)
fd.close()
#print(declensions)

genders = {}
for lemma in forms:
	if lemma[-1] == 'a':
		genders[lemma] = ['f']
	elif lemma[-1] in 'oe':
		genders[lemma] = ['n']
	else:
		genders[lemma] = ['f1','m']
#print(genders)

annotated = {}
for lemma in forms:
	if lemma not in annotated:
		annotated[lemma] = {}
	for form in forms[lemma]:
		if form == stems[lemma]:
			form_end = form + '0'
		else: 
			form_end = form
		for gender in genders[lemma]:
			#print(lemma+' '+gender)
			for pair in declensions[gender]:
				#print(pair)
				for set in pair:
					#print(set)
					for ending in pair[set]:
						#print(form+' '+form_end[len(stems[lemma])-1:])
						if form_end[len(stems[lemma]):] == ending:
							if form in annotated[lemma]:
								if gender in annotated[lemma][form]:
									annotated[lemma][form][gender].append(set)
								else:
									annotated[lemma][form][gender] = []
									annotated[lemma][form][gender].append(set)
							else:
								annotated[lemma][form] = {}
								annotated[lemma][form][gender] = []
								if 'nom,sg' in set and form != lemma:
									continue
								annotated[lemma][form][gender].append(set)
						else: 
							continue
#print(annotated)
#Checking gender consistency, if there is more than one form for a lemma 
#and some of the genders are not found for at least one of the forms, then
#the word is not of this gender and the annotation can be improved.

gender_check = {}
for lemma in annotated:
	gender_check[lemma] = []
	if len(annotated[lemma]) == 1 or genders[lemma] in [['f'], ['n']]:
		gender_check[lemma].append(genders[lemma])
	for gender in ['f', 'f1', 'n', 'm']:
		counter = {gender:0}
		for form in annotated[lemma]:
			if gender in annotated[lemma][form]:
				counter[gender] += 1
		if counter[gender] == len(annotated[lemma]):
			 gender_check[lemma].append(gender)

annotated_clear = {}
for lemma in annotated:
	if lemma not in annotated_clear:
		annotated_clear[lemma] = {}
	for form in annotated[lemma]:
		if form not in annotated_clear[lemma]:
			annotated_clear[lemma][form] = {}
		for gender in annotated[lemma][form]:
			if gender in gender_check[lemma]:
				annotated_clear[lemma][form][gender] = annotated[lemma][form][gender]
			else: 
				continue
#print(annotated_clear)

for i in range(len(text)):
	if text[i] in wordst:
			line_array = text[i].split('\t')
			word = str(line_array[1])
			morphology = str(line_array[5])
			if hasNumbers(word) == True:
				line_array[3] = 'NUM'
				line_array[2] = word
			for lemma in annotated_clear:
				if word in annotated_clear[lemma]:
					if line_array[2] == '_':
						line_array[2] = lemma
					if line_array[3] == '_':
						line_array[3] = 'NOUN'
					if line_array[5] == '_':
						morphology = 'Possible inflectional characteristics. '
						for gender in annotated_clear[lemma][word]:
							morphology += 'Gender='+gender+': '
							for set in annotated_clear[lemma][word][gender]:
								morphology += set+', '
							morphology = morphology[:len(morphology)-2]
							morphology += ". "
			text[i] =  line_array[0]+'\t'+line_array[1]+'\t'+line_array[2]+'\t'+line_array[3]+'\t'+line_array[4]+'\t'+morphology+'\t'+line_array[6]+'\t'+line_array[7]+'\t'+line_array[8]+'\t'+line_array[9]
				#print(text[i])
	#else:
		#print(text[i])
s_text = ''
for line in text:
	s_text+=line
	print(line)

#Сделать программу, которая будет определять список возможных склонений 
#существительного по правилам из грамматики, учесть при этом палатализацию

#Задать списком возможные суффиксы в каждом склонении
#Дальше применять этот код
				
				
			