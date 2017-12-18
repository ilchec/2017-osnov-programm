The main program is inflections2.py. It takes the data extracted from Czech and Polish UDs and 
comes up with possible inflectional characteristics in the Upper Sorbian wiki.
As an input it takes a UD annotation of Wikipedia (it may be just tokenized of have some other annotation there) and 
outputs a file with lemmatized nouns in the 3rd column (if it was empty in the source file and only where possible) and
a set of possible inflectional characteristics in the 6th column (where possible and only if this column is empty).

Other programs extract the necessary data and create the files that are used by inflections2.py.
The files are already there so there is no need to run these programs.
