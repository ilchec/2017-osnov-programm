import sys

a = 0 # This is a variable for counting the number of vowels

for c in sys.stdin.read():
	print('Main loop:', a, c, file=sys.stderr)
	if c in 'аэиоуяеыёю':
		print('Found a vowel!', c, file=sys.stderr)
		a = a + 1

print(a)